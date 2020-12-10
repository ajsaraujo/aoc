import sys

file_name = sys.argv[1]

def get_diffs(adapters):
	current_voltage = 0

	diff_count = [0, 0, 0, 0]

	for i in range(len(adapters)):
		adapter_voltage = adapters[i]

		diff = adapter_voltage - current_voltage
		if diff > 3:
			break

		diff_count[diff] += 1

		current_voltage = adapter_voltage

	return diff_count

with open(file_name, 'r') as file:
	adapters = sorted([int(line) for line in file.readlines()])
	adapters.append(adapters[-1] + 3)
	diff_count = get_diffs(adapters)

	print(f'{diff_count[1]} x {diff_count[3]} = {diff_count[1] * diff_count[3]}')
