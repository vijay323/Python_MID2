"""Q2. Write a Python program to accept a list of integers and perform the following:
• Remove duplicates 
• Sort in ascending and descending order 
• Display the second largest and smallest element """

nums = list(map(int, input("Enter integers separated by space: ").split())) 
 
nums = list(set(nums)) 
print("After removing duplicates:", nums) 
 
asc = sorted(nums) 
desc = sorted(nums, reverse=True) 
print("Ascending:", asc) 
print("Descending:", desc) 
 
if len(nums) >= 2: 
    print("Second smallest:", asc[1]) 
    print("Second largest:", desc[1]) 
else: 
    print("Not enough elements") 
