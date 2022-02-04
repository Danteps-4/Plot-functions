import numpy as np
import matplotlib.pyplot as plt

a = 10
b = 5
c = 2

def menu():
    print("Functions menu".center(40, "-"))
    print("1- sin")
    print("2- cos")
    print("3- tan")
    print("4- exp")
    print("5- log")
    print("6- linear")
    print("7- quadratic")
    function = int(input("Enter the number of the function:"))
    return function

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

def tan(x):
    return np.tan(x)

def exp(x):
    return np.exp(x)

def log(x):
    return np.log(x)

def linear(x, a, b):
    return a*x + b

def quadratic(x, a, b ,c):
    return a*x**2 + b*x + c

def plot_function(function):
    if function == 1:
        plt.plot(x, sin(x))
        plt.title("Sine function")
    elif function == 2:
        plt.plot(x, cos(x))
        plt.title("Cosine function")
    elif function == 3:
        plt.plot(x, tan(x))
        plt.title("Tangent function")
    elif function == 4:
        plt.plot(x, exp(x))
        plt.title("Exponential function")
    elif function == 5:
        plt.plot(x, log(x))
        plt.title("Logarithmic function")
    elif function == 6:
        plt.plot(x, linear(a, b, x))
        plt.title("Linear function")
    elif function == 7:
        plt.plot(x, quadratic(x, a, b, c))
        plt.title("Quadratic function")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

try:
    first = int(input("Enter the first value of x: "))
    last = int(input("Enter the last value of x: "))
    while last <= first:
        print(f"Invalid value, must enter a value greater than {first}")
        last = int(input("Enter the last value of x: "))
except Exception as e:
    print(f"Error: {e}")

x = np.linspace(first, last, 1000)

function = menu()
plot_function(function)