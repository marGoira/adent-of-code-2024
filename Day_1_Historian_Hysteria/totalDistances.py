# Lets read the input from input.txt
# requests library would be nice way also.
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Lets declare two list.
list1 = []
list2 = []

# Process each line and split numbers into the two lists
for line in lines:
    numbers = line.split()
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))

# So now I sort those list because we want to handle smallest - smallest etc.
list1.sort()
list2.sort()

# Now I should get that total distance bu summing those differences.
total_distance = sum(abs(a - b) for a, b in zip(list1, list2))

print("Total Distance:", total_distance)