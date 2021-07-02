import pandas as pd
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import os


def load_quotations(path):
# Load DataFrame
    os.chdir(path)
    quotations = pd.read_excel(path + '\\Fundamentus.xlsx')
    return quotations


def df_info(df):
    # Data Exploration
    print(df.columns.tolist())
    print(df.head())
    print(df.shape)
    print(df.info())


def quotations_cleanup(quotations):
    # Data Wrangling
    '''
        1. Drop subtotal row
        2. Replace decimal separators
        3. Convert percentages and objects to float numbers
    '''
    quotations.drop(len(quotations)-1, inplace = True)
    for c in quotations.loc[:, 'Cotação':'Vacância Média']:
        quotations.loc[:,c] = quotations.loc[:,c].astype(str)
        quotations.loc[:,c] = quotations.loc[:,c].str.replace('.','')
        quotations.loc[:,c] = quotations.loc[:,c].str.replace('%','').str.replace(',', '.')
        quotations.loc[:,c] = pd.to_numeric(quotations.loc[:, c])
    return quotations


def quotations_order(quotations):
    # Ordering
    '''
        1. High DY (> 4%) - Higher is better
        2. Market value descending
        3. High rentability ('Liquidez')
        4. P/VP (bet. 0.4 and 1.2) - Lower is better
        5. Lowest vacancy (< 30%) 
        6. Higher than inflation (4%, as pointed in topic 1)
    '''
    quotations.drop(quotations.loc[(quotations['Vacância Média'] > 30) |  \
        ((quotations['P/VP'] < 0.4) | (quotations['P/VP'] > 1.2)) \
        | (quotations['Dividend Yield'] < 4)].index, \
        inplace = True)
    quotations.sort_values(by = ['Valor de Mercado', 'Dividend Yield', 'Liquidez', 'P/VP', 'Vacância Média'], \
        ascending = [False, False, False, True, True], inplace = True)
    quotations.reset_index(drop = True, inplace = True)


def save_quotations(quotations_list, sheet_list, file_name):
    # Export to spreadsheet
    writer = pd.ExcelWriter(file_name, engine = 'xlsxwriter')
    for dataframe, sheet in zip(quotations_list, sheet_list):
        dataframe.to_excel(writer, sheet_name = sheet, startrow = 0 , startcol = 0)
    writer.save()
    return True


def quotations_plot(quotations):
    segments = quotations['Segmento'].value_counts().index
    data = list()
    for seg in segments:
        top = quotations.loc[quotations['Segmento'] == seg].reset_index(drop = True)
        data.append(top)
    return data


def load_brokers(path):
    brokers = pd.read_csv(path + "\\Brokers.csv")
    brokers["Valor"] = brokers["Valor"].str.replace('.', '').str.replace(',', '.')
    brokers["Valor"] = pd.to_numeric(brokers["Valor"])
    return brokers


def merge_tables(brokers, quotations):
    merged = brokers.merge(quotations, left_on = 'Titulo', right_on = 'Papel')
    gpby = merged.loc[:, ['Titulo', 'Valor']].groupby(['Titulo']).sum()
    merged = merged.merge(gpby, left_on = 'Titulo', right_on = 'Titulo')
    merged.rename(columns = {'Valor_x': 'Valor aplicado em corretora', 'Valor_y': 'Valor acumulado'}, inplace = True)
    merged.drop(columns = ['Papel'], inplace = True)
    merged['Shareof'] = round((merged['Valor acumulado'] / merged['Valor acumulado'].sum()) * 100, 2)
    merged.sort_values(by = ['Shareof'], ascending = False, inplace = True)
    merged = merged.reset_index(drop = True)
    merged.index = np.arange(1, len(merged)+1)
    return merged

def main():
    path = r'C:\Users\casoto\Documents\GitHub\portfolio\Personal Finances\Datasets'
    quotations = load_quotations(path)
    brokers = load_brokers(path)
    # df_info(quotations)
    # df_info(brokers)
    quotations = quotations_cleanup(quotations)
    merged = merge_tables(brokers, quotations)
    quotations_order(quotations)
    quotations_plot(quotations)
    data = quotations_plot(quotations)
    save_quotations(data, quotations['Segmento'].value_counts().index, 'fundamentus_manip.xlsx')
    return merged


merged = main()
print(merged[['Titulo', 'Valor acumulado', 'Shareof']])