# 1. Solution 

with open("log.txt", "w") as f:
    f. write("Session started.\n")


print(f"file is closed: {f.closed}")


# 2. Solution 
file_ref = None
try:
    with open("critical_data.txt", "w") as f:
        file_ref = f
        f.write("Checkpoint 1\n")
        # Simulate unexpected crash mid-write
        raise RuntimeError("Simulated database/write failure!")
except RuntimeError as err:
    print(f"Q2 - Caught expected exception: {err}")

# Even though an exception occurred, the file was closed safely before handling the error
print(f"Q2 - Is file closed after runtime exception? {file_ref.closed}")  # Output: True