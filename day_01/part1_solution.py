from scripts.utilities import (open_advent_calendar)

# rotations = open_advent_calendar("day_01\sample_input.txt")
rotations = open_advent_calendar("day_01\puzzle_input.txt")

pos = 50
password = 0

for rot in rotations:
    if rot[0] == "L":
        pos -= abs(int(rot[1:]))
        pos = pos % 100    
    else:
        pos += abs(int(rot[1:])) 
        pos = pos % 100    
        
    if pos == 0:
        password += 1

print(password)

        