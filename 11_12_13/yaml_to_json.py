import os
import sys
import yaml
import json

def convert_yaml_to_json(yaml_file, json_file):
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    with open(json_file, 'w') as file:
        json.dump(yaml_data, file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python yaml_to_json.py <dir>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print("Error: Directory does not exist.")
        sys.exit(1)

    for file_name in os.listdir(directory_path):
        if file_name.endswith('.yaml') or file_name.endswith('.yml'):
            yaml_file = os.path.join(directory_path, file_name)
            json_file = os.path.join(directory_path, file_name.rsplit('.', 1)[0] + '.json')
            convert_yaml_to_json(yaml_file, json_file)

