import random
import tkinter as tk

num = random.randint(1,100)
guessCount = 0

def check_guess():
    global guessCount
    guess = int(guess_entry.get())
    guessCount += 1

    if guess < num:
        result_label.config(text="Too low!. Try again.")
    elif guess > num:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"Congratulations! you guessed the number in {guessCount} guesses")

root = tk.Tk()
root.title("Guess the Number Game")

instruction_label = tk.Label(root, text="Guess a number between 1 and 100:")
instruction_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
