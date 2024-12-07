"""
Module for calculating total distances between lists.
"""
from day_1_historian_hysteria.utils.helper import read_input_file, process_lines
import os
import sys

task_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(task_dir, '..', '..'))
sys.path.insert(0, parent_dir)

def dayonetaskone():
    """Runs the task for Day 1 Part One."""
    task_dir = os.path.dirname(__file__)
    input_file_path = os.path.join(task_dir, '..', 'input.txt')

    lines = read_input_file(input_file_path)
    list1, list2 = process_lines(lines)

    total_distance = sum(abs(a - b) for a, b in zip(list1, list2))
    print("Total Distance:", total_distance)

def main():
    dayonetaskone()

if __name__ == "__main__":
    main()
