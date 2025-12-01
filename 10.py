"""Q10. Write a program to read a text file and count the frequency of each word, storing the 
result in another file """
file1 = open("input.txt", "r") 
text = file1.read().lower().split() 
file1.close() 
 
freq = {} 
for word in text: 
    freq[word] = freq.get(word, 0) + 1 
 
file2 = open("output.txt", "w") 
for word, count in freq.items(): 
    file2.write(f"{word}: {count}\n") 
file2.close() 
print("Word frequency written to output.txt") 
