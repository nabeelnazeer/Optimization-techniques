from scipy.optimize import linprog

# Coefficients of the objective function (negative because linprog minimizes)
c = [-3, -2]

# Coefficients of the inequality constraints
A = [
    [2, 1],   # Budget constraint
    [1, 1],   # Production constraint
    [-1, 0],  # Minimum chocolate cakes
    [0, -1]   # Minimum vanilla cakes
]

# RHS values of the inequality constraints
b = [500, 400, -100, -50]

# Bounds for the decision variables
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extract the optimal solution and revenue
optimal_chocolate_cakes = result.x[0]
optimal_vanilla_cakes = result.x[1]
max_revenue = -result.fun  # convert back to maximize

# Print the results
print(f"Optimal number of chocolate cakes: {optimal_chocolate_cakes:.2f}")
print(f"Optimal number of vanilla cakes: {optimal_vanilla_cakes:.2f}")
print(f"Maximum revenue: ${max_revenue:.2f}")
