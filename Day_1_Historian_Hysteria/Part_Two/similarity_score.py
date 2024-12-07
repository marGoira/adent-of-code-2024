"""
Module for calculating similarity score between lists.
"""

import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.insert(0, parent_dir)

from Day_1_Historian_Hysteria.utils.helper import read_input_file, process_lines

def dayonetasktwo():
    """Runs the task for Day 1 Part Two."""
    current_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(current_dir, '..', 'input.txt')

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
    dayonetasktwo()

if __name__ == "__main__":
    main()
