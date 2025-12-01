#Q3. Write Python program that uses a recursive function to compute the factorial of a given 

non-negative integer 
def factorial(n): 
    if n == 0 or n == 1: 
        return 1 
    return n * factorial(n - 1) 
 
num = int(input("Enter a non-negative integer: ")) 
print("Factorial:", factorial(num))
