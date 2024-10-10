import py_compile
import subprocess
import sys

def check_syntax(file_path):
    try:
        py_compile.compile(file_path, doraise=True)
        print(f"No syntax errors in {file_path}")
    except py_compile.PyCompileError as e:
        print(f"Syntax error in {file_path}: {e}")

def check_runtime(file_path):
    try:
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"No runtime errors in {file_path}")
        else:
            print(f"Runtime error in {file_path}:\n{result.stderr}")
    except Exception as e:
        print(f"Failed to run {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_syntax.py <file_path>")
    else:
        file_path = sys.argv[1]
        check_syntax(file_path)
        check_runtime(file_path)