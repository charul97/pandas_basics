import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

# Append combines the rows of one dataframe to another dataframe.
# Concat can take a group of 2+ dataframes and combines the dataframes via the rows or columns.

concat = pd.concat([df1,df2])  # just rows being added
print(concat)

concat = pd.concat([df1,df2,df3]) # new columns also being added. NaN is shown for no value
print(concat)

df4 = df1.append(df2) # gives same output as concat[df1,df2] here
print(df4)

df4 = df1.append(df3) # gives same output as concat[df1,df3] here
print(df4)


s = pd.Series([80,2,50], index=['HPI','Int_rate','US_GDP_Thousands'])
df4 = df1.append(s, ignore_index=True)
print(df4)