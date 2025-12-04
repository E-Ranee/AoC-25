import os
import copy

script_dir = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(script_dir, "input.txt")
# file = os.path.join(script_dir, "test.txt")

f = open(file, "r")
file_data = f.readlines()
f.close()

data = []
for row in file_data:
    data.append([x for x in row.strip().split()[0]])

def check_if_accessible(row_index, col_index, grid):
    # the upper and lower bounds of the box
    min = 0
    max = len(grid) - 1

    # the relative change in coordinates for all 8 directions
    north = (-1,0)
    north_east = (-1,1)
    east = (0,1)
    south_east = (1,1)
    south = (1,0)
    south_west = (1,-1)
    west = (0,-1)
    north_west = (-1,-1)

    # for troubleshooting: identifying which neighbours it registered as finding paper
    neighbours = []
    adjacent_paper = 0

    for direction in [north, north_east, east, south_east, south, south_west, west, north_west]:
        new_row_index = row_index + direction[0]
        new_col_index = col_index + direction[1]

        # check that the direction isn't outside of bounds
        if new_row_index >= min and new_row_index <= max and new_col_index >= min and new_col_index <= max:
            # check if it is what we're looking for
            if grid[new_row_index][new_col_index] == "@":
                neighbours.append((new_row_index, new_col_index))
                adjacent_paper += 1

    # only accessible if fewer than 4 neighbours
    if adjacent_paper < 4:
        return 1
    else:
        return 0
    
accessible_roll = 0

for row_index in range(len(data)):
    for col_index in range(len(data[0])):
        if data[row_index][col_index] == "@":
            accessible_roll += check_if_accessible(row_index, col_index, data)

print(accessible_roll)

##### PART 2 ####

accessible_roll = 0
changes_made_this_cycle = 0
new_grid = copy.deepcopy(data)
keep_going = True

# we will keep looping until there is a pass where no new accesible rolls are found
while keep_going:
    temp_grid = copy.deepcopy(new_grid) 
    # this is the grid that is constructed for the next loop
    # we still need to keep the current loop's data (new grid) intact instead of deleting rolls as we go
    for row_index in range(len(data)):
        for col_index in range(len(data[0])):
            if new_grid[row_index][col_index] == "@": # if you find a roll...
                accessible = check_if_accessible(row_index, col_index, new_grid) #... check how many neighbours it has
                accessible_roll += accessible
                if accessible:
                    changes_made_this_cycle += 1 # update the count so we know we're not done yet
                    temp_grid[row_index][col_index] = "." # delete this for the next loop
    if changes_made_this_cycle == 0: # once we've done a whole loop with no changes, we're finished
        keep_going = False
    else:
        changes_made_this_cycle = 0 # reset the count for the next loop
    new_grid = copy.deepcopy(temp_grid) # update the grid with the changes for the next loop

print(accessible_roll)

