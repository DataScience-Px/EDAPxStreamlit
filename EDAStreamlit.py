
#Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go

#Loading the data
dfkaj = pd.read_csv(f'dfkaj_proc.csv', sep=';')
#Creating a dataframe
dfkaj = pd.DataFrame(dfkaj)


#Erase outliers in the 'Logins' column
dfloginskaj = dfkaj[(dfkaj['Logins'] > dfkaj['Logins'].quantile(0.05)) &
                     (dfkaj['Logins'] < dfkaj['Logins'].quantile(0.95))]



# Creating a sidebar
sidebar = st.sidebar.selectbox("Menu", ["Kajabi Progress Report", "EDEC", "...", "...."])

# Check the selected sidebar option
if sidebar == "Kajabi Progress Report":
   st.dataframe(dfkaj)