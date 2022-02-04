import numpy as np
import matplotlib.pyplot as plt

a = 10
b = 5
c = 2

def menu():
    print("Menu de funciones posibles".center(40, "-"))
    print("1- sin")
    print("2- cos")
    print("3- tan")
    print("4- exp")
    print("5- log")
    print("6- linear")
    print("7- quadratic")
    funcion = int(input("Digite la función a visualizar:"))
    return funcion

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
        plt.title("Función seno")
    elif function == 2:
        plt.plot(x, cos(x))
        plt.title("Función coseno")
    elif function == 3:
        plt.plot(x, tan(x))
        plt.title("Función tangente")
    elif function == 4:
        plt.plot(x, exp(x))
        plt.title("Función exponencial")
    elif function == 5:
        plt.plot(x, log(x))
        plt.title("Función logarítmica")
    elif function == 6:
        plt.plot(x, linear(a, b, x))
        plt.title("Función lineal")
    elif function == 7:
        plt.plot(x, quadratic(x, a, b, c))
        plt.title("Función cuadrática")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

try:
    inicio = int(input("Ingrese primer valor de X: "))
    fin = int(input("Ingrese ultimo valor de X: "))
    while fin <= inicio:
        print(f"Rango no valido, debe ingresar un numero mayor que {inicio}")
        fin = int(input("Ingrese ultimo valor de X: "))
except Exception as e:
    print(f"Error: {e}")

x = np.linspace(inicio, fin, 1000)

function = menu()
plot_function(function)