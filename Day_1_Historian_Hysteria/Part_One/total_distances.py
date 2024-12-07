"""
Module for calculating total distances between lists.
"""

import os

def main():

    # Lets read the input from input.txt
    # requests library would be nice way also.
    current_dir = os.path.dirname(__file__) 
    input_file_path = os.path.join(current_dir, '..', 'input.txt')

    with open(input_file_path, 'r', encoding='utf-8') as file:
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

if __name__ == "__main__":
    main()
