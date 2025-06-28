import tkinter as tk
from tkinter import scrolledtext
import wikipedia
import pickle
import re
import warnings
import pyttsx3

warnings.filterwarnings("ignore")

# === Text-to-Speech (TTS) ===
tts_engine = pyttsx3.init()
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# === Load Model and Vectorizer ===
try:
    model = pickle.load(open("../model.pkl", "rb"))
    vectorizer = pickle.load(open("../vectorizer.pkl", "rb"))

except Exception as e:
    print("❌ Error loading model or vectorizer:", e)
    exit()

# === Wikipedia Summary Handler ===
def get_wikipedia_summary(query):
    try:
        query = query.lower()
        query = re.sub(r"(what is|who is|tell me about|explain)", "", query).strip()

        special_terms = {
            "ai": "Artificial intelligence",
            "python": "Python (programming language)",
            "java": "Java (programming language)",
            "apple": "Apple Inc.",
            "tesla": "Tesla, Inc.",
            "turing": "Alan Turing",
            "elon musk": "Elon Musk",
            "cm of ap": "Chief Minister of Andhra Pradesh",
            "andhra pradesh cm": "Chief Minister of Andhra Pradesh",
            "prime minister of india": "Prime Minister of India",
            "president of india": "President of India"
        }

        mapped_query = special_terms.get(query, query)
        return wikipedia.summary(mapped_query, sentences=2)

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many meanings. Be more specific (e.g., {e.options[:2]})"
    except wikipedia.exceptions.PageError:
        return "❌ Topic not found on Wikipedia."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# === ML Model Response with Confidence ===
def get_model_response(user_input):
    try:
        x = vectorizer.transform([user_input])
        prediction = model.predict(x)[0]
        probas = model.predict_proba(x)[0]
        confidence = max(probas)
        return f"{prediction} (Confidence: {confidence:.2f})"
    except Exception as e:
        return "❌ Sorry, I didn't understand that."

# === GUI Setup ===
root = tk.Tk()
root.title("Smart AI ChatBot")
root.geometry("650x500")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 13), width=75, height=20)
chat_display.pack(padx=10, pady=10)
chat_display.insert(tk.END, "Bot: Hello! Ask me anything.\n")
chat_display.config(state=tk.DISABLED)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, font=("Arial", 13), width=50)
entry.pack(side=tk.LEFT, padx=10)

# === On Send ===
def send():
    user_input = entry.get()
    if not user_input.strip():
        return

    entry.delete(0, tk.END)
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_input}\n")

    if any(word in user_input.lower() for word in ["who is", "what is", "tell me about", "explain", "cm", "prime minister", "president"]):
        response = get_wikipedia_summary(user_input)
    else:
        response = get_model_response(user_input)

    chat_display.insert(tk.END, f"Bot: {response}\n\n")
    speak(response)
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)

# === Send Button ===
send_button = tk.Button(entry_frame, text="Send", command=send, font=("Arial", 12))
send_button.pack(side=tk.LEFT)

entry.bind("<Return>", lambda event: send())

root.mainloop()
