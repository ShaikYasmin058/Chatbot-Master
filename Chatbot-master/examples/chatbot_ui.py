# import tkinter as tk
# from tkinter import scrolledtext, messagebox
# import wikipedia
# import pickle
# import re
# import warnings
# import pyttsx3
# import datetime
# import os

# warnings.filterwarnings("ignore")

# # === Text-to-Speech (TTS) ===
# tts_engine = pyttsx3.init()
# def speak(text):
#     tts_engine.say(text)
#     tts_engine.runAndWait()

# # === Load Model and Vectorizer ===
# try:
#     model = pickle.load(open("model.pkl", "rb"))
#     vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
# except Exception as e:
#     print("❌ Error loading model or vectorizer:", e)
#     exit()

# # === Wikipedia Summary Handler ===
# def get_wikipedia_summary(query):
#     try:
#         query = query.lower()
#         query = re.sub(r"(what is|who is|tell me about|explain)", "", query).strip()

#         special_terms = {
#             "ai": "Artificial intelligence",
#             "python": "Python (programming language)",
#             "java": "Java (programming language)",
#             "apple": "Apple Inc.",
#             "tesla": "Tesla, Inc.",
#             "turing": "Alan Turing",
#             "elon musk": "Elon Musk",
#             "cm of ap": "Chief Minister of Andhra Pradesh",
#             "andhra pradesh cm": "Chief Minister of Andhra Pradesh",
#             "prime minister of india": "Prime Minister of India",
#             "president of india": "President of India"
#         }

#         mapped_query = special_terms.get(query, query)
#         return wikipedia.summary(mapped_query, sentences=2)

#     except wikipedia.exceptions.DisambiguationError as e:
#         return f"⚠️ Too many meanings. Be specific (e.g., {e.options[:2]})"
#     except wikipedia.exceptions.PageError:
#         return "❌ Topic not found on Wikipedia."
#     except Exception as e:
#         return f"❌ Error: {str(e)}"

# # === ML Model Response with Confidence ===
# def get_model_response(user_input):
#     try:
#         x = vectorizer.transform([user_input])
#         prediction = model.predict(x)[0]
#         probas = model.predict_proba(x)[0]
#         confidence = max(probas)
#         return f"{prediction} (Confidence: {confidence:.2f})"
#     except Exception as e:
#         return "❌ Sorry, I didn't understand that."

# # === GUI Setup ===
# root = tk.Tk()
# root.title("Smart AI ChatBot")
# root.geometry("700x550")
# root.config(bg="#f2f2f2")

# chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 13), width=80, height=20, bg="#ffffff")
# chat_display.pack(padx=10, pady=10)
# chat_display.insert(tk.END, "🤖 Bot: Hello! Ask me anything.\n")
# chat_display.config(state=tk.DISABLED)

# entry_frame = tk.Frame(root, bg="#f2f2f2")
# entry_frame.pack(pady=10)

# entry = tk.Entry(entry_frame, font=("Arial", 13), width=55)
# entry.pack(side=tk.LEFT, padx=10)

# def save_chat_log(user_input, response):
#     with open("chat_log.txt", "a", encoding="utf-8") as file:
#         now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
#         file.write(f"{now} - You: {user_input}\n{now} - Bot: {response}\n\n")

# # === Send Button Function ===
# def send():
#     user_input = entry.get()
#     if not user_input.strip():
#         return

#     entry.delete(0, tk.END)
#     chat_display.config(state=tk.NORMAL)
#     chat_display.insert(tk.END, f"You: {user_input}\n")

#     if any(word in user_input.lower() for word in ["who is", "what is", "tell me about", "explain", "cm", "prime minister", "president"]):
#         response = get_wikipedia_summary(user_input)
#     else:
#         response = get_model_response(user_input)

#     chat_display.insert(tk.END, f"Bot: {response}\n\n")
#     chat_display.config(state=tk.DISABLED)
#     chat_display.yview(tk.END)

