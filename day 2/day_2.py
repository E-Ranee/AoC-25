import os
script_dir = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(script_dir, "input.txt")
# file = os.path.join(script_dir, "test.txt")

f = open(file, "r")
file_data = f.readlines()
f.close()

data = file_data[0].split(",")

list_of_ranges = []
for individual_range in data:
    list_of_ranges.append([int(x) for x in individual_range.split("-")])

### for part B ###
def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

factors = {}
for n in range(1,12):
    factors[n] = find_factors(n)
###

invalid_IDs = []
partB_invalid_IDs = []
for pair in list_of_ranges:
    for n in range(pair[0], pair[1]+1):
        number_of_digits = len(str(n))
        mid = int(number_of_digits/2)
        number_str = str(n)
        if number_str[:mid] == number_str[mid:]:
            invalid_IDs.append(n)
        ### part B
        factors_to_check = factors[number_of_digits]
        chunks = []
        index = 0
        done = False
        while done == False:
            if number_of_digits == 1:
                done = True
            for chunk_size in factors_to_check[:-1]:
                for i in range(int(number_of_digits/chunk_size)):
                    chunks.append(number_str[index:index+chunk_size])
                    index += chunk_size
                if len(set(chunks)) == 1:
                    partB_invalid_IDs.append(n)
                    chunks = []
                    index = 0
                    done = True
                    break
                chunks = []
                index = 0
                done = True

print(sum(invalid_IDs))
print(sum(partB_invalid_IDs))