from pathlib import Path

DIR_PATH = Path(__file__).parent
FILE_PATH = DIR_PATH/"ip.txt"

def read_file(file):
    """Read a text file and return its lines as a list.
    Returns None if the file doesn't exist."""
    try:
        with open(file)as f:
            return f.readlines()
    except FileNotFoundError as e:
        print(f"File not found, {e}")

def is_valid_cidr(ip):
    """Validates the CIDR block:
    checks if there are exactly 4 parts when split and validates if each part is a digit and between 0 - 255"""

    parts = ip.split(".")
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        if int(part) >255:
            return False
    return True

def is_valid_prefix(prefix):
    """Confirms that the prefix is also valid. Needs to be a number between 0 - 32"""

    if prefix.isdigit():
        return int(prefix) < 33
    else:
        return False

def main():
    """Read IP/CIDR entries from a file, validate each one, and report
    any that are invalid.

    Handles two formats: a bare IP address (e.g. 192.168.1.1), and a
    full CIDR block (e.g. 10.0.0.0/24). For CIDR entries, both the IP
    portion and the prefix length are validated independently.
    """

    data = read_file(FILE_PATH)
    invalid = []

    for line in data:
       
        valid = True
        if "/" in line:
            ip, prefix = line.split("/")
            if not is_valid_prefix(prefix.strip()):
                valid = False
            if not is_valid_cidr(ip.strip()):
                valid = False

        else:
            if not is_valid_cidr(line.strip()):
                valid = False

        if not valid:
            invalid.append(line)


    if invalid:
        print(f"\n⚠️ Invalid IP(s)")
        for x in invalid:
            print(f"    - {x.strip()}")
    else:
        print(f"✅ All IP(s) Valid")

if __name__ == "__main__":
    main()