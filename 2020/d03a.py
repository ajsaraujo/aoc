import sys

def read_grid(file_path):
    with open(file_path) as file:
        return [line[:-1] for line in file]

def count_trees_in_path(grid):
    j = 0
    grid_width = len(grid[0])
    tree_count = 0

    for i in range(1, len(grid)):
        j = (j + 3) % grid_width

        if grid[i][j] == '#':
            tree_count += 1
    
    return tree_count

input_file = sys.argv[1]
grid = read_grid(input_file)
num_of_trees = count_trees_in_path(grid)
print(num_of_trees)