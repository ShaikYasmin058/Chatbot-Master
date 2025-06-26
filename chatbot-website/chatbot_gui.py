from chatbot import Chat
import tkinter as tk
from tkinter import scrolledtext
import os

# ✅ Use existing template
chat = Chat("examples/Example.template")

# GUI setup
root = tk.Tk()
root.title("ChatBot UI")

# Chat display area
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 14), width=60, height=20)
chat_display.pack(padx=10, pady=10)
chat_display.insert(tk.END, "Bot: Hello! How can I help you?\n")
chat_display.config(state=tk.DISABLED)

# Input + Send button
frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame, font=("Arial", 14), width=40)
entry.pack(side=tk.LEFT, padx=(10, 5))

def send():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    entry.delete(0, tk.END)
    
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_input}\n")
    response = chat.respond(user_input, session_id="chat_ui")
    chat_display.insert(tk.END, f"Bot: {response}\n\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)

send_button = tk.Button(frame, text="Send", command=send)
send_button.pack(side=tk.LEFT, padx=(5, 10))

entry.bind("<Return>", lambda event: send())

root.mainloop()
