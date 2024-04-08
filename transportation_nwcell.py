# Transportation problem - northwest corner cell method using user inpuut

import numpy as np

def northwest_corner_cell(supply, demand):
  solution = np.zeros((len(supply), len(demand)))

  current_supply = supply.copy()
  current_demand = demand.copy()

  for i in range(len(supply)):
    for j in range(len(demand)):
      allocation = min(current_supply[i], current_demand[j])

      solution[i][j] = allocation
      current_supply[i] -= allocation
      current_demand[j] -= allocation

      if current_demand[j] == 0:
        break

  return solution

supply = list(map(int, input("Enter the supply for each source (separated by spaces): ").split()))
demand = list(map(int, input("Enter the demand for each destination (separated by spaces): ").split()))

solution = northwest_corner_cell(supply, demand)

print("\nInitial Solution:")
print(solution)


# The Northwest Corner Method is a heuristic algorithm used for finding an initial feasible solution to transportation problems. It's named as such because it starts allocating resources from the northwest corner of the transportation matrix and fills as much as possible until the demand and supply constraints are satisfied. Here's the algorithm:

# Northwest Corner Method Algorithm:
# Initialize: Start from the northwest corner (top-left cell) of the transportation matrix.

# Allocate: Allocate units from the supply at the northwest corner to the demand at the top until either the supply or the demand is fully satisfied.

# Update: After allocating, update the supply and demand accordingly:

# Subtract the allocated amount from the supply of the row.
# Subtract the allocated amount from the demand of the column.
# Move: Move to the next cell to the right (to the east) if the supply is exhausted or move down (to the south) if the demand is satisfied. If both supply and demand are satisfied, move diagonally to the southeast.

# Repeat: Repeat steps 2-4 until all supply and demand are satisfied.

# Termination: Terminate when all supply and demand are satisfied.