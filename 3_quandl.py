import pandas as pd
df = pd.read_csv('/home/charul/pandas/ZILLOW-N8628_MLPFAH.csv')
print(df.head())

df.set_index('Date', inplace= True) # setting Date as index
df.to_csv('/home/charul/pandas/newfile.csv') # saving the file after creating Date as index to csv
df= pd.read_csv('/home/charul/pandas/newfile.csv') # raeding the newly created csv file 
print(df.head()) # but this prints the same output as earlier i.e., no index as Date. This is because csv files have no attribute as index.

df = pd.read_csv('/home/charul/pandas/newfile.csv', index_col=0) # to define first column as index
print(df.head())

# to rename the column
df.columns = ['Pricing']
print(df.head())
# OR
df.rename(columns={'Pricing':'Priced_Value'}, inplace=True)
print(df.head())

# saving the file now
df.to_csv('/home/charul/pandas/newfile2.csv')

# for no headers in the file
df.to_csv('/home/charul/pandas/newfile3.csv', header=False) 

# converting the file to various different formats like html, xls, etc.
df.to_html('/home/charul/pandas/example.html')