#Project Name: Guess the Number
#Author Name: Sai Satwik Bikumandla
#Date: 26th March, 2023

import random
num = random.randint(1,100)
guessCount = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    guessCount += 1

    if guess < num :
        print("Too low!. Try again.")
    elif guess > num :
        print("Too high! Try again.")
    else:
        print(f"Congratulations! you guessed the number in {guessCount} guesses")      
        break  