#     speak(response)
#     save_chat_log(user_input, response)

# # === Button Controls ===
# send_button = tk.Button(entry_frame, text="Send", command=send, font=("Arial", 12), bg="#4CAF50", fg="white", width=8)
# send_button.pack(side=tk.LEFT, padx=5)

# clear_button = tk.Button(root, text="Clear Chat", font=("Arial", 10), bg="#f44336", fg="white", command=lambda: chat_display.config(state=tk.NORMAL) or chat_display.delete(1.0, tk.END) or chat_display.insert(tk.END, "🤖 Bot: Hello again! Ask me anything.\n") or chat_display.config(state=tk.DISABLED))
# clear_button.pack(pady=5)

# entry.bind("<Return>", lambda event: send())

# # === Exit Button (Optional) ===
# def close_app():
#     if messagebox.askokcancel("Quit", "Do you want to exit?"):
#         root.destroy()

# root.protocol("WM_DELETE_WINDOW", close_app)

# root.mainloop()






# import tkinter as tk
# from tkinter import scrolledtext, messagebox
# import wikipedia
# import pickle
# import re
# import warnings
# import pyttsx3
# import datetime
# import os

# warnings.filterwarnings("ignore")

# # === Text-to-Speech (TTS) ===
# tts_engine = pyttsx3.init()
# def speak(text):
#     tts_engine.say(text)
#     tts_engine.runAndWait()

# # === Load Model and Vectorizer ===
# try:
#     model = pickle.load(open("model.pkl", "rb"))
#     vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
# except Exception as e:
#     print("❌ Error loading model or vectorizer:", e)
#     exit()

# # === Wikipedia Summary Handler ===
# def get_wikipedia_summary(query):
#     try:
#         query = query.lower()
#         query = re.sub(r"(what is|who is|tell me about|explain)", "", query).strip()

#         special_terms = {
#             "ai": "Artificial intelligence",
#             "python": "Python (programming language)",
#             "java": "Java (programming language)",
#             "apple": "Apple Inc.",
#             "tesla": "Tesla, Inc.",
#             "turing": "Alan Turing",
#             "elon musk": "Elon Musk",
#             "cm of ap": "Chief Minister of Andhra Pradesh",
#             "andhra pradesh cm": "Chief Minister of Andhra Pradesh",
#             "prime minister of india": "Prime Minister of India",
#             "president of india": "President of India"
#         }

#         mapped_query = special_terms.get(query, query)
#         return wikipedia.summary(mapped_query, sentences=2)

#     except wikipedia.exceptions.DisambiguationError as e:
#         return f"⚠️ Too many meanings. Be specific (e.g., {e.options[:2]})"
#     except wikipedia.exceptions.PageError:
#         return "❌ Topic not found on Wikipedia."
#     except Exception as e:
#         return f"❌ Error: {str(e)}"

# # === ML Model Response with Confidence ===
# def get_model_response(user_input):
#     try:
#         x = vectorizer.transform([user_input])
#         prediction = model.predict(x)[0]
#         probas = model.predict_proba(x)[0]
#         confidence = max(probas)
#         return f"{prediction} (Confidence: {confidence:.2f})"
#     except Exception as e:
#         return "❌ Sorry, I didn't understand that."

# # === GUI Setup ===
# root = tk.Tk()
# root.title("Smart AI ChatBot")
# root.geometry("700x550")
# root.config(bg="#f2f2f2")

# chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 13), width=80, height=20, bg="#ffffff")
# chat_display.pack(padx=10, pady=10)
# chat_display.insert(tk.END, "🤖 Bot: Hello! Ask me anything.\n")
# chat_display.config(state=tk.DISABLED)

# entry_frame = tk.Frame(root, bg="#f2f2f2")
# entry_frame.pack(pady=10)

# entry = tk.Entry(entry_frame, font=("Arial", 13), width=55)
# entry.pack(side=tk.LEFT, padx=10)

