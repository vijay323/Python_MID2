"""Q15. Write a Python program that takes user input for two numbers and performs di vision. 
Handle exceptions for invalid input, divide by zero, and unexpected errors gracefully.""" 
def safe_division(): 
    try: 
        a = input("Enter numerator: ").strip() 
        b = input("Enter denominator: ").strip() 
        num = float(a) 
        den = float(b) 
        result = num / den 
    except ValueError: 
        print("Error: Invalid numeric input. Please enter valid numbers.") 
    except ZeroDivisionError: 
        print("Error: Division by zero is not allowed.") 
    except Exception as e: 
        print("Unexpected error:", type(e).__name__, "-", e) 
    else: 
        print(f"Result: {result}") 
 
if __name__ == "__main__": 
    safe_division()
