"""Q1. Write a program to generate and display the first n Fibonacci numbers using a for loop and 
while loop separately."""

n = int(input("Enter number of terms: ")) 
 
# Using for loop 
a, b = 0, 1 
print("Fibonacci using for loop:") 
for i in range(n): 
    print(a, end=" ") 
    a, b = b, a + b 
 
# Using while loop 
print("\nFibonacci using while loop:") 
a, b, i = 0, 1, 0 
while i < n: 
    print(a, end=" ") 
    a, b = b, a + b 
    i += 1
