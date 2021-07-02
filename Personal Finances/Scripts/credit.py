import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import re
import os


# Change Directory
path = r'C:\Users\casoto\Documents\GitHub\portfolio\Personal Finances\Datasets'
os.chdir(path)
history = pd.DataFrame()


# Concatenate credit card buy history
for file in os.listdir():
    with open(file) as fp:
        content = fp.readlines()
        for e in list(enumerate(content)):
            if e[0] == 4:
                period = e[1]
                period = period.split('FECHADO ')[1].replace('\n', '')
            if 'Total da Fatura em Real' in e[1]:
                d = e[0] - 7
    df = pd.read_csv(file, sep = ';', skiprows = 4, nrows = d, encoding = 'ANSI')
    df['Periodo'] = period
    history = pd.concat([df,history])


# Data wrangling
history.drop(['US$'], axis = 1, inplace = True)
history = history.loc[(~history['Histórico'].str.contains('SALDO ANTERIOR')) & \
        (~history['Histórico'].str.contains('PAGTO. POR DEB EM C/C')) & \
        (~history['Histórico'].str.contains('Total para JOAO C C JUNIOR'))]
history['R$'] = history['R$'].str.replace('.','').str.replace(',', '.')
history['R$'] = pd.to_numeric(history['R$'])
history['Data'] = pd.to_datetime(history['Data'], format='%d/%m').dt.strftime('%d/%m')
history['Periodo'] = pd.to_datetime(history['Periodo'], format='%d/%m/%Y')
history.sort_values(by = 'Periodo', ascending = False, inplace = True)


# Group and separate by period
gp = history.groupby(['Histórico', 'Periodo']).sum()
gp.sort_values(by = 'R$', ascending = False, inplace = True)
periods = history['Periodo'].value_counts().index
topmost = dict()
for period in periods:
    topmost = history.loc[history['Periodo'] == period].groupby(['Histórico']).sum().sort_values(by = 'R$', ascending = False)
    print(topmost)