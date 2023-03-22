#Project Name: Password Generator
#Author Name: Sai Satwik Bikumandla
#Date: 22nd March, 2023

import random
import string

def generatePassword(length, custom):

    character = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(character, length)) + custom
    return password

length = int(input("Enter length of your desired Password: "))
custom = input("Enter your custom character to be included in your Password: ")

password = generatePassword(length, custom)
print("Generated Password:", password)