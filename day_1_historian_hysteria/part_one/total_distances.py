"""
Module for calculating total distances between lists.
"""

import os
from day_1_historian_hysteria.utils.helper import read_input_file, process_lines, setup_path

# Set up the module search path
task_dir, parent_dir = setup_path()

def dayonetaskone():
    """Runs the task for Day 1 Part One."""
    # Function implementation
    function_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(function_dir, '..', 'input.txt')

    lines = read_input_file(input_file_path)
    list1, list2 = process_lines(lines)

    total_distance = sum(abs(a - b) for a, b in zip(list1, list2))
    print("Total Distance:", total_distance)

def main():
    """Main function for standalone execution."""
    dayonetaskone()

if __name__ == "__main__":
    main()
