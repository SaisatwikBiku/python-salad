#Project Name: Chat Bot
#Author Name: Sai Satwik Bikumandla
#Date: 23rd March, 2023

import time

print("Welcome to Chatbot Oggy")
print("Your conversation has started!")

def chat(message):

    match message:

        case "hi":
            print("Oggy: Hello! Nice to meet you.")

        case "what is your name?":
            print("Oggy: My name is Oggy.")

        case "who created you?":
            print("Oggy: Sai Satwik Bikumandla coded me.")

        case "nice to meet you oggy":
            print("Oggy: It's my pleasure to meet you.")

        case "what is the time?":
            print("Oggy: The time is", time.strftime("%H:%M:%S"))

        case _:
            print("Oggy: Sorry! I do not understand what you are saying.")

while True:

    message = input("You: ")
    
    if message == "quit":
        break
    else:
        chat(message)
        





