from scripts.utilities import open_advent_calendar






if __name__ == '__main__':
    
    batteries = open_advent_calendar("day_03\sample_input.txt")
    # batteries = open_advent_calendar("day_03\puzzle_input.txt")

    sum = 0
    seq_length = 2
    
    for battery in batteries:
        
        search = True
        answer_pos = 0
        length = len(battery)
        digit_1 = 0
        digit_2 = 0       
        
        while search:
            
            max_digit = max(list(battery))
            positions = [i for i in range(len(battery)) if battery[i] == max_digit]
            positions = [i for i in positions if i <= (length - seq_length + answer_pos)]
            if positions:
                digit_1 = max_digit
            
            for position in positions:
                max_digit = max(list(battery[position+1:]))
                positions = [i for i in range(len(battery)) if battery[i] == max_digit]
                positions = [i for i in positions if i <= (length - seq_length + answer_pos)]
                if positions:
                    digit_2 = max_digit
                    search = False
                    sum += int(str(digit_1) + str(digit_2))
                
    print(sum)
            
                