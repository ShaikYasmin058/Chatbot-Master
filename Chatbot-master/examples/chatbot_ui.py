# from chatbot import Chat
# import tkinter as tk
# from tkinter import scrolledtext, PhotoImage
# import os

# # Load Chatbot
# chat = Chat("Hebrew.template")

# # GUI setup
# root = tk.Tk()
# root.title("Hebrew ChatBot")

# # Banner image (optional)
# # image_path = os.path.join("images", "banner.png")
# # if os.path.exists(image_path):
# #     img = PhotoImage(file=image_path)
# #     banner = tk.Label(root, image=img)
# #     banner.pack()

# # Chat display
# chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 14), width=60, height=20)
# chat_display.pack(padx=10, pady=10)
# chat_display.insert(tk.END, "Bot: שלום, איך אפשר לעזור?\n")
# chat_display.config(state=tk.DISABLED)

# # Entry + Send Button
# frame = tk.Frame(root)
# frame.pack()

# entry = tk.Entry(frame, font=("Arial", 14), width=40)
# entry.pack(side=tk.LEFT, padx=(10, 5))

# def send():
#     user_input = entry.get()
#     if user_input.strip() == "":
#         return
#     entry.delete(0, tk.END)
    
#     chat_display.config(state=tk.NORMAL)
#     chat_display.insert(tk.END, f"You: {user_input}\n")
#     response = chat.respond(user_input, session_id="hebrew_session")
#     chat_display.insert(tk.END, f"Bot: {response}\n\n")
#     chat_display.config(state=tk.DISABLED)
#     chat_display.yview(tk.END)

# send_button = tk.Button(frame, text="Send", command=send)
# send_button.pack(side=tk.LEFT, padx=(5, 10))

# entry.bind("<Return>", lambda event: send())

# root.mainloop()


# from chatbot import Chat
# import tkinter as tk
# from tkinter import scrolledtext
# import os

# chat = Chat("Chatbot-master/examples/Example.template")


# root = tk.Tk()
# root.title("ChatBot UI")

# chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 14), width=60, height=20)
# chat_display.pack(padx=10, pady=10)
# chat_display.insert(tk.END, "Bot: Hello! How can I help you?\n")
# chat_display.config(state=tk.DISABLED)

# frame = tk.Frame(root)
# frame.pack()

# entry = tk.Entry(frame, font=("Arial", 14), width=40)
# entry.pack(side=tk.LEFT, padx=(10, 5))

# def send():
#     user_input = entry.get()
#     if user_input.strip() == "":
#         return
#     entry.delete(0, tk.END)
    
#     chat_display.config(state=tk.NORMAL)
#     chat_display.insert(tk.END, f"You: {user_input}\n")
#     response = chat.respond(user_input, session_id="general")
#     chat_display.insert(tk.END, f"Bot: {response}\n\n")
#     chat_display.config(state=tk.DISABLED)
#     chat_display.yview(tk.END)

# send_button = tk.Button(frame, text="Send", command=send)
# send_button.pack(side=tk.LEFT, padx=(5, 10))

# entry.bind("<Return>", lambda event: send())

# root.mainloop()


# from chatbot import Chat, register_call
# import wikipedia
# import warnings
# import tkinter as tk
# from tkinter import scrolledtext
# import os

# warnings.filterwarnings("ignore")
# wikipedia.set_lang("en")  # English Wikipedia

# # Custom Wikipedia call
# @register_call("whoIs")
# def who_is(session, query):
#     try:
#         cleaned = (
#             query.lower()
#             .replace("what is", "")
#             .replace("who is", "")
#             .replace("tell me about", "")
#             .replace("explain", "")
#             .strip()
#         )

#         special_terms = {
#             "python": "Python (programming language)",
#             "java": "Java (programming language)",
#             "apple": "Apple Inc.",
#             "tesla": "Tesla, Inc."
#         }

#         cleaned = special_terms.get(cleaned, cleaned)
#         return wikipedia.summary(cleaned, sentences=2)

