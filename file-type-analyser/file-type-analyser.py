
import argparse
from pathlib import Path
import sys

MB = 1024 ** 2

def size_format(size):
    """Format a file size in bytes to a readable string."""
    if size > MB:
        return f"{round(size / MB):>8} mb"
    return f"{size:>8,} bytes"

def extract_info(path):
    """Scan a directory and return file counts and sizes grouped by extension."""
    if not path.exists():
        print(f"Error: {path} doesn't exist")
        sys.exit(1)
    
    count_dict = {}

    for file in path.iterdir():

        if not file.is_file():
            continue

        size = file.stat().st_size

        suffix = file.suffix if file.suffix else "No extension"

        if suffix not in count_dict:
            count_dict[suffix] = {"count": 0, "size": 0}

        count_dict[suffix]['count'] += 1
        count_dict[suffix]['size'] += size

    return count_dict

def main():

    parser = argparse.ArgumentParser(description="Extract folder info based on suffix and size")
    parser.add_argument("--dir-path", required=True, type=Path, help="Enter path to directory")
    args = parser.parse_args()

    count_dict = extract_info(args.dir_path)

    if not count_dict:
        print("No data found")
        sys.exit(0)
    
    print(f"\nFile Type Report: {args.dir_path}")
    print("-" * 40)
    print(f"{'Extension':<13}{'Files':<10}{'Total Size'}")
    print("-" * 40)

   
    for suffix, data in sorted(count_dict.items(), key=lambda x: x[1]['count'], reverse=True):  
        if suffix == "No extension":
            continue      
        print(f"{suffix:<15}{data['count']:<6}{size_format(data['size'])}")

    if "No extension" in count_dict:
        data = count_dict['No extension']
        print(f"\n{'No extension':<15}{data['count']:<6}{size_format(data['size'])}")


if __name__ == "__main__":
    main()