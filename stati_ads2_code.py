# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:05:47 2023

@author: acer
"""
""" ASSIGNMENT_2 STATISTICS AND TRENDS"""




import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename):
    df = pd.read_csv(filename, skiprows=4)
    return df


def filter_data(dt, cn, value, conty, yr):
    '''
    filtering dataframe

    Parameters
    ----------
    dt : dataset
    cn : Column name
    value : Given values
    conty : Countries taken from dataframe
    yr : Years taken from dataframe

    Returns
    -------
    df_f : Dataframe taken as df_f
    df_tran : Transposed data is stored as df_tran
        

    '''
    #grouping datas to filter
    df_f = dt.groupby(cn, group_keys=True)
    df_f = df_f.get_group(value)
    #reseting index of dataframe
    df_f = df_f.reset_index()
    #setting index as Country Name
    df_f.set_index('Country Name', inplace=True)
    #cropping datas
    df_f = df_f.loc[:, yr]
    df_f = df_f.loc[conty, :]
    #dropping some values from data
    df_f = df_f.dropna(axis=1)
    df_f = df_f.reset_index()
    #transposing data and storing as df_tran
    df_tran = df_f.set_index('Country Name')
    df_tran = df_tran.transpose()
    return df_f, df_tran

def bar_plot(data, title, x, y):
    '''
    

    Parameters
    ----------
    data : Bar plot
        
    title :
        Setting the title of bar graph
    x : 
        SETTING THE X-AXIS
    y : 
        SETTING THE Y-AXIS


    '''
    #setting bar plot
    ax = data.plot.bar(x='Country Name', rot=0, figsize=(50, 30), fontsize=50)
    #Setting the yticks to plot the graph
    ax.set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40,
                  45, 50, 55, 60, 65, 70, 75, 80])
    #Setting the title of graph and fontsize
    ax.set_title(title.upper(), fontsize=50, fontweight='bold')
    #Setting x label
    ax.set_xlabel(x, fontsize=50)
    #Setting y label
    ax.set_ylabel(y, fontsize=50)
    #Setting the size of legend
    ax.legend(fontsize=50)
    #Saving figure as png form
    plt.savefig(title + '.png')
    plt.show()
    return

#listing countries for bar plot
country1 = ['Kenya', 'Japan', 'Denmark', 'Albania', 'Iraq','Brazil','China']
#listing years
year1 = ['2000', '2005', '2010', '2015']
#reading data as csv file
evn_data = read_data("Environment_data.csv")

#calling function to filter data for bar plot1
b_p11, b_p12 = filter_data(
    evn_data, 'Indicator Name', 'Agricultural land (% of land area)', country1, year1)
print(b_p11)
print(b_p12)
bar_plot(b_p11, 'Agricultural land', 'Countries', 'Percentage of land area')