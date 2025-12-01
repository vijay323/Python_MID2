"""Q11. Write a program that reads a text file and replaces all occurrences of a given word with 
another word. Save the modified content into a new file."""

old = input("Word to replace: ") 
new = input("New word: ") 
 
with open("input.txt", "r") as f: 
    data = f.read().replace(old, new) 
 
with open("modified.txt", "w") as f: 
    f.write(data) 
 
print("Replacement done and saved in modified.txt")
