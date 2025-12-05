from scripts.utilities import open_advent_calendar



rolls = open_advent_calendar("day_04\puzzle_input.txt")

sum = 0 
i_max = len(rolls)-1
j_max = len(rolls[0])-1

for i, roll in enumerate(rolls):
    
    for j in range(len(roll)):
        
        if roll[j] == "@":
            
            if i == 0 and j==0:
                check_area = [rolls[i][j+1],
                            rolls[i+1][j],
                            rolls[i+1][j+1]]
            
            elif i == 0 and j == j_max:
                check_area = [rolls[i][j-1],
                            rolls[i+1][j-1],
                            rolls[i+1][j]]
                    
            elif i == i_max and j == 0:
                check_area= [rolls[i-1][j],
                            rolls[i-1][j+1],                       
                            rolls[i][j+1]]
            
            elif i == i_max and j == j_max:
                check_area = [rolls[i-1][j-1], 
                            rolls[i-1][j],
                            rolls[i][j-1]]
            
            elif i == 0:
                # top border
                check_area = [rolls[i][j-1],                          
                            rolls[i][j+1],
                            rolls[i+1][j-1],
                            rolls[i+1][j],
                            rolls[i+1][j+1]]
            
            elif j == 0:            
                # left border
                check_area = [rolls[i-1][j],
                            rolls[i-1][j+1],                          
                            rolls[i][j+1],
                            rolls[i+1][j],
                            rolls[i+1][j+1]]
                
            elif i == i_max:
                # bottom border
                check_area = [rolls[i-1][j-1], 
                            rolls[i-1][j],
                            rolls[i-1][j+1],
                            rolls[i][j-1],                          
                            rolls[i][j+1]]
                
            elif j == j_max:
                # right border
                check_area = [rolls[i-1][j-1], 
                            rolls[i-1][j],
                            rolls[i][j-1],
                            rolls[i+1][j-1],
                            rolls[i+1][j]]

            else:
                # middle middle
                check_area = [rolls[i-1][j-1], 
                            rolls[i-1][j],
                            rolls[i-1][j+1],
                            rolls[i][j-1],                          
                            rolls[i][j+1],
                            rolls[i+1][j-1],
                            rolls[i+1][j],
                            rolls[i+1][j+1]]
            
            other_roll_count = len([x for x in check_area if x == "@"])
            if other_roll_count < 4:
                sum += 1

print(sum)
            
