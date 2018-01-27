# to download multiple files from a data set, how to do so without selecting every link 
# using this example (https://www.50states.com/abbreviations.htm)

# install quandl for it

import quandl
import pandas as pd 

api_key = open('quandlapikey.txt', 'r').read() # api key would be written in this file

df=quandl.get('FMAC/HPI_AK', authtoken=api_key) # FMAC/HPI_AK is the quandl code on the above quandl website link
print(df.head())

# list of dataframes containing the US states
states= pd.read_html('https://www.50states.com/abbreviations.htm')

print(states) # prints all the dataframes

print(states[0]) # prints only 1st dataframe

print(states[0][1]) # prints 2nd column of 1st dataframe

for abbv in states[0][1][1:51]: # from 1st row to 50th row 
	print("FMAC/HPI_"+ str(abbv))