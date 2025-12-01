from scripts.utilities import (open_advent_calendar)


def sign(a):
    if a > 0:
        return 1
    return 0


# rotations = open_advent_calendar("day_01\sample_input.txt")
rotations = open_advent_calendar("day_01\puzzle_input.txt")

pos = 50
password = 0

for rot in rotations:
    
    last_pos = pos
    hundreds = 0
    
    shift = int(rot[1:])
    
    if shift > 100: 
        hundreds = shift // 100
        remainder = shift - (hundreds * 100)
    else:
        remainder = shift
    
    if rot[0] == "L":
        pos -= remainder
        if pos <= -100 or (sign(last_pos) != sign(pos) and last_pos != 0):
            password += 1      
            passing = True 
        else:
            passing = False      
        pos = pos % 100
        print(f"Dial moved L{shift} to point at {pos}")
        if passing:
            print(f"Passing zero, password is now {password}\n\n")
    else:
        pos += remainder
        if pos >= 100 or (sign(last_pos) != sign(pos) and last_pos != 0):
            password += 1 
            passing = True 
        else:   
            passing = False      
        pos = pos % 100    
        print(f"Dial moved R{shift} to point at {pos}")
        if passing:
            print(f"Passing zero, password is now {password}\n\n")
    
    if hundreds > 0:
        password += hundreds
    
    pass

print(password) # 2014 too low, 3894 too low, 5794 too low, 6193 not right, 6181 not right


