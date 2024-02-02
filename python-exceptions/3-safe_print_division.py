#!/usr/bin/python3
def safe_print_division(a, b):
    # Assume that a and b are integers
    try:
        # Try to divide a by b
        result = a / b
    except ZeroDivisionError:
        # Handle the case when b is zero
        result = None
    finally:
        # Print the result in the finally section
        print("Inside result:", result)
        # Return the result
        return result
