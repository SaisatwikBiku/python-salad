#Project Name: Plot Two Points
#Author Name: Sai Satwik Bikumandla
#Date: 24th March, 2023
import matplotlib.pyplot as plt
x_values = []
y_values = []
num1 = int(input("Add X_Coordinate of 1st Point: "))
x_values.append(num1)
num2 = int(input("Add Y_Coordinate of 1st Point: "))
y_values.append(num2)
num1 = int(input("Add X_Coordinate of 2nd Point: "))
x_values.append(num1)
num2 = int(input("Add Y_Coordinate of 2nd Point: "))
y_values.append(num2)
plt.figure()
plt.plot(x_values, y_values, 'bo')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Plotting Two Coordinates')
plt.show()
