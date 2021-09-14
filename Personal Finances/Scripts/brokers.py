import pandas as pd
import os

# Change wd
path = r'C:\Users\casoto\Documents\GitHub\portfolio\Personal Finances\Datasets'
os.chdir(path)

# Read csv data
brokers = pd.read_csv(path + '\\Brokers.csv', sep = ',')
brokers['Valor'] = pd.to_numeric(brokers['Valor'].str.replace('.', '').str.replace(',', '.'))

# Group by value and add shareoff
gpby = brokers.groupby(['Titulo']).sum()
gpby['Shareof'] = (gpby['Valor'] / gpby['Valor'].sum()) * 100
gpby.sort_values(by = ['Shareof'], ascending = False, inplace = True)
gpby['Shareof'] = pd.Series(["{0:.2f}%".format(val) for val in gpby['Shareof']], index = gpby.index)

gpby