# 1. Solution

file = open("welcome.txt", 'w')

file.write("Hello, Python File I/O!")
file.close()

print(f"Q1 - Is file closed? {file.closed}")  # Output: True


# 2. Solution 

data = open("welcome.txt", "r")

print(data.read())

data.close()

print(f"is this file closed : {data.closed}")



# 3. Solution

def safe_write(filepath: str, content: str) -> None:
    f = open(filepath, "w")
    try:
        f.write(content)
    finally:
        f.close()
        print(f"Q3 - File safely closed in finally block: {f.closed}")

safe_write("safe_test.txt", "Critical data written safely.")



# 4. Solution

from pathlib import Path

abs_path = Path("app_log.txt").resolve()
print(f"Absolute Path: {abs_path}")

file = open(abs_path, "w")
file.write("Log started.")
file.close()


# 5. Solution 

f = open("descriptor_test.txt", "w")
fd = f.fileno()
print(f"Q5 - OS File Descriptor integer: {fd}")
f.close()

# Attempting operations on a closed file
try:
    f.fileno()
except ValueError as e:
    print(f"Q5 - Expected error after close: {e}")