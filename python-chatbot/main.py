#!/usr/bin/env python3
"""
Main script to run the Python Chatbot
"""

from src.chatbot import Chatbot
import sys

def main():
    print("🤖 Welcome to Python Chatbot!")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("-" * 50)
    
    # Initialize the chatbot
    chatbot = Chatbot()
    
    # Simple conversation loop
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chatbot: Goodbye! Have a great day! 👋")
                break
            
            # Skip empty input
            if not user_input:
                continue
            
            # Get response from chatbot
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")
            
        except KeyboardInterrupt:
            print("\nChatbot: Goodbye! Have a great day! 👋")
            break
        except Exception as e:
            print(f"Chatbot: Sorry, I encountered an error: {e}")

if __name__ == "__main__":
    main() 