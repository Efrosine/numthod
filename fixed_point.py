import numpy as np

def f(x):
    return x**3 - 0.165*x**2 + 3.993*10**(-4) 


def find_gx(f, x):
    """
    Finds the derivative of the function f(x) at x = xo.

    Parameters:
    f (function): The function to find the derivative of.
    xo (float): The value of x to evaluate the derivative at.

    Returns:
    function: The derivative of f(x) at x = xo.
    """
    h = 1e-6
    

    return (f(x+h) - f(x-h)) / (2*h)

dev=find_gx(f, 0)
print(f(0))
print(dev(0))
