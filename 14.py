"""Q14. Create a Python program to rename, copy, and delete a file using the os module. Ensure 
exception handling for file access errors""" 
import os 
import shutil 
 
try: 
    os.rename("input.txt", "renamed.txt") 
    shutil.copy("renamed.txt", "copy.txt") 
    os.remove("copy.txt") 
    print("File operations successful!") 
except FileNotFoundError: 
    print("File not found!") 
except Exception as e: 
    print("Error:", e)
