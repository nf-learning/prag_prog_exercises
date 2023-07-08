import sys
import yaml
import json

def convert_yaml_to_json(yaml_file, json_file):
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    with open(json_file, 'w') as file:
        json.dump(yaml_data, file, indent=4)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python yaml_to_json.py <input_yaml_file> <output_json_file>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    json_file = sys.argv[2]

    convert_yaml_to_json(yaml_file, json_file)
