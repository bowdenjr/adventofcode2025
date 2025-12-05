from scripts.utilities import open_advent_calendar


def split_number(x):

    length = int(len(str(x)) / 2)

    return (int(str(x)[:length]), int(str(x)[length:]))


def chop_number(x, chop_length):
    """
    1212, 2 -> 12, 12
    123123, 3 -> 123, 123
    544544544, 3 -> 544, 544, 544
    """
    
    times = len(str(x)) // chop_length
    output = [int(str(x)[t*chop_length:chop_length*(t+1)]) for t in range(times)]
    
    
    return output


if __name__ == "__main__":

    # ranges = open_advent_calendar("day_02\sample_input.txt")
    ranges = open_advent_calendar("day_02\puzzle_input.txt")
    ranges = ranges[0].split(",")
    sum = 0
    record = {}

    for r in ranges:
        r = r.split("-")
        num = int(r[0])
        while num <= int(r[-1]):
            max_length = len(str(num)) // 2
            for i in range(1, max_length+1):
                if len(str(num)) % i != 0:
                    continue
                chopped_num = chop_number(num, i)
                if len(set(chopped_num)) == 1 and num not in record.keys():
                    # print(f"Invalid ID at {num}")
                    record[num] = 1
                    sum += num
            num += 1

    print(sum)
