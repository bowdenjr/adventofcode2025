from scripts.utilities import open_advent_calendar



# load = open_advent_calendar("day_05\puzzle_input.txt")
load = open_advent_calendar("day_05\sample_input.txt")

for i, row in enumerate(load):
    if row == "":
        id_ranges = load[:i]
        products = load[i+1:]

lookup_ids = []

for id_range in id_ranges:
    numbers = id_range.split("-")
    lookup_id_range = tuple([int(numbers[0]), int(numbers[1])])
    lookup_ids.append(lookup_id_range)
    
overall_id_length = 0

for id in lookup_ids:
    for id_right in lookup_ids:
        if id == id_right:
            continue
        if id_right[0] <= id[1] and id_right[1] > id[1]:
            # right overlap case
            overall_id_length += id_right[1] - id[1]            
        elif id_right[0] < id[0] and id_right[1] >= id[1]:
            # left overlap case
            overall_id_length += id[0] - id_right[1]
        elif id_right[0] >= id[0] and id_right[1] <= id[1]:
            # right is entirely within
            pass
        elif id_right[0] < id[0] and id_right[1] > id[1]:
            # id is entirely within right
            pass
        else:
            # right is entierly separate
            overall_id_length += id[1] - id[0] + 1
            
     
    
    pass

# There are several cases




print(overall_id_length)

