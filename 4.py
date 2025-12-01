#Q4. Write Python program that uses a recursive function to find the digital sum of a given integer. 
def digital_sum(n): 
    if n < 10: 
        return n 
    return n % 10 + digital_sum(n // 10) 
 
num = int(input("Enter an integer: ")) 
print("Digital Sum:", digital_sum(num))
