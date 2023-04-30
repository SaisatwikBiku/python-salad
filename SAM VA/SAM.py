import os #MacOS Only
import tkinter as tk
import time as tp
import random

def greet():
    name = name_entry.get()
    welcome = f"say Hello {name} ! I am Sam your Virtual Assistant. I am now ready to Assist you. Feel free to enter a command." # System Voice : Siri(India)
    os.system(welcome)

def number_input():
    number = number_entry.get()
    timer_cmd = f"open -u https://www.bigtimer.net/?minutes={number}&repeat=false&target=1682701685557"
    os.system(timer_cmd)
    os.system(f"say Timer is set for {number} minutes. Press Start to continue")

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
    elif command == "open whatsapp" or command == "whatsapp" or command == "sam open whatsapp":   
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
    elif command == "open youtube" or command == "youtube" or command == "yt"  or command == "sam open youtube" :
        os.system("say Opening Youtube")
        os.system("open -u https://www.youtube.com/")
    elif command == "set timer" or command == "timer" :
        os.system("say Sure. Input the number of minutes to set the timer in the Number Input Box.")
    elif command == "generate QR code" or command == "generate qr code" or command == "qr" or command == "generate qr" or command == "qr code":
        os.system("say Okay. Opening QR maker")
        os.system("python QRG_GUI.py")
    elif command == "generate a strong password" or command == "generate password" or command == "new password" or command == "password" :
        os.system("say Okay. Opening Password Generator")
        os.system("python PassGen.py")
    elif command == "let us play a game" or command == "game" or command == "play a game" or command == "play with me" :
        os.system("say Okay. Opening a Game")
        os.system("python Game.py")
    else:
        os.system("say I did not get you master. But I can search for the same on web for you")
        for i in command :
            if i == " ":
                command = command.replace(" ", "+")
        os.system(f"open -u https://www.google.com/search?q={command}")



root = tk.Tk()
root.title("Sam Virtual Assistant")

name_label = tk.Label(root, text="Enter your name:")
name_entry = tk.Entry(root)
greet_button = tk.Button(root, text="Greet", command=greet)

command_label = tk.Label(root, text="Enter your command:")
command_entry = tk.Entry(root)
execute_button = tk.Button(root, text="Execute", command=execute_command)

number_label = tk.Label(root, text="Number input:")
number_entry = tk.Entry(root)
number_button = tk.Button(root, text="Input", command=number_input)

name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry.grid(row=0, column=1, padx=5, pady=5)
greet_button.grid(row=0, column=2, padx=5, pady=5)

command_label.grid(row=1, column=0, padx=5, pady=5)
command_entry.grid(row=1, column=1, padx=5, pady=5)
execute_button.grid(row=1, column=2, padx=5, pady=5)

number_label.grid(row=2, column=0, padx=5, pady=5)
number_entry.grid(row=2, column=1, padx=5, pady=5)
number_button.grid(row=2, column=2, padx=5, pady=5)



root.mainloop()
