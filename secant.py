def secant(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Find a root of the function f using the secant method.

    Parameters:
    f (function): The function to find the root of.
    x0 (float): The first initial guess.
    x1 (float): The second initial guess.
    tol (float): The tolerance for the root. Defaults to 1e-6.
    max_iter (int): The maximum number of iterations. Defaults to 100.

    Returns:
    float: The root of the function f.
    """
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    raise ValueError("The method failed to converge.")
