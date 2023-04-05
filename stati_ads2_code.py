# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:05:47 2023

@author: acer
"""
""" ASSIGNMENT 2 STATISTICS AND TRENDS"""


import pandas as pd


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

#reading data as csv file
evn_data = read_data("Environment_data.csv")