from scripts.utilities import open_advent_calendar


def split_number(x):

    length = int(len(str(x)) / 2)

    return (int(str(x)[:length]), int(str(x)[length:]))


if __name__ == "__main__":

    # ranges = open_advent_calendar("day_02\sample_input.txt")
    ranges = open_advent_calendar("day_02\puzzle_input.txt")
    ranges = ranges[0].split(",")
    sum = 0

    for range in ranges:
        range = range.split("-")
        num = int(range[0])
        while num <= int(range[-1]):
            if len(str(num)) % 2 == 0:
                split = split_number(num)
                if split[0] == split[1]:
                    sum += num
            num += 1

    print(sum)

