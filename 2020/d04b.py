import sys
import re

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

def passport_ok(passport, validators):
    for field in validators:
        if field not in passport:
            return False
        
        validator = validators[field]
        value = passport[field]

        if not validator(value):
            return False
    
    return True

def count_valid_passports(passports):
    valid_passports = 0
    validators = {
        'byr': lambda birth_year : len(birth_year) == 4 and int(birth_year) in range(1920, 2003),
        'ecl': lambda eye_color : eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'iyr': lambda issue_year : len(issue_year) == 4 and int(issue_year) in range(2010, 2021),
        'hgt': lambda height : int(height[:-2]) in range(150, 194) if height[-2:] == 'cm' else int(height[:-2]) in range(59, 77),
        'pid': lambda pass_id : len(pass_id) == 9,
        'eyr': lambda exp_year : len(exp_year) == 4 and int(exp_year) in range(2020, 2031),
        'hcl': lambda hair_color : re.match('^#[0-9a-f]{6}$', hair_color)
    }

    for passport in passports:
        if passport_ok(passport, validators):
            valid_passports += 1

    return valid_passports                

def height_field_looks_ok(passport):
    if 'hgt' not in passport:
        return False
    
    height = passport['hgt']

    return 'cm' in height or 'in' in height

    
def remove_bad_passports(passports):
    return [passport for passport in passports if height_field_looks_ok(passport)]

passports = read_passports()
good_passports = remove_bad_passports(passports)

print(count_valid_passports(good_passports))