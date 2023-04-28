import os #MacOS Only
import tkinter as tk
import time as tp
import random

def greet():
    name = name_entry.get()
    welcome = f"say Hello {name} ! I am Sam your Virtual Assistant." # System Voice : Samantha
    os.system(welcome)

def execute_command():
    command = command_entry.get().lower()
    if command == "hi":
        greetings = f"say hey there, {name_entry.get()} ! How can I help you?"
        os.system(greetings)
    elif command == "how are you?":
        os.system("say I am good master.")
    elif command == "what is the time?" or command == "time" or command == "what is time?" or command == "what is time":
        hours = tp.strftime("%H")
        minutes = tp.strftime("%M")
        time = f"say the time is {hours}  {minutes} "
        os.system(time)
    elif command == "i love you" or command == "let us marry" or command == "do you have feelings?" :
        os.system("say Sorry, I am busy with the job as the Assistant. I do not have time for this.")
    elif command == "open google" or command == "google.com" or command == "google":
        os.system("say Opening Google Search Engine.")
        os.system("open -u https://www.google.com/")
    elif command == "open whatsapp" or command == "whatsapp" or command == "chitti open whatsapp":   
        os.system("say Opening WhatsApp.")
        os.system("open -u https://web.whatsapp.com/")
    elif command == "tell me a joke" or command == "tell a joke" or command == "joke" :
        choice = random.randint(0, 9)
        match choice :
            case 0 :
                os.system("say Why don't scientists trust atoms? Because they make up everything! hahaha")   
            case 1 :
                os.system("say Why did the banana go to the doctor? Because it wasn't peeling well... hahaha")
            case 2 :
                os.system("say What did the ocean say to the beach? Nothing, it just waved.")
            case 3 :
                os.system("say Why do seagulls fly over the ocean? Because if they flew over the bay, we’d call them bagels.")
            case 4 :
                os.system("say What do you give a sick lemon? A Lemon-aid") 
            case 5 :
                os.system("say Can a kangaroo jump higher than the Empire State Building? Of course! Buildings can’t jump!")   
            case 6 :
                os.system("say Why did maths book look so worried? Because it has too many problems.... hahaha.")
            case 7 :
                os.system("say Why did Severus Snape stand in the middle of the road? So you’d never know which side he was on.")
            case 8 :
                os.system("say What do you call a bear with no teeth? A gummy bear.")
            case 9 :
                os.system("say How do you increase attendance percentage of students? By making everyday as Traditional Day")        
    elif command == "what is weather here?" or command == "weather" :
        os.system("say Showing Weather.")
        os.system("open -u https://www.accuweather.com/en/in/hyderabad/202190/weather-forecast/202190")
    else:
        os.system("say I did not get you master. Give a valid command.")


root = tk.Tk()
root.title("Sam Virtual Assistant")

name_label = tk.Label(root, text="Enter your name:")
name_entry = tk.Entry(root)
greet_button = tk.Button(root, text="Greet", command=greet)

command_label = tk.Label(root, text="Enter your command:")
command_entry = tk.Entry(root)
execute_button = tk.Button(root, text="Execute", command=execute_command)

name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry.grid(row=0, column=1, padx=5, pady=5)
greet_button.grid(row=0, column=2, padx=5, pady=5)

command_label.grid(row=1, column=0, padx=5, pady=5)
command_entry.grid(row=1, column=1, padx=5, pady=5)
execute_button.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
