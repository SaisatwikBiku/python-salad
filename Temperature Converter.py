#Project Name: Temperature Converter
#Author Name: Sai Satwik Bikumandla
#Date: 26th March, 2023

temp = float(input("Enter the temperature: "))
unit = input("Is the temperature in Celsius or Fahrenheit? ")

if unit.lower() == "celsius":
    fahrenheit = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit:.2f}")
elif unit.lower() == "fahrenheit":
    celsius = (temp - 32) * 5/9
    print(f"The temperature in Celsius is {celsius:.2f}")
else:
    print("Invalid input. Please enter either 'Celsius' or 'Fahrenheit'.")
