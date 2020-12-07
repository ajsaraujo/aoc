import sys

def parse_insider_bag(word_list):
	if 'no other bags' in ' '.join(word_list):
		return None

	clean_list = [word for word in word_list if word != '']

	bag = {}

	bag['name'] = ' '.join(clean_list[1:3])
	bag['quantity'] = int(clean_list[0])

	return bag

def read_bags(file_content):
	bags = {}

	for line in file_content:
		this_bag = {}

		parts = [segment.split(' ') for segment in line.split(',')]

		this_bag_name = ' '.join(parts[0][:2])

		inside_bags = [parse_insider_bag(parts[0][4:])]
		inside_bags += [parse_insider_bag(part) for part in parts[1:]]

		for bag in inside_bags:
			if bag is None:
				continue

			bag_name = bag['name']
			this_bag[bag_name] = bag['quantity']

		bags[this_bag_name] = this_bag

	return bags

file_name = sys.argv[1]

def count_how_many_bags(bags, bag_name):
	bag = bags[bag_name]

	sum = 1

	for inner_bag, quantity in bag.items():
		sum += quantity * count_how_many_bags(bags, inner_bag)

	print(f'{bag_name} = {sum}')
	return sum

with open(file_name, 'r') as file:
	file_content = file.readlines()
	bags = read_bags(file_content)

	print(count_how_many_bags(bags, 'shiny gold'))
