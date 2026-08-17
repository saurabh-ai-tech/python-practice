# 1. Solution

log_file = "server.log"
log_content = (
    "[INFO] Server started\n"
    "[DEBUG] Connecting to database\n"
    "[ERROR] Database connection failed\n"
    "[INFO] Retrying connection\n"
)

with open(log_file, "w", encoding="utf-8") as f:
    f.write(log_content)


print("--- 1. Using readline() in a loop ---")
with open(log_file, "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if line == "":  # EOF indicator
            break
        print(f"Readline: {line.strip()}")



# 2. Solution 
text_file = "large_text.txt"

with open(text_file, "w", encoding="utf-8") as f:
    f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def process_in_chunks(filepath: str, chunk_size: int = 5):
    chunk_count = 0
    print(f"\n--- Reading in fixed chunks of {chunk_size} characters ---")
    
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:  # An empty string signals EOF
                break
            chunk_count += 1
            print(f"Chunk {chunk_count}: '{chunk}'")
            
    print(f"Total chunks processed: {chunk_count}")

process_in_chunks(text_file, chunk_size=5)


# 3. Solution
tasks = ["Buy groceries", "Pay electric bill", "Schedule doctor appointment"]

# 1. The trap: writelines() does NOT append newlines automatically
with open("tasks_raw.txt", "w", encoding="utf-8") as f:
    f.writelines(tasks)

with open("tasks_raw.txt", "r", encoding="utf-8") as f:
    print("Q1 - Raw writelines (no newlines):")
    print(f"'{f.read()}'")
    # Output: 'Buy groceriesPay electric billSchedule doctor appointment'


# 2. Correct usage: Append '\n' to each item
formatted_tasks = [task + "\n" for task in tasks]

with open("tasks_formatted.txt", "w", encoding="utf-8") as f:
    f.writelines(formatted_tasks)

with open("tasks_formatted.txt", "r", encoding="utf-8") as f:
    print("\nQ1 - Formatted writelines (with explicit newlines):")
    print(f.read())