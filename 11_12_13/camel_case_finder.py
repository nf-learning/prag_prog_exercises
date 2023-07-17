
import os
import re
import sys

def find_variables_matching_pattern(file_path, pattern):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    variables = []

    for line_num, line in enumerate(lines, start=1):
        matches = re.findall(pattern, line)
        for match in matches:
            variables.append((match, file_path, line_num))

    return variables

def scan_directory_for_matching_pattern(directory, pattern, file_extensions):
    matching_variables = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extensions):
                file_path = os.path.join(root, file)
                matching_variables.extend(find_variables_matching_pattern(file_path, pattern))

    return matching_variables

def print_matching_variables(variables):
    if variables:
        print("Matching variables found:")
        for variable, file_path, line_num in variables:
            print(f"Variable: {variable}, File: {file_path}, Line: {line_num}")
    else:
        print("No matching variables found in the specified directory.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python came_case_finder.py <directory_path> ")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("Error: Invalid directory path.")
        sys.exit(1)

    pattern = r'\b[a-z]+(?:[A-Z][a-z]*)+\b'
    file_extensions =  ('.py', '.pyw')

    matching_variables = scan_directory_for_matching_pattern(directory_path, pattern, file_extensions)
    print_matching_variables(matching_variables)

if __name__ == "__main__":
    main()
