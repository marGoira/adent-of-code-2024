import os

current_dir = os.path.dirname(__file__) 
input_file_path = os.path.join(current_dir, '..', 'input.txt')

with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Lets declare two list.
list1 = []
list2 = []
sumList = []
result = 0

# Process each line and split numbers into the two lists
for line in lines:
    numbers = line.split()
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))

# So now I sort those list because we want to handle smallest - smallest etc.
list1.sort()
list2.sort()

# Now we must check how many times left one is on the right side.
for i in list1:
    multiplier = 0
    item = i
    for y in list2:
        if item == y:
            multiplier += 1
    sumList.append(item * multiplier)

for x in sumList:
    result += x

print(result)