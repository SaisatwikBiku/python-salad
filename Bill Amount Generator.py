#Project Name: Bill Amount Generator
#Author Name: Sai Satwik Bikumandla
#Date: 22nd March, 2023
'''A restaurant gives a discount of 10% if the total customer bill including
5% tax is greater than or equal to Rs. 1000.'''

print("===============Welcome to Dominos Pizza==============")
print("-----------------------------------------------------")
print("Menu for you-")
print("1)\tCorn n Cheese Pizza \t279 Rs")
print("2)\tPaneer Paratha Pizza\t299 Rs")
print("3)\tMargherita          \t329 Rs")
print("4)\tFarmhouse           \t459 Rs")
print("-----------------------------------------------------")

cart = []
total_bill = 0

while len(cart) < 4:
    opt = input("Please select a pizza of your choice (1/2/3/4): ")
    if opt in ['1', '2', '3', '4']:
        pizza_price = [279, 299, 329, 459][int(opt)-1]
        total_bill += pizza_price
        cart.append(pizza_price)
    else:
        print("Please enter a valid option from the menu")
        continue
    
    choice = input("Do you want to add another pizza to your cart? (Yes-1;No-0): ")
    if choice == '0':
        break

tax = total_bill * 0.05
amount = total_bill + tax

if amount >= 1000:
    payable_amount = amount * 0.9
    print("\nCongrats! You are eligible for a 10% discount.\n")
else:
    payable_amount = amount

print(f"Total bill: {total_bill} Rs")
print(f"Tax: {tax:.2f} Rs")
print(f"Payable amount: {payable_amount:.2f} Rs")
print("-----------------------------------------------------")




