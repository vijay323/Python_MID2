#Q13. Given a CSV file containing a single column of integers, write a program to count how many numbers are odd. 
import csv 
count = 0 
with open("numbers.csv", "r") as file: 
    reader = csv.reader(file) 
    for row in reader: 
        num = int(row[0]) 
        if num % 2 != 0: 
            count += 1 
print("Total odd numbers:", count)
