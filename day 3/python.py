import os
script_dir = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(script_dir, "input.txt")
file = os.path.join(script_dir, "test.txt")

f = open(file, "r")
file_data = f.readlines()
f.close()

data = []
for row in file_data:
    data.append(row.strip())

print(data)