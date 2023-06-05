
#Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go

#Loading the data
dfkaj = pd.read_csv(f'dfclean.csv', sep=';')
#Creating a dataframe
dfkaj = pd.DataFrame(dfkaj)


#Loading the data
#cols = ['Product Progress','Logins','Start Date', 'Last Activity At', 'Days Lapsed','Months Lapsed']
#dfkaj = pd.read_csv('https://github.com/DataScience-Px/EDAPxStreamlit/blob/main/dfclean.csv', sep=';', encoding='utf-8', engine='python', 
 #                   on_bad_lines='skip', names=cols, header=0, decimal= '.', parse_dates=['Start Date', 'Last Activity At'], index_col='Unnamed: 0')
#Creating a dataframe
#dfkaj = pd.DataFrame(dfkaj)


#Erase outliers in the 'Logins' column
#dfloginskaj = dfkaj[(dfkaj['Logins'] > dfkaj['Logins'].quantile(0.05)) &
                             #  (dfkaj['Logins'] < dfkaj['Logins'].quantile(0.95))]



# Creating a sidebar
sidebar = st.sidebar.selectbox("Menu", ["Kajabi Progress Report", "EDEC", "...", "...."])

# Check the selected sidebar option
if sidebar == "Kajabi Progress Report":
   st.dataframe(dfkaj)