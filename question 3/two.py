from scipy.optimize import linprog

# Coefficients of the objective function (negative because linprog minimizes)
c = [-20, -30]

# Coefficients of the inequality constraints
A = [
    [1, 5],  # Wood constraint
    [3, 1]   # Metal constraint
]

# RHS values of the inequality constraints
b = [125, 80]

# Bounds for the decision variables
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extract the optimal solution and profit
optimal_chairs = result.x[0]
optimal_tables = result.x[1]
max_profit = -result.fun  # convert back to maximize

# Print the results
print(f"Optimal number of chairs: {optimal_chairs:.2f}")
print(f"Optimal number of tables: {optimal_tables:.2f}")
print(f"Maximum profit: ${max_profit:.2f}")
