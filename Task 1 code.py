# Simple Rule-Based Chatbot in Python
# Written for learning purpose (Task 1)
# This bot just replies with fixed answers using if-else.
# It’s not smart like ChatGPT, but it works :)

def reply(user_text):
    # make it lowercase so matching is easy
    text = user_text.lower()

    # greetings
    if "hello" in text or "hi" in text:
        return "Hey there! 👋 How can I help you?"

    # small talk
    elif "how are you" in text:
        return "I'm fine, thanks! (well, I'm just some code 😅). What about you?"

    # asking for name
    elif "your name" in text:
        return "I'm just a simple Python chatbot, not a real human."

    # asking for help
    elif "help" in text:
        return "Sure! You can ask me about greetings, my name, or just say bye."

    # goodbye
    elif "bye" in text or "exit" in text:
        return "Goodbye! Take care 👋"

    # unknown inputs
    else:
        return "Hmm... I don’t understand that. Can you try saying something else?"


# main program loop
print("Chatbot: Hi, I'm your assistant. Type 'bye' to quit.")

while True:
    user = input("You: ")
    ans = reply(user)
    print("Chatbot:", ans)

    # stop if user says bye or exit
    if "bye" in user.lower() or "exit" in user.lower():
        break
