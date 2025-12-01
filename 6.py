"""Q6. Create a user-defined module named math_utils with functions for prime checking, 
factorial, and Fibonacci generation. Import and use it in another program. """
def is_prime(n): 
    if n < 2: 
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            return False 
    return True 
 
def factorial(n): 
    if n == 0 or n == 1: 
        return 1 
    return n * factorial(n - 1) 
 
def fibonacci(n): 
    a, b = 0, 1 
    seq = [] 
    for _ in range(n): 
        seq.append(a) 
        a, b = b, a + b 
    return seq 
 
import math_utils as mu 
 
n = int(input("Enter number: ")) 
print("Prime check:", mu.is_prime(n)) 
print("Factorial:", mu.factorial(n)) 
print("Fibonacci:", mu.fibonacci(n)) 
