import numpy as np
import sys

def nearest_neighbor(cost_matrix):
    num_cities = len(cost_matrix)
    visited = [False] * num_cities
    tour = []
    
    # Start from city 0
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True
    
    # Repeat until all cities are visited
    while len(tour) < num_cities:
        min_cost = sys.maxsize
        nearest_city = -1
        
        # Find the nearest unvisited city
        for next_city in range(num_cities):
            if not visited[next_city] and cost_matrix[current_city][next_city] < min_cost:
                min_cost = cost_matrix[current_city][next_city]
                nearest_city = next_city
        
        # Visit the nearest unvisited city
        if nearest_city != -1:
            tour.append(nearest_city)
            visited[nearest_city] = True
            current_city = nearest_city
    
    # Return to the starting city
    tour.append(0)
    
    return tour

def calculate_total_distance(tour, cost_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += cost_matrix[tour[i]][tour[i+1]]
    return total_distance

# Example usage
cost_matrix = np.array([[0, 10, 15, 20],
                        [10, 0, 35, 25],
                        [15, 35, 0, 30],
                        [20, 25, 30, 0]])

shortest_route = nearest_neighbor(cost_matrix)
total_distance = calculate_total_distance(shortest_route, cost_matrix)

print("Shortest route:", shortest_route)
print("Total distance:", total_distance)



# Start from an Initial City:

# Choose an arbitrary city as the starting point for the tour.
# Select the Nearest Unvisited City:

# From the current city, find the nearest unvisited city.
# Calculate the distance from the current city to all unvisited cities.
# Select the city with the shortest distance as the next city to visit.
# Update Tour and Mark City as Visited:

# Add the selected city to the tour.
# Mark the selected city as visited.
# Repeat:

# Repeat steps 2 and 3 until all cities are visited.
# Return to Starting City:

# After visiting all cities, return to the starting city to complete the tour.
# Tour Optimization:

# Optionally, after completing the tour, apply local optimization techniques (e.g., 2-opt optimization) to improve the tour's quality further.