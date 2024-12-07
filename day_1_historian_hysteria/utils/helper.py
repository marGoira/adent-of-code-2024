"""
Utilities for reading input files and processing data.
"""

import os
import sys

def setup_path():
    """Sets up the module search path and returns task and parent directories.""" 
    task_dir = os.path.dirname(__file__) 
    parent_dir = os.path.abspath(os.path.join(task_dir, '..', '..')) 
    sys.path.insert(0, parent_dir) 
    return task_dir, parent_dir

def read_input_file(file_path):
    """Reads and returns lines from the specified input file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def process_lines(lines):
    """Processes lines into two sorted lists of integers."""
    list1, list2 = [], []
    for line in lines:
        numbers = line.split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))
    list1.sort()
    list2.sort()
    return list1, list2
