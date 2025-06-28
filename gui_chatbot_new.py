import tkinter as tk
from chatbot import get_response

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    response = get_response(user_input)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")
    with open("chat_log.txt", "a", encoding="utf-8") as log:
        log.write(f"You: {user_input}\nBot: {response}\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI Chatbot")

chat_log = tk.Text(root, height=20, width=60)
chat_log.pack()

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10)
tk.Button(root, text="Send", command=send_message).pack(side=tk.LEFT)

root.mainloop()