# # === Global variable to store last bot response ===
# last_bot_response = ""

# def save_chat_log(user_input, response):
#     with open("chat_log.txt", "a", encoding="utf-8") as file:
#         now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
#         file.write(f"{now} - You: {user_input}\n{now} - Bot: {response}\n\n")

# # === Send Button Function ===
# def send():
#     global last_bot_response
#     user_input = entry.get()
#     if not user_input.strip():
#         return

#     entry.delete(0, tk.END)
#     chat_display.config(state=tk.NORMAL)
#     chat_display.insert(tk.END, f"You: {user_input}\n")

#     if any(word in user_input.lower() for word in ["who is", "what is", "tell me about", "explain", "cm", "prime minister", "president"]):
#         response = get_wikipedia_summary(user_input)
#     else:
#         response = get_model_response(user_input)

#     last_bot_response = response  # Store the response for TTS
#     chat_display.insert(tk.END, f"Bot: {response}\n\n")
#     chat_display.config(state=tk.DISABLED)
#     chat_display.yview(tk.END)

#     save_chat_log(user_input, response)

# # === Speak Button Function ===
# def speak_last_response():
#     if last_bot_response:
#         speak(last_bot_response)

# # === Button Controls ===
# send_button = tk.Button(entry_frame, text="Send", command=send, font=("Arial", 12), bg="#4CAF50", fg="white", width=8)
# send_button.pack(side=tk.LEFT, padx=5)

# clear_button = tk.Button(root, text="Clear Chat", font=("Arial", 10), bg="#f44336", fg="white",
#                          command=lambda: chat_display.config(state=tk.NORMAL) or chat_display.delete(1.0, tk.END) or
#                                          chat_display.insert(tk.END, "🤖 Bot: Hello again! Ask me anything.\n") or
#                                          chat_display.config(state=tk.DISABLED))
# clear_button.pack(pady=5)

# speak_button = tk.Button(root, text="🔊 Speak", font=("Arial", 10), bg="#2196F3", fg="white", command=speak_last_response)
# speak_button.pack(pady=5)

# entry.bind("<Return>", lambda event: send())

# # === Exit Button (Optional) ===
# def close_app():
#     if messagebox.askokcancel("Quit", "Do you want to exit?"):
#         root.destroy()

# root.protocol("WM_DELETE_WINDOW", close_app)

# root.mainloop()




import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import wikipedia
import pickle
import re
import warnings
import pyttsx3
import datetime
from googletrans import Translator
from fpdf import FPDF

warnings.filterwarnings("ignore")

# === Text-to-Speech (TTS) ===
tts_engine = pyttsx3.init()
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# === Load Model and Vectorizer ===
try:
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
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
        return f"⚠️ Too many meanings. Be specific (e.g., {e.options[:2]})"
    except wikipedia.exceptions.PageError:
        return "❌ Topic not found on Wikipedia."
    except Exception as e:
        return f"❌ Error: {str(e)}"

# === ML Model Response with Confidence ===
def get_model_response(user_input):
    greetings = ["hi", "hello", "hlo", "hey"]
    if user_input.strip().lower() in greetings:
        return "Hello! How can I assist you today? 😊"

    try:
        x = vectorizer.transform([user_input])
        prediction = model.predict(x)[0]
        probas = model.predict_proba(x)[0]
        confidence = max(probas)
        if confidence < 0.5:
            return "🤔 I'm not confident. Could you please rephrase?"
        return f"{prediction} (Confidence: {confidence:.2f})"
    except Exception as e:
        return "❌ Sorry, I didn't understand that."


# === Translation ===
translator = Translator()
def translate_response(response, lang):
    try:
        translated = translator.translate(response, dest=lang)
        return translated.text
    except Exception as e:
        return f"⚠️ Translation failed: {str(e)}"

