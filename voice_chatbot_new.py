import speech_recognition as sr
import pyttsx3
from chatbot import get_response

recognizer = sr.Recognizer()
engine = pyttsx3.init()

print("🎤 Voice Chatbot Started. Speak into the mic...")

while True:
    with sr.Microphone() as source:
        print("You (speaking): ", end="")
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            print(user_input)
            response = get_response(user_input)
            print("Bot:", response)
            engine.say(response)
            engine.runAndWait()
            with open("chat_log.txt", "a", encoding="utf-8") as log:
                log.write(f"You: {user_input}\nBot: {response}\n\n")
        except Exception as e:
            print("⚠️ Sorry, I didn't get that. Error:", e)
