import sys

def make_dict(list_of_strings):
    my_dict = {}

    for data in list_of_strings:
        key, value = data.split(':')
        my_dict[key] = value

    return my_dict

def read_passports():
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        list_of_strings = file.read().split('\n\n')
        list_of_lists = [value.replace('\n', ' ').split(' ') for value in list_of_strings]
        clean_list = [[value for value in each_list if value != ''] for each_list in list_of_lists]

        list_of_dicts = [make_dict(passport) for passport in clean_list]        

        return list_of_dicts

def count_valid_passports(passports):
    valid_passports = 0
    fields_to_check = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    
    for passport in passports:
        passport_ok = True

        for field in fields_to_check:
            if field not in passport:
                passport_ok = False

        if passport_ok:
            print(passport)
            valid_passports += 1

    return valid_passports                

passports = read_passports()
print(count_valid_passports(passports))