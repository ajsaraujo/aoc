import sys

file_name = sys.argv[1]

def is_valid(index, numbers, preamble_size):
	range_beginning = index - preamble_size
	range_end = index

	candidate = numbers[index]

	for i in range(range_beginning, range_end):
		for j in range(i + 1, range_end):
			if numbers[i] + numbers[j] == candidate:
				if numbers[i] != numbers[j]:
					return True
	
	return False

with open(file_name, 'r') as file:
	numbers = [int(num) for num in file.readlines()]

	preamble_size = 5

	for i in range(preamble_size + 1, len(numbers)):
		candidate = numbers[i]

		if is_valid(i, numbers, preamble_size):
			continue

		print(f'{numbers[i]} is not valid')