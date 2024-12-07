"""
Module for calculating total distances between lists.
"""

from day_1_historian_hysteria.utils.helper import ( 
    setup_path, 
    read_input_file, 
    process_lines, 
    get_input_file_path )

# Set up the module search path and get directories
task_dir, parent_dir = setup_path()

def calculate_total_distance():
    """Calculates the total distance between two lists based on input data."""
    input_file_path = get_input_file_path(task_dir)

    lines = read_input_file(input_file_path)
    list1, list2 = process_lines(lines)

    total_distance = sum(abs(a - b) for a, b in zip(list1, list2))
    print("Total Distance:", total_distance)

def main():
    """Main function for standalone execution."""
    calculate_total_distance()

if __name__ == "__main__":
    main()
