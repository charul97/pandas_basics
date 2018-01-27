import pandas as pd
import datetime
from pandas_datareader import data, wb   # instead of import pandas.io.data as web  (deprecated now) 
import matplotlib.pyplot as plt # for plotting graph
from matplotlib import style

start = datetime.datetime(2010, 1, 12)
end = datetime.datetime(2018, 1, 12)

df = data.DataReader("XOM", "yahoo", start, end) # This pulls data for Exxon from the Yahoo Finance API, storing the data to our df variable
print(df.head())  # since its gonna be large output so we are just printing first 5 output lines using head function

style.use('bmh')   # type of graph u want to plot
df['High'].plot()
plt.legend()
plt.show()