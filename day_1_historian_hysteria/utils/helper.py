"""
Utilities for reading input files and processing data.
"""

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
