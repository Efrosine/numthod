def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Implements the Newton-Raphson method for finding the root of a function f(x).
    
    Parameters:
    f (function): The function to find the root of.
    df (function): The derivative of the function f(x).
    x0 (float): The initial guess for the root.
    tol (float): The tolerance for the root. Default is 1e-6.
    max_iter (int): The maximum number of iterations. Default is 100.
    
    Returns:
    float: The root of the function f(x).
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            break
        x = x - fx/dfx
    return x
