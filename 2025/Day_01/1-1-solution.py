import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '1-puzzle_input.txt')

with open(file_path, 'r') as file:
    puzzle_input = [line.strip() for line in file.readlines()]

dial_position = 50

def move_dial(direction, clicks):
    global dial_position
    if direction == 'L':
        dial_position = (dial_position - clicks) % 100
    elif direction == 'R':
        dial_position = (dial_position + clicks) % 100
    else:
        raise ValueError("Invalid direction. Use 'L' for left or 'R' for right.")

count = 0

for position in puzzle_input:
    direction = position[0]
    clicks = int(position[1:])
    move_dial(direction, clicks)
    if dial_position == 0:
        count += 1

print(count)