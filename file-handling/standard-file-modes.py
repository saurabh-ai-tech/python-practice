# 1. Solution 

import os

filename = "config_backup.txt"

# Remove file if it already exists from previous runs to test both paths
if os.path.exists(filename):
    os.remove(filename)

# First attempt: file does not exist -> succeeds
try:
    f = open(filename, "x")
    f.write("Initial config")
    f.close()
    print(f"Q1 - File '{filename}' created successfully.")
except FileExistsError:
    print(f"Q1 - Error: '{filename}' already exists!")

# Second attempt: file already exists -> raises FileExistsError
try:
    f = open(filename, "x")
    f.write("Overwriting attempt")
    f.close()
except FileExistsError:
    print(f"Q1 - Caught FileExistsError: Protected existing data from being overwritten.")


# 2. Solution 

