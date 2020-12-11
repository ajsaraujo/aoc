import sys

file_name = sys.argv[1]

def count_paths(adapter_set, current_adapter, paths_to):
	if current_adapter not in adapter_set:
		return 0

	if current_adapter not in paths_to:
		result = 0

		for i in range(1, 4):
			result += count_paths(adapter_set, current_adapter - i, paths_to)
		
		paths_to[current_adapter] = result

	return paths_to[current_adapter]

with open(file_name, 'r') as file:
	adapters = sorted([int(line) for line in file.readlines()])

	adapter_set = { adapter for adapter in adapters }
	adapter_set.add(0)

	last_adapter = adapters[-1] 
	paths_to = { 0: 1 }

	print(count_paths(adapter_set, last_adapter, paths_to))

