from scripts.utilities import open_advent_calendar


if __name__ == '__main__':
    
    # batteries = open_advent_calendar("day_03\sample_input.txt")
    batteries = open_advent_calendar("day_03\puzzle_input.txt")

    sum = 0
    for battery in batteries:
        pos_1 = -1
        pos_2 = -1
        for num in range(99,10,-1):
            digit_1, digit_2 = list(str(num))
            pos_1 = battery.find(digit_1)
            pos_2 = battery.find(digit_2, pos_1+1)
            
            if pos_1 != len(battery) and pos_1 < pos_2 and pos_1 != pos_2 and pos_1 != -1 and pos_2 != -1:
                sum += num
                print(f"found {num}")
                break
                
    print(sum)
            
                