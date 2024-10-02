#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sketching Leg Tracker using Streamlit
Created on Oct 2, 2024
@author: danyasherbini
"""

import pandas as pd
import streamlit as st
import os

PATH = '/Users/danyasherbini/Documents/GitHub/lt-streamlit'
os.chdir(PATH)


# Show the page title and description
st.set_page_config(page_title="Legislation Tracker", layout="wide") #can add page_icon argument
st.title("Legislation Tracker")
st.write(
    """
    This app shows California bills for the 2023-2024 legislative session. 
    Type in a search term to filter bills.
    """
)



# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("/Users/danyasherbini/Documents/GitHub/lt-streamlit/bills.csv")
    return df

df = load_data()

# Get only relevant columns
keep_cols = ['bill_number','bill_name','author','coauthors','full_text','origin_chamber_id']
bills = df[keep_cols]

# Filtering widgets

# Show a slider widget with the years using `st.slider`.
#years = st.slider("Years", 1986, 2006, (2000, 2016))

# Multiselect widget for chamber
#chambers = st.multiselect(
#    "origin_chamber_id",
#    [1,2],
#    [1,2]
#)


# Search bar widget
with st.form(key='search_form'):
    search_term = st.text_input('Search for bills:', placeholder='Enter text to search')
    submit_button = st.form_submit_button(label='Search')

# Filter data
def filter_data():
    bills_df = bills.copy()
    df_filtered = bills_df[bills_df['bill_name'].str.contains(search_term, na=False, case=False)]
    return df_filtered

# Display filtered data when search button is clicked
if submit_button:
    st.dataframe(
        filter_data(),
        use_container_width=True,
        hide_index=True)
# otherwise display all data
else:
    st.dataframe(
        bills.copy(),
        use_container_width=True,
        hide_index=True)
