import os
import numpy as np
import math

script_dir = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(script_dir, "input.txt")
file = os.path.join(script_dir, "test.txt")

f = open(file, "r")
file_data = f.readlines()
f.close()

data = []
for row in file_data[:-1]:
    data.append([int(x) for x in row.strip().split()]) # data will be a 2d array of integers
data.append([x for x in file_data[-1].strip().split()]) # add the operators, which will be strings

# convert to a numpy array
data_np = np.array(data[:-1]) # 2d array of ints
operator_np = np.array(data[-1]) # 1d array of strings
# swap rows and columns
transposed_np = data_np.T # transposed 2d array of ints

totals = []
part_2_totals = []
for i in range(len(transposed_np)):
    # iterate grabbing one row from transposed data and get the operator from the list of strings
    operator = operator_np[i] # "+" or "*"
    row = transposed_np[i] # list of ints
    
    if operator == "+":
        totals.append(sum(row))
    else:
        totals.append(math.prod(row))

print(sum(totals))