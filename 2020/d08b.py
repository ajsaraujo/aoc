import sys

def parse_instructions(file_content):
	instructions = []

	for line in file_content:
		instruction_code, instruction_value = line.split(' ')

		signal = -1

		if instruction_value[0] == '+':
			signal = 1

		instruction = {
			'code': instruction_code,
			'value': int(instruction_value[1:]) * signal
		}

		instructions.append(instruction)

	return instructions

def execute_instruction(instruction, index, accumulator):
	execute = {
		'nop': lambda v, i, acc : [i + 1, acc],
		'acc': lambda v, i, acc : [i + 1, acc + v],
		'jmp': lambda v, i, acc : [i + v, acc]
	}

	code = instruction['code']
	value = instruction['value']

	return execute[code](value, index, accumulator)

def terminates(instructions):
	was_executed = [False for i in range(len(instructions))]

	index = 0
	accumulator = 0

	while index < len(instructions) and (not was_executed[index]):
		was_executed[index] = True
		index, accumulator = execute_instruction(instructions[index], index, accumulator)	
	
	terminates = index == len(instructions)

	if terminates:
		print(f'Program terminated with acc {accumulator}')

	return terminates

def reverse_code(code):
	if code == 'nop':
		return 'jmp'
	
	return 'nop'

file_name = sys.argv[1]

with open(file_name, 'r') as file:
	content = file.readlines()
	instructions = parse_instructions(content)
	
	for instruction in instructions:
		real_code = instruction['code']

		if real_code in ['nop', 'jmp']:
			new_code = reverse_code(real_code)
			instruction['code'] = new_code

			if new_code == 'jmp' and instruction['value'] == 0:
				instruction['code'] = 'nop'
				continue
		
			if terminates(instructions):
				break

			instruction['code'] = real_code