from scipy.optimize import linprog

# Coefficients of the objective function (negative because linprog minimizes)
c = [-200, -150]

# Coefficients of the inequality constraints
A = [
    [-1, 0],  # Minimum acres of wheat
    [0, -1],  # Minimum acres of barley
    [-20, -10],  # Fertilizer constraint
    [-10, -15]   # Insecticide constraint
]

# RHS values of the inequality constraints
b = [-20, -10, -1200, -600]

# Bounds for the decision variables
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extract the optimal solution and profit
optimal_acres_wheat = result.x[0]
optimal_acres_barley = result.x[1]
max_profit = -result.fun  # convert back to maximize

# Print the results
print(f"Optimal acres of wheat: {optimal_acres_wheat:.2f}")
print(f"Optimal acres of barley: {optimal_acres_barley:.2f}")
print(f"Maximum profit: ${max_profit:.2f}")
