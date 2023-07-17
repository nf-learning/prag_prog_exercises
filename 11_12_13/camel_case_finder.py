import os
import re
import sys

def convert_camel_to_snake_case(variable):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', variable).lower()

def find_variables_matching_pattern(file_path, pattern):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    variables = []

    for line_num, line in enumerate(lines, start=1):
        matches = re.findall(pattern, line)
        for match in matches:
            variables.append((match, file_path, line_num))

    return variables

def convert_variables_to_snake_case(file_path, pattern):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    converted_lines = []
    for line in lines:
        converted_line = re.sub(pattern, lambda x: convert_camel_to_snake_case(x.group()), line)
        converted_lines.append(converted_line)

    new_file_path = file_path.replace(".py", "_variable_changed.py")
    with open(new_file_path, 'w') as new_file:
        new_file.writelines(converted_lines)

def scan_directory_for_matching_pattern(directory, pattern, file_extensions, convert_to_snake_case):
    matching_variables = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extensions):
                file_path = os.path.join(root, file)
                matching_variables.extend(find_variables_matching_pattern(file_path, pattern))
                if convert_to_snake_case:
                    convert_variables_to_snake_case(file_path, pattern)

    return matching_variables

def print_matching_variables(variables):
    if variables:
        print("Matching variables found:")
        for variable, file_path, line_num in variables:
            print(f"Variable: {variable}, File: {file_path}, Line: {line_num}")
    else:
        print("No matching variables found in the specified directory.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python came_case_finder.py <directory_path> [-c/--convert]")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("Error: Invalid directory path.")
        sys.exit(1)

    pattern = r'\b[a-z]+(?:[A-Z][a-z]*)+\b'
    file_extensions = ('.py', '.pyw')

    convert_to_snake_case = False
    if len(sys.argv) == 3 and sys.argv[2] in ('-c', '--convert'):
        convert_to_snake_case = True

    matching_variables = scan_directory_for_matching_pattern(directory_path, pattern, file_extensions, convert_to_snake_case)
    print_matching_variables(matching_variables)

if __name__ == "__main__":
    main()
