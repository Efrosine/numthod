from bisection_gui import TableBisectionGUI

def bisection(f, a, b, tol=0.001, max_iter=100):
    """
    This function implements the bisection method to find the root of a function f(x) within the interval [a, b].
    
    Parameters:
    f (function): The function whose root is to be found.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    tol (float): The tolerance level for the relative error. Default is 0.001.
    max_iter (int): The maximum number of iterations allowed. Default is 100.
    
    Returns:
    results (list): A list of tuples containing the values of a, b, c, fa, fb, fc, and relative error at each iteration.
    
    Raises:
    ValueError: If f(a) and f(b) have the same sign.
    RuntimeError: If the maximum number of iterations is exceeded.
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    results = []
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        relative_error = abs(b - a) / 2
        results.append((a, b, c, fa, fb, fc, relative_error))
        print(f"xl = {a}, xu = {b}, f(xl) = {fa}, f(xu) = {fb}, xm = {c}, f(xm) = {fc}, error = {relative_error}")
        if abs(relative_error) < tol:
            return results
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    raise RuntimeError("maximum number of iterations exceeded")

def find_a_b(f, x0, dx):
    """
    Given a function f, starting point x0, and step size dx, this function finds a pair of numbers (a, b) such that f(a) * f(b) < 0 and a < b.
    
    Parameters:
    f (function): The function to find the interval for.
    x0 (float): The starting point for the search.
    dx (float): The step size for the search.
    
    Returns:
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    """
    x = x0
    while f(x) * f(x + dx) > 0:
        x += dx
    return x, x + dx

# Example:
#  f(x) = x**3 - 2*x - 5

"""
This function takes user input for a function in terms of x and uses the bisection method to find its root.
# """
str = input("Enter the function in terms of x: ")
g = eval("lambda x: " + str)

# def f(x):
#     return x**3 - 0.165*x**2 + 3.993*10**(-4) 

a, b = find_a_b(g, 0, 0.01)
results = bisection(g, a, b)

table_data = []
for xl, xu, xm, fa, fb, fc, error in results:
    table_data.append((xl, xu, fa, fb, xm, fc, error))
gui = TableBisectionGUI(table_data)
gui.run()