# F-Secure FSK export file to Apple Password CSV compatible file mapper

A simple Python script to map passwords stored in a .fsk file (exported from F-Secure Password Vault) into a CSV format compatible with Apple’s password manager on macOS (introduced in Sequoia 15).

## Features:
 * Converts .fsk files to Apple’s Password CSV format.
 * Outputs a CSV file with the required fields: Title, URL, Username, Password, Notes, and OTPAuth.
 * Lightweight and easy to use.

## Prerequisites:
 * Python 3.7 or later installed on your system.
 * .fsk file exported from F-Secure Password Vault.

Installation:
1.	Clone this repository:

`git clone https://github.com/orby/fsk2csv.git`

`cd fsk2csv`

## Usage:

### Command-Line Interface:

Run the script with the input .fsk file and the desired output CSV file as arguments:

`python map-fsk-to-csv.py <input_file> <output_file>`

### Example:
`python fsk_to_csv.py passwords.fsk apple_passwords.csv`

### Input Format:

The .fsk file should follow the structure exported by F-Secure Password Vault. Here is an example of the expected JSON structure:

```json
{
  "data": {
    "unique_id": {
    "service": "example.com",
    "url": "https://example.com",
    "username": "user@example.com",
    "password": "mypassword123",
    "notes": "Some notes"
    }
  }
}
```

### Output Format:

#### The generated CSV file will have the following columns:
 * Title: The service name (e.g., example.com).
 * URL: The website URL.
 * Username: The username or email.
 * Password: The account password.
 * Notes: Additional notes (optional).
 * OTPAuth: Empty (optional field for one-time passwords).

#### Using in Apple Password Manager:
1.	Open the Passwords app on macOS.
2.	Go to File > Import Passwords.
3.	Select the generated CSV file.

License:

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing:

Feel free to submit issues or pull requests to improve the script. Contributions are always welcome!
