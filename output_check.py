import pandas as pd
import numpy as np
import os

cwd = os.getcwd() # Get current working directory
print(cwd)
# DataFrame in pandas == Excel worksheet
path1 = os.path.join(cwd, "file3.csv")
path2 = os.path.join(cwd, "file4.csv")
#df1 = pd.read_csv(path1.read())
#df2 = pd.read_csv(path2.read())
df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)

print(df1.equals(df2))
#print(np.isClose(df1, df2))

diff_count = 0
columns = list(df1) # Create a list that holds the contents of each column
num_rows = len(df1.index) # Find the number of rows that each excel sheet has

for i in columns:
    for j in range(num_rows):
        if df1[i][j] != df2[i][j]: # compare sheet one to sheet two
            diff_count += 1
print(diff_count)

