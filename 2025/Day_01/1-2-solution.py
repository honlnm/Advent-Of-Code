import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '1-puzzle_input.txt')

with open(file_path, 'r') as file:
    puzzle_input = [line.strip() for line in file.readlines()]

start_dial_position = 50
dial_position = start_dial_position

def move_dial(direction, clicks):
    global dial_position
    if direction == 'L':
        dial_position = (dial_position - clicks) % 100
    elif direction == 'R':
        dial_position = (dial_position + clicks) % 100

def find_full_rotations(clicks):
    return clicks // 100

count = 0

for position in puzzle_input:
    direction = position[0]
    clicks = int(position[1:])
    move_dial(direction, clicks)
    if dial_position == 0:
        count += 1
    if direction == 'L' and dial_position > start_dial_position and start_dial_position != 0:
        count += 1
    elif direction == 'R' and dial_position < start_dial_position and dial_position != 0:
        count += 1
    if find_full_rotations(clicks) > 0:
        count += find_full_rotations(clicks)
    start_dial_position = dial_position

print(count)
