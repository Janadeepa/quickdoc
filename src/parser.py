import os
import re

def parse_comments(input_directory):
    comments = []
    # Example for Python
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    source_code = f.read()
                    pattern = r'#\s*(.*?)\n'
                    comments += re.findall(pattern, source_code, re.DOTALL)
    return comments
