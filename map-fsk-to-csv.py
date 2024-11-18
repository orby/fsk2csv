import json
import csv
from typing import Dict, Any

def fsk_to_csv(input_file: str, output_file: str) -> None:
    """
    Convert a .fsk file to Apple's Password CSV format.

    Parameters:
    - input_file (str): Path to the input .fsk JSON file.
    - output_file (str): Path to the output CSV file.

    Returns:
    - None
    """
    # Read the .fsk JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        fsk_data: Dict[str, Any] = json.load(f)

    # Extract the relevant password data
    passwords = fsk_data.get('data', {})

    # Prepare the CSV output
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'URL', 'Username', 'Password', 'Notes', 'OTPAuth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry_id, entry in passwords.items():
            writer.writerow({
                'Title': entry.get('service', ''),
                'URL': entry.get('url', ''),
                'Username': entry.get('username', ''),
                'Password': entry.get('password', ''),
                'Notes': entry.get('notes', ''),
                'OTPAuth': ''  # Optional field, left empty
            })

    print(f"Conversion complete! CSV saved as: {output_file}")

if __name__ == "__main__":
    # Example usage
    import argparse

    parser = argparse.ArgumentParser(description="Convert a .fsk file to Apple's Password CSV format.")
    parser.add_argument("input_file", help="Path to the input .fsk file")
    parser.add_argument("output_file", help="Path to the output CSV file")

    args = parser.parse_args()
    fsk_to_csv(args.input_file, args.output_file)
