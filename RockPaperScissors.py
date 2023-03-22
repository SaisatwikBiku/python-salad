#Project Name: Rock Paper Scissors
#Author Name: Sai Satwik Bikumandla
#Date: 23rd March, 2023

import tkinter as tk
import random

#creating main window for the GUI
window = tk.Tk()
window.title("RockPaperScissors")

def playGame(playerChoice):

    computerChoice = random.choice(["Rock", "Paper", "Scissors"])
    if playerChoice == computerChoice :
        result = "Tie!"
    elif (playerChoice == "Rock" and computerChoice == "Scissors") or (playerChoice == "Paper" and computerChoice == "Rock") or (playerChoice == "Scissors" and computerChoice == "Paper") :
        result = "You won!"
    else:
        result = "You lost!"
    resultLabel.config(text=f"You chose {playerChoice}\nComputer chose {computerChoice}\n{result}")      

rockButton = tk.Button(window, text = "Rock", width = 10, command = lambda: playGame("Rock"))      
paperButton = tk.Button(window, text = "Paper", width = 10, command = lambda: playGame("Paper"))
scissorsButton = tk.Button(window, text = "Scissors", width = 10, command = lambda: playGame("Scissors"))   
resultLabel = tk.Label(window, text="Choose your move")

rockButton.pack(pady = 5)
paperButton.pack(pady = 5)
scissorsButton.pack(pady = 5)
resultLabel.pack(pady = 5)

window.mainloop()