# === GUI Setup ===
root = tk.Tk()
root.title("Smart AI ChatBot")
root.geometry("800x600")
root.config(bg="#f2f2f2")

is_dark = False
auto_speak = False
last_bot_response = ""
chat_log = []

# === Chat Area ===
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 13), width=90, height=20, bg="#ffffff")
chat_display.pack(padx=10, pady=10)
chat_display.insert(tk.END, "🤖 Bot: Hello! Ask me anything.\n")
chat_display.config(state=tk.DISABLED)

# === Input Area ===
entry_frame = tk.Frame(root, bg="#f2f2f2")
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, font=("Arial", 13), width=55)
entry.pack(side=tk.LEFT, padx=10)

# === Send Button Function ===
def send():
    global last_bot_response
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

    # Translate if language selected
    selected_lang = lang_var.get()
    if selected_lang != "English":
        lang_codes = {"Telugu": "te", "Hindi": "hi"}
        response = translate_response(response, lang_codes[selected_lang])

    last_bot_response = response
    chat_log.append((user_input, response))

    chat_display.insert(tk.END, f"Bot: {response}\n\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)

    if auto_speak:
        speak(response)

# === Speak Button ===
def speak_last_response():
    if last_bot_response:
        speak(last_bot_response)

# === Toggle Dark Mode ===
def toggle_theme():
    global is_dark
    is_dark = not is_dark
    bg = "#1e1e1e" if is_dark else "#f2f2f2"
    fg = "#ffffff" if is_dark else "#000000"
    chat_display.config(bg=bg, fg=fg)
    root.config(bg=bg)
    entry_frame.config(bg=bg)
    entry.config(bg="#ffffff", fg="#000000")

# === Toggle Auto Speak ===
def toggle_voice_mode():
    global auto_speak
    auto_speak = not auto_speak
    mode = "enabled" if auto_speak else "disabled"
    messagebox.showinfo("Voice Mode", f"Auto Speak is now {mode.upper()}.")

# === Export Chat as PDF ===
def export_chat():
    if not chat_log:
        messagebox.showwarning("No Chat", "There's no chat to export.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for user, bot in chat_log:
        pdf.multi_cell(0, 10, f"You: {user}")
        pdf.multi_cell(0, 10, f"Bot: {bot}\n")

    file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file:
        pdf.output(file)
        messagebox.showinfo("Exported", f"Chat saved to {file}")

# === Buttons ===
send_button = tk.Button(entry_frame, text="Send", command=send, font=("Arial", 12), bg="#4CAF50", fg="white", width=8)
send_button.pack(side=tk.LEFT, padx=5)

speak_button = tk.Button(root, text="🔊 Speak", font=("Arial", 10), bg="#2196F3", fg="white", command=speak_last_response)
speak_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Chat", font=("Arial", 10), bg="#f44336", fg="white", 
                         command=lambda: chat_display.config(state=tk.NORMAL) or chat_display.delete(1.0, tk.END) or 
                                         chat_display.insert(tk.END, "🤖 Bot: Hello again! Ask me anything.\n") or 
                                         chat_display.config(state=tk.DISABLED))
clear_button.pack(pady=5)

theme_button = tk.Button(root, text="🌙 Toggle Theme", font=("Arial", 10), command=toggle_theme)
theme_button.pack(pady=2)

voice_button = tk.Button(root, text="🗣️ Toggle Voice", font=("Arial", 10), command=toggle_voice_mode)
voice_button.pack(pady=2)

export_button = tk.Button(root, text="📤 Export Chat to PDF", font=("Arial", 10), command=export_chat)
export_button.pack(pady=2)

# === Language Dropdown ===
lang_var = tk.StringVar(value="English")
lang_menu = tk.OptionMenu(root, lang_var, "English", "Telugu", "Hindi")
lang_menu.config(font=("Arial", 10))
lang_menu.pack(pady=2)

entry.bind("<Return>", lambda event: send())

# === Exit Button ===
def close_app():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()