#     except wikipedia.exceptions.DisambiguationError as e:
#         return f"Too many meanings. Be specific. E.g. {e.options[:2]}"
#     except wikipedia.exceptions.PageError:
#         return "Topic not found on Wikipedia."
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Path to the template
# template_path = os.path.join(os.path.dirname(__file__), "Example.template")
# chat = Chat(template_path)

# # 🧠 Tkinter UI
# root = tk.Tk()
# root.title("ChatBot with Wikipedia Support")

# chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 14), width=60, height=20)
# chat_display.pack(padx=10, pady=10)
# chat_display.insert(tk.END, "Bot: Hello! How can I help you?\n")
# chat_display.config(state=tk.DISABLED)

# frame = tk.Frame(root)
# frame.pack()

# entry = tk.Entry(frame, font=("Arial", 14), width=40)
# entry.pack(side=tk.LEFT, padx=(10, 5))

# def send():
#     user_input = entry.get()
#     if user_input.strip() == "":
#         return
#     entry.delete(0, tk.END)
#     chat_display.config(state=tk.NORMAL)
#     chat_display.insert(tk.END, f"You: {user_input}\n")
#     response = chat.respond(user_input, session_id="general")
#     chat_display.insert(tk.END, f"Bot: {response}\n\n")
#     chat_display.config(state=tk.DISABLED)
#     chat_display.yview(tk.END)

# send_button = tk.Button(frame, text="Send", command=send)
# send_button.pack(side=tk.LEFT, padx=(5, 10))
# entry.bind("<Return>", lambda event: send())

# root.mainloop()
# from chatbot import Chat, register_call
# import wikipedia
# import re

# @register_call("whoIs")
# def who_is(session, query):
#     try:
#         # Clean the input query
#         query = query.lower()
#         query = re.sub(r"(what is|who is|tell me about|explain)", "", query).strip()

#         # Map common terms to correct Wikipedia titles
#         special_terms = {
#             "ai": "Artificial intelligence",
#             "python": "Python (programming language)",
#             "java": "Java (programming language)",
#             "apple": "Apple Inc.",
#             "tesla": "Tesla, Inc.",
#             "turing": "Alan Turing",
#         }

#         mapped_query = special_terms.get(query, query)

#         # Get Wikipedia summary
#         return wikipedia.summary(mapped_query, sentences=2)

#     except wikipedia.exceptions.DisambiguationError as e:
#         return f"Too many results. Be more specific: {e.options[:2]}"
#     except wikipedia.exceptions.PageError:
#         return "Sorry, that topic was not found on Wikipedia."
#     except Exception as e:
#         return f"Error: {str(e)}"










from chatbot import Chat, register_call
import wikipedia
import tkinter as tk
from tkinter import scrolledtext
import warnings
import re

warnings.filterwarnings("ignore")

# Register Wikipedia-based answers
@register_call("whoIs")
def who_is(session, query):
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
            "elon musk": "Elon Musk"
        }

        mapped_query = special_terms.get(query, query)
        return wikipedia.summary(mapped_query, sentences=2)

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many meanings. Be more specific. E.g. {e.options[:2]}"
    except wikipedia.exceptions.PageError:
        return "Topic not found on Wikipedia."
    except Exception as e:
        return f"Error: {str(e)}"

# Load template
import os
template_path = os.path.join(os.path.dirname(__file__), "Example.template")
chat = Chat(template_path)




# GUI Setup
root = tk.Tk()
root.title("Smart ChatBot")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 14), width=60, height=20)
chat_display.pack(padx=10, pady=10)
chat_display.insert(tk.END, "Bot: Hello! How can I help you?\n")
chat_display.config(state=tk.DISABLED)

entry_frame = tk.Frame(root)
entry_frame.pack()

entry = tk.Entry(entry_frame, font=("Arial", 14), width=40)
entry.pack(side=tk.LEFT, padx=10)

def send():
    user_input = entry.get()
    if not user_input.strip():
        return

    entry.delete(0, tk.END)
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_input}\n")
    response = chat.respond(user_input, session_id="general")
    chat_display.insert(tk.END, f"Bot: {response}\n\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)

send_button = tk.Button(entry_frame, text="Send", command=send)
send_button.pack(side=tk.LEFT)

entry.bind("<Return>", lambda event: send())

root.mainloop()
