def false_position(f, a, b, tol=1e-6, max_iter=100):
    """
    Implements the false position method to find a root of the function f
    between the interval [a, b].

    Parameters:
    f (function): The function to find the root of.
    a (float): The left endpoint of the interval.
    b (float): The right endpoint of the interval.
    tol (float): The tolerance for the root.
    max_iter (int): The maximum number of iterations.

    Returns:
    float: The approximate root of the function.
    """

    # Check if the function has opposite signs at the endpoints
    if f(a) * f(b) >= 0:
        raise ValueError("Function must have opposite signs at the endpoints.")

    # Initialize variables
    c = a
    i = 0

    # Loop until the tolerance is met or the maximum number of iterations is reached
    while abs(f(c)) > tol and i < max_iter:
        # Calculate the new estimate
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        # Check if the new estimate is within the interval
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        # Increment the iteration counter
        i += 1

    # Check if the maximum number of iterations was reached
    if i == max_iter:
        print("Maximum number of iterations reached.")

    return c
