import pandas as pd
file = pd.read_excel('file.xlsx')
file1 = pd.read_excel('file1.xlsx')
difference = file[file!=file1]
print(difference)
