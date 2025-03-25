import re
import sys
import json

def parse_output(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    test_results = []
    pattern = r"(test_[^\s]+)\s+(PASSED|FAILED|SKIPPED|ERROR)"
    
    for match in re.finditer(pattern, content):
        name, status = match.groups()
        test_results.append({
            "name": name,
            "status": status
        })
    
    with open("test_results.json", "w") as out:
        json.dump({"tests": test_results}, out, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parser.py <test_output_file>")
    else:
        parse_output(sys.argv[1])
