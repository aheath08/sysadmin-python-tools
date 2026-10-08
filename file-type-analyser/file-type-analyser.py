
import argparse
from pathlib import Path
import sys

MB = 1024 ** 2
GB = 1024 ** 3

def size_format(size):
    """Format a file size in bytes to a readable string."""
    if size > GB:
        return f"{round(size / GB):>8} GB"
    elif size > MB:
        return f"{round(size / MB):>8} MB"
    else:
        return f"{size:>8} bytes"

def extract_info_file(path):
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

def extract_info_dir(path):
    """Scan a directory and return folder sizes, total size and folder count."""
    if not path.exists():
        print(f"Error: {path} doesn't exist")
        sys.exit(1)

    count_dict = {}

    for folder in path.iterdir():

        if not folder.is_dir():
            continue

        dir_size = sum(f.stat().st_size for f in folder.rglob("*") if f.is_file())

        count_dict[folder.name] = {"size": dir_size}

    return count_dict

def main():

    parser = argparse.ArgumentParser(description="Analyse directory contents by file type or folder size")
    parser.add_argument("--dir-path", required=True, type=Path, help="Enter path to directory")
    parser.add_argument("--folders-only", action="store_true", help="Use flag if you want to see folder info only")
    args = parser.parse_args()

    if not args.folders_only:

        count_dict = extract_info_file(args.dir_path)

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
        print("-" * 40)

        if "No extension" in count_dict:
            data = count_dict['No extension']
            print(f"{'No extension':<15}{data['count']:<6}{size_format(data['size'])}")
    
    else:

        count_dict = extract_info_dir(args.dir_path)

        if not count_dict:
            print("No data found")
            sys.exit(0)
        
        print(f"Folder Size Report: {args.dir_path}")
        print("-" * 35)
        print(f"{'Folder':<12} {'Size':>11}")
        print("-" * 35)

        total_size = 0

        for folder, info in sorted(count_dict.items(), key=lambda x: x[1]['size'], reverse=True):
            print(f"{folder:<12} {size_format(info['size'])}")
            total_size += info['size']
        
        print("-" * 35)
        print(f"{'Total:':<12} {size_format(total_size)}")
        print(f"{len(count_dict)} Folders")
        

if __name__ == "__main__":
    main()