import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)

print(df.head())
print(df.tail())
print(df.tail(2)) # for printing last 2 lines of output
df.set_index('Day', inplace= True) # making day as index. inplace=True. What this does is allow us modify the dataframe "inplace," which means we actually modify the variable itself. Without inplace=True, we would need to do something like: df = df.set_index('Day')
style.use('fivethirtyeight')

print(df['Visitors']) # to reference a specific data item
df['Visitors'].plot() # plotting a single column
plt.show()


df.plot() # to plot all the columns
plt.show()

print(df[['Visitors','Bounce Rate']]) # to plot a list of columns
df[['Visitors','Bounce Rate']].plot()
plt.show()

