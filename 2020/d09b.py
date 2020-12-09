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

def get_invalid_number(preamble_size, numbers):
    for i in range(preamble_size + 1, len(numbers)):
        candidate = numbers[i]

        if is_valid(i, numbers, preamble_size):
            continue

        return numbers[i]

def encryption_weakness(invalid_number, numbers):
    for i in range(len(numbers)):
        total = numbers[i]
    
        minimal = numbers[i]
        maximum = numbers[i]

        for j in range(i + 1, len(numbers)):
            total += numbers[j]

            minimal = min(minimal, numbers[j])
            maximum = max(maximum, numbers[j])

            if total == invalid_number:
                return minimal + maximum

            if total > invalid_number:
                break

with open(file_name, 'r') as file:
    numbers = [int(num) for num in file.readlines()]
    preamble_size = 25
    invalid_number = get_invalid_number(preamble_size, numbers)
    print(encryption_weakness(invalid_number, numbers))