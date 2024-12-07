"""
Module for calculating similarity score between lists.
"""

import os
from day_1_historian_hysteria.utils.helper import read_input_file, process_lines, setup_path

# Set up the module search path
task_dir, parent_dir = setup_path()

def dayonetasktwo():
    """Runs the task for Day 1 Part Two."""
    # Function implementation
    function_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(function_dir, '..', 'input.txt')

    lines = read_input_file(input_file_path)
    list1, list2 = process_lines(lines)
    sum_list = []
    result = 0

    # Now we must check how many times left one is on the right side.
    for i in list1:
        multiplier = 0
        item = i
        for y in list2:
            if item == y:
                multiplier += 1
        sum_list.append(item * multiplier)

    for x in sum_list:
        result += x

    print(result)

def main():
    """Main function for standalone execution."""
    dayonetasktwo()

if __name__ == "__main__":
    main()
