import pandas as pd
import os

cwd = os.getcwd() # Get current working directory
print(cwd)
# DataFrame in pandas == Excel worksheet
path1 = os.path.join(cwd, "file1.xlsx")
path2 = os.path.join(cwd, "file2.xlsx")
df1 = pd.read_excel(path1)
df2 = pd.read_excel(path2)

print(df1.equals(df2))

diff_count = 0
columns = list(df1) # Create a list that holds the contents of each column
num_rows = len(df1.index) # Find the number of rows that each excel sheet has

for i in columns:
    for j in range(num_rows):
        if df1[i][j] != df2[i][j]: # compare sheet one to sheet two
            diff_count += 1
print(diff_count)
