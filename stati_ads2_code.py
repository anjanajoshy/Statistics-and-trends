# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:05:47 2023

@author: acer
"""
""" ASSIGNMENT_2 STATISTICS AND TRENDS"""




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
                  45, 50, 55, 60, 65, 70, 75, 80, 85, 90])
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

def line_plot(data, title, x, y):
    '''
    

    Parameters
    ----------
    data : LINE PLOT
        
    title : 
        SETTING THE TITLE OF LINE GRAPH
    x :
        SETTING X-AXIS
    y : 
        SETTING Y-AXIS


    '''
    #setting line plot
    data.plot.line(figsize=(50, 30), fontsize=36, linewidth=6.0)
    #selecting yticks
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 100, 120, 140, 160])
    #setting title
    plt.title(title.upper(), fontsize=50, fontweight='bold')
    #labelling x axis of graph
    plt.xlabel(x, fontsize=50)
    #labelling y axis of graph
    plt.ylabel(y, fontsize=50)
    #setting legend and its fontsize
    plt.legend(fontsize=50)
    plt.savefig(title + '.png')
    plt.show()
    return

def stat_data(df_s, cns, value1, yr, a):
    '''
    

    Parameters
    ----------
    df_s : statistical table
        
    col : 
        Column name
    value : TYPE
        DESCRIPTION.
    yr : TYPE
        DESCRIPTION.
    a : TYPE
        DESCRIPTION.

    Returns
    -------
    df_stat : TYPE
        DESCRIPTION.

    '''
    #grouping datas for statistical table
    df_stat = df_s.groupby(cns, group_keys=True)
    df_stat = df_stat.get_group(value1)
    #resetting group
    df_stat = df_stat.reset_index()
    df_stat.set_index('Indicator Name', inplace=True)
    #cropping data  of table
    df_stat = df_stat.loc[:, yr]
    df_stat = df_stat.transpose()
    df_stat = df_stat.loc[:, a]
    return df_stat

def heat_map(data):
    '''
    

    Parameters
    ----------
    data : Data for plotting heatmap
    
    
    
    '''
    #setting heatmap to get the relation of datas
    plt.figure(figsize=(80,80))
    #setting title
    plt.title("Argentina".upper(), fontsize=70)
    sns.heatmap(data.corr(), annot=True, annot_kws = {"size":40})
    plt.xticks(rotation = 90, horizontalalignment = "center", fontsize = 70)
    plt.yticks(rotation = 0,fontsize=70)
    plt.savefig('heatmap_ar.png')
    plt.show()
    return data

#listing countries for bar plot
country1 = ['Kenya', 'Japan', 'Denmark', 'Albania', 'Iraq', 'Brazil', 'China']
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

#calling function to filter data for bar plot2
b_p21, b_p22 = filter_data(
    evn_data, 'Indicator Name', 'Annual freshwater withdrawals, agriculture (% of total freshwater withdrawal)', country1, year1)
print(b_p21)
print(b_p22)
bar_plot(b_p21, 'Annual freshwater withdrawals,agriculture',
         'Countries', 'total freshwater withdrawal')

#listing countries for line plot
country2 = ['Chile', 'Peru', 'Vietnam', 'Nepal', 'India','Bulgaria','Angola']
#listing year 
year2 = ['2000', '2002', '2004', '2006', '2008']

#calling function to filter data for line plot1
l_p11, l_p12 = filter_data(
    evn_data, 'Indicator Name', 'Access to electricity (% of population)', country2, year2)
print(l_p11)
print(l_p12)
line_plot(l_p12, 'Access to electricity', 'Year', 'percentage of population')

#calling function ti filter data for line plot2
l_p21, l_p22 = filter_data(
    evn_data, 'Indicator Name', 'Electricity production from oil, gas and coal sources (% of total)', country2, year2)
print(l_p21)
print(l_p22)
line_plot(l_p22, 'Electricity production from oil, gas and coal',
          'Year', '% of total sorces')

#listing year for heat map
year3 = ['1990', '1995', '2000', '2005', '2010']
#listing indicator name to create heatmap
indi_h = ['Agricultural land (% of land area)', 'Annual freshwater withdrawals, agriculture (% of total freshwater withdrawal)', 'Access to electricity (% of population)',
       'Electricity production from oil, gas and coal sources (% of total)', 'Methane emissions (% change from 1990)', 'Renewable electricity output (% of total electricity output)']
statd = stat_data(evn_data, 'Country Name', 'Argentina', year3, indi_h)
print(statd.head())
heat_map(statd)