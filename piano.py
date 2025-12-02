import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from fitting_functions import linear_fun, print_equation

def quadratic(x, a, b, c):
    return a * x**2 + b *x + c

raw = np.loadtxt("piano.csv", delimiter = ",", dtype = str)
data = np.char.strip(raw, '"')

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

params, cov = scipy.optimize.curve_fit(quadratic, t, h)

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



# for the cannon ball the quadratic fit worked well because the cannonball did not have air resistance
# so it was close to a perfect curve minus the starting point of how high the cannon started.

# for the piano it wasnt as good and i think it is because of the air resistance. the drag slows it down
# and changes the shape so the curse does not match as nice as the cannon ball.

# the linear fit for x verses time also worked better for the cannonball. It is close to a staight line
# while the piano is not due to the drag slowing it down. 
