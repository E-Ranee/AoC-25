import os
script_dir = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(script_dir, "input.txt")
# file = os.path.join(script_dir, "test.txt")

f = open(file, "r")
file_data = f.readlines()
f.close()

data = []
for row in file_data:
    data.append([int(x) for x in row.strip().split()[0]])

def get_joltage(battery_bank, number_of_batteries):
    """Works by looking at the section of the list after the digits already found and before {number of batteries remaining} from the end"""
    digits = []
    min_index = 0
    for i in range(number_of_batteries): # loop this many times
        unreserved = len(battery_bank) - number_of_batteries + len(digits) + 1 # keep the last x digits free for future loops
        current_slice = battery_bank[min_index:unreserved]
        current_digit = max(current_slice) # the highest number in the available slice
        while battery_bank[min_index] != current_digit: # increment index until you reach the position of this number
            min_index += 1
        min_index += 1 
        digits.append(current_digit)

    string = ""
    for d in digits:
        string += str(d)

    if len(string) != number_of_batteries:
        print(f"""{len(string)} is the string length but {number_of_batteries} is what it should be""")

    return int(string)

partA = []
partB = []
for battery_bank in data:
    partA.append(get_joltage(battery_bank,2))
    partB.append(get_joltage(battery_bank, 12))

print(sum(partA))
print(sum(partB))

