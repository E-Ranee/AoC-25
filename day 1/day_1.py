file = "input.txt"
# file = "test.txt"

f = open(file, "r")
file_data = f.readlines()
f.close()

data = []
for row in file_data:
    instruction_string = row.strip() # format "L68"
    number_to_change_by = int(instruction_string[1:]) # get just the digits
    if instruction_string[0] == "R": # positive if R, negative if L
        data.append(number_to_change_by)
    else:
        data.append(-number_to_change_by)

current_position = 50
password_part1 = 0
password_part2 = 0

for instruction in data:
    new_position = (current_position + instruction)%100
    started_at_zero = current_position == 0
    ended_at_zero = new_position == 0

    # part 1: check if it's pointing at "0" (any multiple of 100)
    if new_position == 0:
        password_part1 += 1

    # part 2: check how many times it passes a multiple of 100
    if current_position + instruction != new_position: # if they are different, it means that the new number is in a different grouping of 100 and has crossed 0 at least once
        difference = current_position + instruction - new_position # the amount in hundreds that the new number is off by

        # If it has CROSSED A THRESHOLD (difference is at least 100)
        
        # if it starts at 0 and goes left
        if started_at_zero and instruction < 0:
            # disregard the first "crossing of zero" (leaving the starting point)
            password_part2 += abs(difference/100) - 1

        # starts at 0 and goes right
        elif started_at_zero and instruction > 0:
            # count how many chunks away the new number is
            # no adjustments necessary
            password_part2 += abs(difference/100) 

        # goes left and ends on 0
        elif ended_at_zero and instruction < 0:
            # add an extra counting for when it hits 0 at the end
            password_part2 += abs(difference/100) + 1 

        # neither starts at 0 nor ends at 0 so you can just count how many chunks of 100 have passed
        else:
            password_part2 += abs(difference/100)

    # doesn't CROSS the threshold but could still END on a 0 which would count
    else:
        # only counts if it ends on 0
        if ended_at_zero:
            password_part2 += 1
        else: # neither crossed a 0 not ended on a 0 so doesn't count
            pass

    # reset for next instruction
    current_position = new_position

print(password_part1)
print(int(password_part2))