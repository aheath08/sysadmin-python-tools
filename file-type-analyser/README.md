# File Type Analyser

A sysadmin tool written in python that scans a given directory for files and prints report on type (based on extension) and file size.

## Project Structure
```
file-type-analyser/
├── file-type-analyser.py
├── test-files/
│   └── (sample files covering multiple extensions
│        plus extensionless files, for quick testing)
└── README.md
```

## Features
- Counts files grouped by extension
- Calculates total size per extension (bytes/MB)
- Files with no extension grouped separately and listed last
- Sorted by file count, highest first
- Handles edge cases: empty directories, directories with only 
  extensionless files, and directories with only extensioned files

## Example Usage 
Takes a CLI arguement for the directory path and analyses specified folder. Project contains a `test-files`. This contains some demo files to demonstrate the output. Includes a README file with no extension purposefully to show the `No extension` feature.

```bash
python3 file-type-analyser.py --dir-path test-files
```
Otherwise can use path to local folder:
```bash
python3 file-type-analyser.py --dir-path path/to/dir
```

## Note on test data
Files in `test-files/` use placeholder text content for simplicity — the `.jpg`, `.png`, and `.zip` files are not real binary files, just plain text with those extensions. This is sufficient for testing extension grouping and size reporting, which is all this tool checks.

## Example Output
```text
File Type Report: /Users/Desktop/python_test_files
----------------------------------------
Extension    Files     Total Size
----------------------------------------
.wav           7          109 mb
.txt           3          554 bytes
.json          3        2,030 bytes
.log           2           78 bytes
.pdf           1      229,633 bytes

No extension   1        6,148 bytes
```

## Requirements
- python3
- Standard libraries only

