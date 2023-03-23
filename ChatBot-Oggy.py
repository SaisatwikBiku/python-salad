#Project Name: Chat Bot
#Author Name: Sai Satwik Bikumandla
#Date: 23rd March, 2023

import time
import tkinter as tk

class Chatbot:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chatbot Oggy")

        self.messages = tk.Text(self.window)
        self.messages.pack(fill="both", expand=True)

        self.input_frame = tk.Frame(self.window)
        self.input_field = tk.Entry(self.input_frame)
        self.input_field.pack(side=tk.LEFT, fill="both", expand=True)
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)
        self.input_frame.pack(fill="both")

        self.messages.insert(tk.END, "Welcome to Chatbot Oggy\nYour conversation has started!\n\n")

        self.input_field.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        message = self.input_field.get()
        self.input_field.delete(0, tk.END)
        self.messages.insert(tk.END, "You: " + message + "\n")
        self.chat(message)

    def chat(self, message):
        match message:
            case "hi":
                self.messages.insert(tk.END, "Oggy: Hello! Nice to meet you.\n")
            case "how are you?":
                self.messages.insert(tk.END, "Oggy: I am doing great so far. Thank you for asking!")    
            case "thank you":
                self.messages.insert(tk.END, "Oggy: You're welcome.")    
            case "what is your name?":
                self.messages.insert(tk.END, "Oggy: My name is Oggy.\n")
            case "who created you?":
                self.messages.insert(tk.END, "Oggy: Sai Satwik Bikumandla coded me.\n")
            case "nice to meet you oggy":
                self.messages.insert(tk.END, "Oggy: It's my pleasure to meet you.\n")
            case "what is the time?":
                self.messages.insert(tk.END, "Oggy: The time is " + time.strftime("%H:%M:%S") + "\n")
            case _:
                self.messages.insert(tk.END, "Oggy: Sorry! I do not understand what you are saying.\n")

chatbot = Chatbot()
chatbot.window.mainloop()





