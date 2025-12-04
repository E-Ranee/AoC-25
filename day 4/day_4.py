import os
script_dir = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(script_dir, "input.txt")
# file = os.path.join(script_dir, "test.txt")

f = open(file, "r")
file_data = f.readlines()
f.close()

data = []
for row in file_data:
    data.append(row.strip())

def check_if_accessible(row_index, col_index):
    min = 0
    max = len(data) - 1

    north = (-1,0)
    north_east = (-1,1)
    east = (0,1)
    south_east = (1,1)
    south = (1,0)
    south_west = (1,-1)
    west = (0,-1)
    north_west = (-1,-1)

    neighbours = []
    adjacent_paper = 0

    for direction in [north, north_east, east, south_east, south, south_west, west, north_west]:
        new_row_index = row_index + direction[0]
        new_col_index = col_index + direction[1]

        if new_row_index >= min and new_row_index <= max and new_col_index >= min and new_col_index <= max:
            if data[new_row_index][new_col_index] == "@":
                neighbours.append((new_row_index, new_col_index))
                adjacent_paper += 1

    if adjacent_paper < 4:
        return 1
    else:
        return 0
    
accessible_roll = 0

for row_index in range(len(data)):
    for col_index in range(len(data[0])):
        if data[row_index][col_index] == "@":
            accessible_roll += check_if_accessible(row_index, col_index)

print(accessible_roll)
