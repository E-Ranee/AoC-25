import os
script_dir = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(script_dir, "input.txt")
# file = os.path.join(script_dir, "test.txt")

f = open(file, "r")
file_data = f.readlines()
f.close()

############## PROCESSING INPUT ########################

fresh_ID_ranges = []
ingredient_IDs = []

for row in file_data:
    if "-" in row:
        # split on hyphen and add a list of two ints to the list of ranges
        fresh_ID_ranges.append([int(x) for x in row.strip().split("-")]) 
    else:
        try:
            # remove new line and convert to an integer
            ingredient_IDs.append(int(row.strip())) 
        except ValueError: 
            # skip over the new line separator between the ranges and IDs
            pass

############# PART 1 ####################################

number_of_fresh_ingredients = 0
for ingredient in ingredient_IDs:
    for range in fresh_ID_ranges:
        # check if it's in the range, min and max inclusive
        if ingredient >= range[0] and ingredient <= range[1]: 
            number_of_fresh_ingredients += 1
            break # no need to keep checking if it fits into any other ranges

print(number_of_fresh_ingredients)

########### PART 2 ######################################
# check the total number of potentially fresh IDs
# second part of the input now irrelevant

# https://www.reddit.com/r/adventofcode/comments/1pep1z7/2025_day_5_part_2_algorithm_visualization/ 
# used this to help me figure out the logic

# sort it based on lower part of ranges
# This means that if the lowest part of the next range is within the bounds of the current range
# that it overlaps and we can just extend the upper range if relevant
# if it doesn't overlap, we can submit the old range as finished and start a new range
fresh_ID_ranges.sort(key=lambda x : x[0]) 

new_ranges = []
lower_bound = None
upper_bound = None
for range in fresh_ID_ranges:
    # if no range currently being worked on:
    if lower_bound == None:
        lower_bound = range[0]
        upper_bound = range[1]

    # there is now a range being looked at
    # does the new range start within it (overlaps)
    elif range[0] >= lower_bound and range[0] <= upper_bound:
        # does the end of this range extend the previous range?
        if range[1] > upper_bound:
            upper_bound = range[1]
    
    # there IS a range being looked at but this new range doesn't overlap with it
    else:
        # add the final overlapped range to the list
        new_ranges.append([lower_bound, upper_bound]) 
        # set this as the new range to be expanded
        lower_bound = range[0]
        upper_bound = range[1]

# if the last loop didn't enter the else outcome because it extended the range
# add it separately to the end of the list
if new_ranges[-1] != [lower_bound, upper_bound]: 
    new_ranges.append([lower_bound, upper_bound])

# sum up the number of items in the ranges, upper bound inclusive
total = 0
for range in new_ranges:
    # eg [3,5]
    total += range[1] - range[0] + 1 # +1 to include upper bound

print(total)

