from scipy.optimize import linprog

# Coefficients of the objective function (since linprog minimizes)
c = [-2, -3, -1]

# Coefficients of the inequality constraints
A = [
    [1, 1, 1],    # Coefficients for u1 + u2 + u3 <= 4
    [-1, -2, 1]   # Coefficients for -u1 - 2u2 + u3 <= -2 (Note: multiplied by -1 to convert to standard form)
]

# RHS values of the inequality constraints
b = [4, -2]

# Bounds for the decision variables
u_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[u_bounds, u_bounds, u_bounds], method='highs')

# Extract the optimal solution and maximum value of p
optimal_u = result.x
max_p = -result.fun  # convert back to maximize

# Print the results
print(f"Optimal values of u: {optimal_u}")
print(f"Maximum value of p: {max_p}")
