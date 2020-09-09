'''
Plots the function and its fourier series for different upper limit of n (Nmax)

f(x) ~ a0 + sum(n=1, Nmax)(an*cos(n*pi*x/L) + bn*sin(n*pi*x/L))

Need to:
    specify f(x) in function(x)
    define an in an(n)
    define bn in bn(n)
    define a0 (scalar)
    provide lower limit (x_lower), upper limit (x_upper), maximum n for the sum (Nmax)
    string describing the function f(x) (function_string) for nice plotting
    number of evaluation points (points)

'''

from numpy import cos, sin, pi, linspace
import matplotlib.pyplot as plt


def fourier_series(x, a0, Nmax):
    value = a0

    for n in range(1, Nmax):
        value += an(n)*cos(n*pi*x/L) + bn(n)*sin(n*pi*x/L)
    
    return value


### EXAMPLE ###

def function(x):
    return x**2

def an(n):
    return (-1)**n * 4/(pi*n)**2

def bn(n):
    return 0

x_lower = -1
x_upper = 1
L = 1
a0 = 1/3
Nmax = 5
function_string = "$x^2$"
points = 51

x_list = linspace(x_lower, x_upper, points)
fourier_series_list = fourier_series(x_list, a0, Nmax)
function_list = function(x_list)


plt.plot(x_list, function_list, label=function_string)
plt.plot(x_list, fourier_series_list, label="Fourier series")
plt.legend()
plt.show()