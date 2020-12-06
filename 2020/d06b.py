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
	answer_count = {}

	for form in group:
		for question in form:
			if question in answer_count:
				answer_count[question] += 1
			else:
				answer_count[question] = 1

	num_of_questions_everyone_answered = 0

	for count in answer_count.values():
		if count == len(group):
			num_of_questions_everyone_answered += 1

	return num_of_questions_everyone_answered

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
