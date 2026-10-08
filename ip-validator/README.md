# IP Validator 
A sysadmin python script takes a `.txt` file of IP addresses which can include the CIDR netmask and validates whether the IP address and, if present, the CIDR prefix are both correctly formatted. Any invalid IP addresses are flagged in the report.

## Project Structure 
```
ip-validator/
├── ip-validator.py
├── ip.txt
└── README.md
```

## Usage 
There is a test file of various IP addresses that can be used to test locally. The test `.txt` file needs to be in the same parent folder as the .py script as per the project structure above.

``` bash
python3 ip-validator.py
```

## What Counts as Valid
- IP address: exactly 4 dot-separated numbers, each 0-255
- CIDR prefix (optional, e.g. `/24`): a number between 0-32


## Example Output
``` text
⚠️ Invalid IP(s)
    - 256.1.1.1
    - 192.168.1
    - 10.0.0.5/33
    - 999.999.999.999/24
```

