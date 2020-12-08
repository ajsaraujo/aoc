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

def execute_program(instructions):
	was_executed = [False for i in range(len(instructions))]

	index = 0
	accumulator = 0

	while not was_executed[index]:
		was_executed[index] = True
		index, accumulator = execute_instruction(instructions[index], index, accumulator)	
	
	return f'Instruction {index} is being executed for the second time. Acc value is {accumulator}'

file_name = sys.argv[1]

with open(file_name, 'r') as file:
	content = file.readlines()
	instructions = parse_instructions(content)
	print(execute_program(instructions))

