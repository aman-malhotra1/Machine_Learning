# Find the gradient descent of function -> x^3-3X^2+7
import numpy as np
import matplotlib.pyplot as plt

function = lambda x:(x**3) - (3*x**2) +7
x = np.linspace(-1,3,500)
plt.plot(x ,function(x))
plt.show()

def calculate_derivative(x):
    return (3*(x**2)) - (6*x)

def calculate_gradient(current_x, precision, learning_rate, previous_x):
    x_list , y_list = [current_x] ,[function(current_x)]
    while np.abs(previous_x - current_x) > precision:
        previous_x = current_x
        derivative_x = calculate_derivative(previous_x)
        current_x = previous_x - (learning_rate * derivative_x)
        x_list.append(current_x)
        y_list.append(function(current_x))
    print("Total No. of Iteration :",len(x_list))
    print("Local minimum value of x ",current_x)
    plt.plot(x,function(x))
    plt.scatter(x_list, y_list, color ='red')
    plt.show()

current_x = 0.5
precision = 0.00001
learning_rate = 0.05
previous_x = 0
calculate_gradient(current_x,precision,learning_rate, previous_x)
