import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit
from fitting_functions import linear_fun, print_equation

def quadratic(x, a, b, c):
    return a * x**2 + b *x + c

data = np.loadtxt("cannon.csv", delimiter = ",", dtype = str)
print("first row: ", data[0])

t = data[1:, 0].astype(np.float32)
x = data[1:, 1].astype(np.float32)
h = data[1:, 2].astype(np.float32)

print("t =", t)
print("x =", x)
print("h =", h)

params, params_cov = scipy.optimize.curve_fit(linear_fun, t, x)

m = params[0]
b = params[1]

print_equation(m, b, "m", "s")

t_fit = np.linspace(min(t), max(t), 200)
x_fit = linear_fun(t_fit, m, b)

plt.figure()
plt.scatter(t, x)
plt.plot(t_fit, x_fit)
plt.legend()
plt.xlabel("time (s)")
plt.ylabel("range (m)")
plt.show()

# Exercise 1

params, params_cov = scipy.optimize.curve_fit(quadratic, t, h)

a = params[0]
b2 = params[1]
c = params[2]

h_fit = quadratic(t_fit, a, b2, c)

plt.figure()
plt.scatter(t, h)
plt.plot(t_fit, h_fit)
plt.xlabel("time (s)")
plt.ylabel("height (m)")
plt.show()
