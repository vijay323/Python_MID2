#Q5. Write a Python program using map(), filter(), and reduce() to find the sum of squares of even numbers. 

from functools import reduce 
 
nums = list(map(int, input("Enter numbers: ").split())) 
even_nums = list(filter(lambda x: x % 2 == 0, nums)) 
squares = list(map(lambda x: x ** 2, even_nums)) 
sum_squares = reduce(lambda x, y: x + y, squares) 
print("Sum of squares of even numbers:", sum_squares)
