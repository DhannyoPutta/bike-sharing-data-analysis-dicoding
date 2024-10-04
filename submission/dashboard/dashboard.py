import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import sys
from pathlib import Path

dir = Path(__file__).resolve()
print(dir)

path_to_day_df = 'day_data.csv'
path_to_hour_df = 'hour_data.csv'

with open(path_to_day_df, 'rb') as file:
    day_df = pd.read_csv(file)

with open(path_to_hour_df, 'rb') as file:
    hour_df = pd.read_csv(file)

sns.set(style='dark')

st.title("Bike Sharing Dashboard :bike:")

st.subheader('Customer Demographic')

col1, col2 = st.columns(2)

with col1:
    st.metric(label='Daily Casual Users', value = int(day_df["casual"].mean()))
    st.metric(label='Daily Registered Users', value = int(day_df["registered"].mean()))

with col2:
    st.metric(label='Monthly Casual Users', value = int(day_df["casual"].mean()) * 30)
    st.metric(label='Monthly Registered Users', value = int(day_df["registered"].mean()) * 30)


st.subheader('Bike Sharing Usage Behavior')

tab1, tab2, tab3 = st.tabs(["Day of the Week", "Time of Day and Day of the Week", "Status of Registration"])
 
with tab1:
    figure, axis = plt.subplots(figsize=(12, 5))
    sns.barplot(data=day_df, x='weekday', y='count', palette = "rocket", ax=axis)
    axis.set_title("Bike Sharing Usage based on Day of the Week", loc="center", fontsize=18)
    axis.set(xlabel=None)
    axis.set(ylabel=None)
    
    st.pyplot(figure)
 
with tab2:
    figure, axis = plt.subplots(figsize=(12, 5))
    sns.pointplot(data=hour_df, x='hour', y= 'count', hue='weekday', ax=axis)
    axis.set_title("Bike Sharing Usage based on Time of Day and Day of the Week", loc="center", fontsize=18)
    
    st.pyplot(figure)

with tab3:
    melted_df = hour_df.melt(id_vars=['weekday'], value_vars=['casual', 'registered'],
                          var_name='user_type', value_name='rental_count')

    figure, axis = plt.subplots(figsize=(12, 6))
    sns.barplot(data=melted_df, x='weekday', y='rental_count', hue='user_type', estimator=sum)

    axis.set_title('Daily Casual and Registered Customers', loc="center", fontsize=18)

    st.pyplot(figure)
    
tab1, tab2, tab3 = st.tabs(["Weather Condition", "Season", "Month"])

custom_palette = ['#A8E6CF',
                  '#FFD54F',
                  '#FF8A65',
                  '#90CAF9']

with tab1:
    figure, axis = plt.subplots(figsize=(12, 5))

    sns.barplot(data=hour_df, x='weather', y='count', palette="mako_r", ax=axis)
    axis.set_title('Number of Customers on Different Weather Conditions', loc="center", fontsize=18)
    axis.set(xlabel=None)
    axis.set(ylabel=None)

    st.pyplot(figure)

with tab2:
    figure, axis = plt.subplots(figsize=(12, 5))
    
    sns.barplot(data=hour_df, x='season', y='count', hue='season', palette=custom_palette, ax=axis)
    axis.set_title('Number of Customers on Different Seasons', loc="center", fontsize=18)
    axis.set(xlabel=None)
    axis.set(ylabel=None)
    
    st.pyplot(figure)

with tab3:
    figure, axis = plt.subplots(figsize=(12, 5))
    
    sns.barplot(data=day_df, x='month', y='count', palette="viridis_r", ax=axis)
    axis.set_title('Number of Customers on Different Months', loc="center", fontsize=18)
    axis.set(xlabel=None)
    axis.set(ylabel=None)
    
    st.pyplot(figure)

st.subheader('Yearly Customer Growth')
figure, axis = plt.subplots(figsize=(12, 5))

day_df['year'].replace({0: "2011", 1: "2012"}, inplace = True)

sns.barplot(x='month', y='count', data=day_df, hue='year', ax=axis)
axis.set_title("Customer Growth in 2011 and 2012", loc="center", fontsize=18)
axis.set(xlabel=None)
axis.set(ylabel=None)
st.pyplot(figure)

st.caption("Dhannyo Putta - Oct 2024")
