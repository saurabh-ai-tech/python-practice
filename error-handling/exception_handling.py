# 1. The Basics: Input Validation
# Problem: Write a program that asks the user to input two numbers and divides the first by the second.

# Requirements:

# Handle ValueError if the user enters non-numeric text.

# Handle ZeroDivisionError if the second number is 0.

# Use an else block to print the result if no errors occurred.
"""try: 
    a = int(input("Enter the first no: "))
    b = int(input("Tnter the second no: "))

    result = a/b

except ValueError:
    print("Error: Please Numeric values.")

except ZeroDivisionError:
    print("Error: you can't divide no by zero")

else:
    print(result)"""

# 2. File Operations and Cleanup
# Problem: Create a script that attempts to read a file named data.txt.

# Requirements:

# Handle FileNotFoundError by printing a friendly message.

# Use a finally block to ensure that a "Cleanup complete" message prints regardless of whether the file was found or not.

# Bonus: Use a with statement and explain why it's often preferred over a manual try-finally for files.
"""
try: 
    with open("data-structure/list.py", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("Error: file not found")

finally:
    print("cleanup complete")"""










