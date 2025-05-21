import json
import csv

def json_to_csv(json_string_data, csv_file_path):
    """
    Converts a JSON string containing a list of test scenario dictionaries to a CSV file.

    Args:
        json_string_data (str): The JSON string data.
        csv_file_path (str): The path to the output CSV file.
    """
    try:
        data = json.loads(json_string_data)

        # Ensure data is a list and not empty
        if not isinstance(data, list) or not data:
            print("Error: JSON data is not a list or is empty.")
            return

        headers = list(data[0].keys())

        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)

            writer.writeheader()

            for row_dict in data:
                writer.writerow(row_dict)

        print(f"Successfully converted JSON to CSV: {csv_file_path}")

    except json.JSONDecodeError:
        print("Error: Invalid JSON string provided.")
    except IOError:
        print(f"Error: Could not write to CSV file at {csv_file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
