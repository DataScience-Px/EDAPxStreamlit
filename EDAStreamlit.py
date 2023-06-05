
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

    st.title("Kajabi Progress Report")
    st.dataframe(dfkaj)
    # Create scatter plot
    fig = go.Figure(data=go.Scatter(x=dfloginskaj['Logins'],
                                   y=dfloginskaj['Product Progress'],
                                   mode='markers',
                                   marker=dict(color='rgba(29, 123, 138, 0.8)'),
                                   opacity=0.7))

   
    # Add title annotation
    fig.update_layout(
        title=dict(
            text='<b>Correlation between Logins and Product Progress</b>',
            x=0.5,
            y=0.9,
            xanchor='center',
            yanchor='top',
            font=dict(family='Raleway',
                      size=18,
                      color='rgb(37, 37, 37)')
        ),
        font=dict(family='Raleway', size=12, color='rgb(64, 64, 64)'),
        width=800,  # Adjust the width of the plot
        height=600,  # Adjust the height of the plot
    )

    # Set x-axis label
    fig.update_xaxes(title=dict(text='Logins', font=dict(family='Raleway', size=14)))

    # Set y-axis label
    fig.update_yaxes(title=dict(text='Product Progress', font=dict(family='Raleway', size=14)))

    # Display the plot in Streamlit sidebar
    st.plotly_chart(fig)
    
    #Plot a second graph
    fig = go.Figure(data=go.Scatter(x=dfloginskaj['Logins'],
                               y=dfloginskaj['Months Lapsed'],
                               mode='markers',
                               marker=dict(color='rgba(29, 123, 138, 0.8)'),  # Green color
                               opacity=0.7))

    # Update layout
    fig.update_layout(
        title=dict(
            text='<b>Correlation between Logins and Months Lapsed</b>',
            x=0.5,
            y=0.9,
            xanchor='center',
            yanchor='top',
            font=dict(family='Raleway',
                    size=18,
                    color='rgb(37, 37, 37)')
        ),
        font=dict(family='Raleway', size=12, color='rgb(64, 64, 64)'),
        xaxis=dict(title='Logins', title_font=dict(family='Raleway', size=14)),
        yaxis=dict(title='Months Lapsed', title_font=dict(family='Raleway', size=14)),
        width=800,  # Adjust the width of the plot
        height=600,  # Adjust the height of the plot
    )

    # Display the plot
    st.plotly_chart(fig)

    #Plot a third graph
    fig = go.Figure(data=go.Scatter(
    x=dfloginskaj['Logins'],
    y=dfloginskaj['Months Lapsed'],
    mode='markers',
    marker=dict(
        color=dfloginskaj['Product Progress'],
        colorscale='sunsetdark',
        colorbar=dict(title='Product Progress', titleside='right')
    ),
    opacity=0.7
))

    # Update layout
    fig.update_layout(
        title=dict(
            text='<b>Correlation between Logins, Months Lapsed, and Product Progress</b>',
            x=0.5,
            y=0.9,
            xanchor='center',
            yanchor='top',
            font=dict(family='Raleway',
                    size=18,
                    color='rgb(37, 37, 37)')
        ),
        font=dict(family='Raleway', size=12, color='rgb(64, 64, 64)'),
        xaxis=dict(title='Logins', title_font=dict(family='Raleway', size=14)),
        yaxis=dict(title='Months Lapsed', title_font=dict(family='Raleway', size=14)),
        width=700,  # Adjust the width of the plot
        height=500,  # Adjust the height of the plot
    )
    st.plotly_chart(fig)

  
   