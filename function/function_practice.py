"""
Python Functions — 10 Practice Problems
=======================================
Instructions:
Implement the empty functions/tasks below based on each problem description.
"""

# ==============================================================================
# Problem 1: User Profile Function
# ==============================================================================
# Practice: Defining functions, positional arguments, return values.
# Task: Create a function that accepts a user's name, age, and email,
#       and returns a formatted profile string or dictionary.

def create_user_profile(name, age, email):
    return f"Name: {name}, Age: {age}, email: {email}"


# ==============================================================================
# Problem 2: Flexible Greeting Function
# ==============================================================================
# Practice: Positional arguments, keyword arguments, default arguments.
# Task: Create a greet_user() function where the user can provide the name
#       as either a positional or keyword argument, with a default greeting.

def greet_user(name, greeting="Hello"):
    return f"{greeting} {name}, How are you doing?"

# ==============================================================================
# Problem 3: Calculator with *args
# ==============================================================================
# Practice: *args, returning multiple values.
# Task: Create a function that accepts any number of numbers and returns
#       their sum, average, minimum, and maximum.

#==============================================================================
# Problem 4: User Settings with **kwargs
# ==============================================================================
# Practice: **kwargs, dictionaries, reusable functions.
# Task: Create a function that accepts a username and any number of settings
#       such as theme, language, notifications, and timezone, then returns
#       the settings as a dictionary.

 
def configure_user_settings(username, **settings):
    """
    Combines username with any arbitrary key-value configuration settings.
    """
    user_config = {
        "username": username,
        "settings": settings
    }
    return user_config

# Test Problem 4:
print("--- Problem 4 ---")
config = configure_user_settings(
    "dev_sarah",
    theme="dark",
    language="en_US",
    notifications=True,
    timezone="Asia/Kolkata"
)
print("Configured Settings:", config)
print()


# ==============================================================================
# Problem 5: Text Processing Pipeline
# ==============================================================================
# Practice: Small reusable functions, functions calling other functions.
# Task: Create separate functions to clean text, remove extra spaces,
#       convert it to lowercase, and count words. Create another function
#       that calls all of them in a pipeline.

def remove_extra_spaces(text):
    return " ".join(text.split())

def to_lowercase(text):
    return text.lower()

def count_words(text):
    if not text.strip():
        return 0
    return len(text.split())

def text_processing_pipeline(text):
    pass

print(remove_extra_spaces("saurabh skdfjdla gjd. ... "))
# ==============================================================================
# Problem 6: Order Price Calculator
# ==============================================================================
# Practice: Function composition, arguments, return values.
# Task: Create functions for calculating item subtotal, discount, tax,
#       and final price. Create one main function that calls the other functions.

def calculate_subtotal(items):
    """Calculates sum total of items where each item is a dict with price & qty."""
    return sum(item["price"] * item["quantity"] for item in items)

def calculate_discount(subtotal, discount_percent):
    """Calculates discount amount."""
    return subtotal * (discount_percent / 100)

def calculate_tax(taxable_amount, tax_percent):
    """Calculates tax on an amount."""
    return taxable_amount * (tax_percent / 100)

def calculate_final_order_price(items, discount_percent=0.0, tax_percent=5.0):
    """
    Main function combining subtotal, discount deduction, and tax addition.
    """
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, discount_percent)
    taxable_amount = subtotal - discount
    tax = calculate_tax(taxable_amount, tax_percent)
    final_total = taxable_amount + tax

    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "final_total": round(final_total, 2)
    }

# ==============================================================================
# Problem 7: Local vs Global Settings
# ==============================================================================
# Practice: Scope, local variables, global variables.
# Task: Create a program with a global application setting and a function
#       that has a local setting with the same name. Experiment with changing
#       and reading both.

APP_SETTING = "GLOBAL_PRODUCTION_MODE"

APP_MODE = "PRODUCTION"  # Global variable

def demonstrate_scope():
    """
    Demonstrates local shadowing of a global variable and explicit global modification.
    """
    # 1. Local variable shadowing global variable with same name
    APP_MODE = "DEVELOPMENT_LOCAL"
    print(f"Inside function (Local APP_MODE): {APP_MODE}")

def update_global_mode(new_mode):
    """Modifies the global APP_MODE explicitly."""
    global APP_MODE
    APP_MODE = new_mode


# ==============================================================================
# Problem 8: Function Factory
# ==============================================================================
# Practice: Functions returning functions, closures, scope.
# Task: Create a function that accepts a percentage and returns another
#       function that applies that percentage as a discount.

def discount_factory(percentage):
    pass


# ==============================================================================
# Problem 9: Lambda Data Processor
# ==============================================================================
# Practice: Lambda functions, sorting, filtering.
# Task: Given a list of products containing names and prices, use lambda
#       functions to sort products by price and identify/filter expensive products.

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 300},
    {"name": "Keyboard", "price": 75},
]

def process_product_data(product_list, expensive_threshold=100):
    pass


# ==============================================================================
# Problem 10: Mini Utility Library
# ==============================================================================
# Practice: Functions + modules + reusable code.
# Task: Create reusable functions for:
#       - validating email
#       - calculating price
#       - formatting names
#       - counting words
#       - checking passwords
# (Note: In your actual project, save these in a module like `utilities.py`
#  and import them into a `main.py` file to test).

def validate_email(email):
    pass

def calculate_price(unit_price, quantity, tax_rate=0.0):
    pass

def format_name(first_name, last_name):
    pass

def count_words_util(text):
    pass

def check_password_strength(password):
    pass