import sys
import operator
from functools import reduce

def read_grid(file_path):
    with open(file_path) as file:
        return [line[:-1] for line in file]

def traverse_map(grid, x_speed, y_speed):
    j = 0
    grid_width = len(grid[0])
    tree_count = 0

    for i in range(y_speed, len(grid), y_speed):
        j = (j + x_speed) % grid_width

        if grid[i][j] == '#':
            tree_count += 1
    
    return tree_count

def count_trees_in_paths(grid):
    strategies = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    tree_counts = [traverse_map(grid, x_speed, y_speed) for [x_speed, y_speed] in strategies]
    
    return reduce(lambda a,b : a * b, tree_counts)

input_file = sys.argv[1]
grid = read_grid(input_file)
num_of_trees = count_trees_in_paths(grid)
print(num_of_trees)