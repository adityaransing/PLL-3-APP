import csv
import json

def read_csv(input_file):
    with open(input_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_json(output_file, data):
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)

def convert_csv_to_json(input_file, output_file):
    data = read_csv(input_file)
    write_json(output_file, data)

if __name__ == "__main__":
    input_file = "students.csv"
    output_file = "students.json"

    convert_csv_to_json(input_file, output_file)

    print("CSV data successfully converted to JSON.")
    print("JSON file created:", output_file)