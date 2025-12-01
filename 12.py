"""Q12. Write a program that accepts a word from the user and displays all the line numbers in 
which that word occurs in a text file."""
word = input("Enter word to search: ") 
with open("input.txt", "r") as f: 
    lines = f.readlines() 
 
for i, line in enumerate(lines, start=1): 
    if word in line: 
        print(f"Found in line {i}: {line.strip()}")
