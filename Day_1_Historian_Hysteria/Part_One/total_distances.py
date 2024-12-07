"""
Module for calculating total distances between lists.
"""

import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.insert(0, parent_dir)

from Day_1_Historian_Hysteria.utils.helper import read_input_file, process_lines

def dayonetaskone():
    """Runs the task for Day 1 Part One."""
    input_file_path = os.path.join(parent_dir, 'Day_1_Historian_Hysteria', 'input.txt')

    lines = read_input_file(input_file_path)
    list1, list2 = process_lines(lines)

    total_distance = sum(abs(a - b) for a, b in zip(list1, list2))
    print("Total Distance:", total_distance)

def main():
    dayonetaskone()

if __name__ == "__main__":
    main()
