"""
Module for calculating similarity score between lists.
"""

from day_1_historian_hysteria.utils.helper import (
    setup_path,
    read_input_file,
    process_lines,
    get_input_file_path )

# Set up the module search path and get directories
task_dir, parent_dir = setup_path()

def calculate_similarity_score():
    """Calculates the similarity score between two lists based on input data."""
    input_file_path = get_input_file_path(task_dir)

    lines = read_input_file(input_file_path)
    list1, list2 = process_lines(lines)
    sum_list = []
    result = 0

    # Check how many times the left one is on the right side.
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
    calculate_similarity_score()

if __name__ == "__main__":
    main()
