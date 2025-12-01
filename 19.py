"""Q19. Write a program to create a NumPy 2D array, compute row-wise and column wise sums, 
and convert it to a Pandas DataFrame for further processing (e.g., normalization)."""
import numpy as np 
import pandas as pd 
 
# create a sample 2D numpy array 
arr = np.array([[10, 20, 30], 
                [5, 15, 25], 
                [2, 4, 6]]) 
 
# row-wise sums and column-wise sums 
row_sums = arr.sum(axis=1) 
col_sums = arr.sum(axis=0) 
 
print("Array:\n", arr) 
print("Row sums:", row_sums) 
print("Column sums:", col_sums) 
 
# convert to pandas DataFrame 
df = pd.DataFrame(arr, columns=["C1", "C2", "C3"]) 
print("\nDataFrame:\n", df) 
 
# simple min-max normalization (per column) 
normalized = (df - df.min()) / (df.max() - df.min()) 
print("\nNormalized DataFrame:\n", normalized) 
