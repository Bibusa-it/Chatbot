import random
import re

class Chatbot:
    def __init__(self):
        self.model = None
        self.data = None
        self.responses = {
            'greeting': [
                "Hello! I'm your AI assistant. How are you?",
                "Hi there! Nice to meet you!",
                "Good day! What can I do for you?"
            ],
            'farewell': [
                "Goodbye! Have a wonderful day!",
                "See you later! Take care!",
                "Bye! It was nice chatting with you!",
                "Farewell! Come back anytime!"
            ]
        }

if __name__ == "__main__":
    bot = Chatbot()
    print("Chatbot initialized. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        # Respond to greetings
        if any(greet in user_input.lower() for greet in ['hello', 'hi', 'hey']):
            print("Bot:", random.choice(bot.responses['greeting']))
        # Respond to farewells
        elif any(bye in user_input.lower() for bye in ['bye', 'goodbye', 'see you']):
            print("Bot:", random.choice(bot.responses['farewell']))
        else:
            print("Bot: I'm not sure how to respond to that.")