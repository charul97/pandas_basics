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
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

print(pd.merge(df1,df3, on='HPI'))

print(pd.merge(df1,df2, on=['HPI','Int_rate'])) # sharing on multiple columns

df4 = pd.merge(df1,df3, on='HPI')
df4.set_index('HPI', inplace=True)
print(df4)

df4 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df5 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

merged = pd.merge(df4,df5, on='Year') # leaves the uncommon years data
merged.set_index('Year', inplace=True)
print(merged)

# "how" is a parameter that reflects the merging choices that come from merging databases. You have the following choices: Left, right, outer, inner.
merged = pd.merge(df4,df5, on='Year', how='left') # takes data of 2002 but not 2005
merged.set_index('Year', inplace=True)
print(merged)

merged = pd.merge(df4,df5, on='Year', how='right') # takes data of 2005 but not 2002
merged.set_index('Year', inplace=True)
print(merged)

merged = pd.merge(df4,df5, on='Year', how='outer') # takes data of both 2002 and 2005
merged.set_index('Year', inplace=True)
print(merged)

merged = pd.merge(df4,df5, on='Year', how='inner') # neither takes data of 2002 nor 2005
merged.set_index('Year', inplace=True)
print(merged)


# join will join on the index
df4.set_index('Year', inplace=True)
df5.set_index('Year', inplace=True)
joined = df4.join(df5, how="outer")
print(joined)