import pyttsx3
import speech_recognition as sr
from textblob import TextBlob

engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You:", text)
            return text
        except:
            return "Sorry, I couldn't understand."

def chatbot_reply(user_input):
    blob = TextBlob(user_input)
    if blob.sentiment.polarity > 0:
        return "You seem happy!"
    elif blob.sentiment.polarity < 0:
        return "Oh no, you sound upset."
    else:
        return "I see."

speak("Hello! I am your chatbot. Say something.")
while True:
    user_input = listen()
    if "bye" in user_input.lower():
        speak("Goodbye!")
        break
    response = chatbot_reply(user_input)
    speak(response)
import pyttsx3
import speech_recognition as sr
from textblob import TextBlob

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You:", text)
            return text
        except:
            return "Sorry, I couldn't understand."

def chatbot_reply(user_input):
    blob = TextBlob(user_input)
    if blob.sentiment.polarity > 0:
        return "You seem happy!"
    elif blob.sentiment.polarity < 0:
        return "Oh no, you sound upset."
    else:
        return "I see."

# Start the voice-based chatbot
speak("Hello! I am your chatbot. Say something.")
while True:
    user_input = listen()
    if "bye" in user_input.lower():
        speak("Goodbye!")
        break
    response = chatbot_reply(user_input)
    speak(response)
