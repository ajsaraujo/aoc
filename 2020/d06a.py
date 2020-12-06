import sys

def separate_into_groups(lines):
	groups = []
	current_group = []

	for line in lines:
		if line != '\n':
			parsed_line = line.replace('\n', '')
			current_group.append(parsed_line)
		else:
			groups.append(current_group)
			current_group = []

	groups.append(current_group)

	return groups

def count_group_answers(group):
	positive_answers = set()

	for form in group:
		for answer in form:
			positive_answers.add(answer)

	return len(positive_answers)

def read_groups():
	file_name = sys.argv[1]

	with open(file_name, 'r') as file:
		lines = file.readlines()
		groups = separate_into_groups(lines)

		return groups

groups = read_groups()
count = 0

for group in groups:
	count += count_group_answers(group)

print(count)
