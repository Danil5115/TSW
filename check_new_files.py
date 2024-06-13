import os
import ast
import sys

def is_valid_python_file(file_path):
    try:
        with open(file_path, "r") as file:
            tree = ast.parse(file.read(), filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return True
        return False
    except SyntaxError:
        return False

def check_new_files():
    new_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.py')]
    for file in new_files:
        if not is_valid_python_file(file):
            print(f"Error: {file} is not a valid Python file or does not contain any functions.")
            return 1
    print("All new Python files are valid.")
    return 0

if __name__ == "__main__":
    sys.exit(check_new_files())
