# task: Geocacher wanted to go geocaching. He wanted to visit 7 caches and get back home so that he visits each cache just once and total disntace is as short as possible.

import itertools
import numpy as np

# Distance matrix
distance_matrix = np.array([
    [0, 52, 63, 58, 58, 58, 56, 86],
    [52, 0, 46, 55, 45, 26, 11, 74],
    [63, 46, 0, 54, 26, 45, 53, 81],
    [58, 55, 54, 0, 58, 22, 55, 77],
    [58, 45, 26, 58, 0, 40, 80, 81],
    [58, 26, 45, 22, 40, 0, 40, 12],
    [56, 11, 53, 55, 80, 40, 0, 80],
    [86, 74, 81, 77, 81, 12, 80, 0]
])

# Number of locations (nodes)
num_locations = distance_matrix.shape[0]

start_node = 0

# Generate all possible paths starting and ending at the start node
nodes = list(range(1, num_locations))
all_possible_paths = [(start_node, *perm, start_node) for perm in itertools.permutations(nodes)]

# Calculate the total distance for each path
shortest_path = None
shortest_distance = float('inf')

for path in all_possible_paths:
    # Calculate the distance for the current path
    distance = sum(distance_matrix[path[i], path[i+1]] for i in range(len(path) - 1))
    if distance < shortest_distance:
        shortest_distance = distance
        shortest_path = path

path_distances = []


for i in range(len(shortest_path) - 1):
    start = shortest_path[i]
    end = shortest_path[i + 1]
    distance = distance_matrix[start, end]
    path_distances.append((start, end, distance))  
print(path_distances, shortest_distance)



