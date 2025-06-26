from chatbot import Chat, register_call
import wikipedia
import os
import warnings

warnings.filterwarnings("ignore")

@register_call("whoIs")
def who_is(session, query):
    try:
        cleaned = (
            query.lower()
            .replace("what is", "")
            .replace("who is", "")
            .replace("tell me about", "")
            .replace("explain", "")
            .strip()
        )

        special_terms = {
            "python": "Python (programming language)",
            "java": "Java (programming language)",
            "apple": "Apple Inc.",
            "tesla": "Tesla, Inc."
        }

        cleaned = special_terms.get(cleaned, cleaned)
        return wikipedia.summary(cleaned, sentences=2)

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many meanings. Try to be specific. E.g. {e.options[:2]}"
    except wikipedia.exceptions.PageError:
        return "Topic not found on Wikipedia."
    except Exception as e:
        return f"Error: {str(e)}"

# Skip templates
chat = Chat()
# chat = Chat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "examples", "Example.template"))
# chat = Chat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Example.template"))


# Start manual conversation loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Goodbye!")
        break
    print("Bot:", chat.respond(user_input, session_id="general"))




from chatbot import Chat, register_call
import wikipedia
import warnings
warnings.filterwarnings("ignore")

wikipedia.set_lang("he")  # or "en" for English

@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return f"לא מצאתי מידע על {query}"

# Use TEMPLATE MODE
chat = Chat("Chatbot-master/examples/Example.template")


chat.converse("שלום, איך אפשר לעזור?")
