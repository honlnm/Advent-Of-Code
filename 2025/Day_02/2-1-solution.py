
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '2-puzzle_input.txt')

with open(file_path, 'r') as file:
    puzzle_input =  file.readline().strip().split(',')

prod_code_ranges = []
for prod_code in puzzle_input:
    prod_code_range = prod_code.split('-')
    prod_code_ranges.append(prod_code_range)

prod_full_ranges = []
for prod_code in prod_code_ranges:
    start_num = int(prod_code[0])
    end_num = int(prod_code[1])
    full_range = list(range(start_num, end_num + 1))
    prod_full_ranges.append(full_range)

def find_repeating_pattern(num: str):
    length = len(num)
    if length % 2 == 0:
        half_length = length // 2
        if num[:half_length] == num[half_length:]:
            return num
    return None

invalid_codes = []
for full_range in prod_full_ranges:
    for num in full_range:
        num = str(num)
        result = find_repeating_pattern(num)
        if result:
            invalid_codes.append(num)

sum_invalid = sum(int(code) for code in invalid_codes)
print(sum_invalid)