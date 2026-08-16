# 1. Solution

filename = "international.txt"
content = "Café ☕"

# Write UTF-8 data
with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

# 1. errors='strict' (Default behavior) -> raises UnicodeDecodeError
try:
    with open(filename, "r", encoding="ascii", errors="strict") as f:
        print(f.read())
except UnicodeDecodeError as e:
    print(f"Q1 - Strict decoding error: {e}")