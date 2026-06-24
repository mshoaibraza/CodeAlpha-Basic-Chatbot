# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hi" or user_input == "hello":
        return "Hello! How can I help you today?"

    elif user_input == "how are you":
        return "I'm fine, thanks for asking!"

    elif user_input == "what is your name":
        return "I am a simple Python chatbot."

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that."

# Main Program
print("=== Simple Rule-Based Chatbot ===")
print("Type 'bye' to exit the chat.\n")

while True:
    user_message = input("You: ")

    response = chatbot_response(user_message)
    print("Bot:", response)

    if user_message.lower() == "bye":
        break