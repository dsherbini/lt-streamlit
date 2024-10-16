#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sketching Leg Tracker using Streamlit
Created on Oct 2, 2024
@author: danyasherbini

This script sketches a prototype of the Legislation Tracker app using 
Streamlit, an open-source framework to build data apps in Python.
"""

import os
import pandas as pd
import numpy as np
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, ColumnsAutoSizeMode
from src import aggrid_styler


PATH = '/Users/danyasherbini/Documents/GitHub/lt-streamlit'
os.chdir(PATH)
os.getcwd()


# Show the page title and description
st.set_page_config(page_title='Legislation Tracker', layout='wide') #can add page_icon argument
st.title('Legislation Tracker')
st.write(
    """
    This app shows California bills for the 2023-2024 legislative session. 
    Type in a search term to filter bills.
    """
)

# Add logo
st.logo(
    '/Users/danyasherbini/Documents/GitHub/lt-streamlit/logo.png',
    link="https://techequity.us"
)

# Add sidebar
st.sidebar.markdown('Legislation Tracker')

############################ LOAD AND SET UP DATA #############################

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    bills = pd.read_csv('/Users/danyasherbini/Documents/GitHub/lt-streamlit/data/bills.csv')
    bills['chamber'] = np.where(bills['origin_chamber_id']==1,'Assembly','Senate')
    bill_history = pd.read_csv('/Users/danyasherbini/Documents/GitHub/lt-streamlit/data/bill_history.csv')
    bills = pd.merge(bills, bill_history, how='left', on= 'bill_id')
    bills = bills.rename(columns={'history_trace':'bill_history','bill_date':'date_introduced','bill_number':'bill_no'})
    return bills

bills = load_data()

# Move bill_number column to first column
numbers = bills['bill_no']
bills.insert(0,'bill_number',numbers)

# Drop some columns we don't need
drop_cols = ['bill_no','bill_id','openstates_bill_id', 'committee_id', 'origin_chamber_id']
bills = bills.drop(drop_cols, axis=1)

# Sort by bill number by default
bills = bills.sort_values('bill_number', ascending=True) 


# Get dataframes for AI bills, housing bills, and labor bills

# AI bills
ai_df = bills[bills['bill_name'].str.contains('artificial intelligence',na=False,case=False)]
ai_df = ai_df.sort_values('bill_number', ascending=True) # sort by bill number by default


# Housing bills
housing_terms = ['housing','eviction','tenants','renters']
housing_df = bills[bills['bill_name'].str.contains('|'.join(housing_terms), na=False, case=False)]
housing_df = housing_df.sort_values('bill_number', ascending=True) # sort by bill number by default


# Labor bills
labor_terms = ['worker','labor','gig economy','contract workers']
labor_df = bills[bills['bill_name'].str.contains('|'.join(labor_terms), na=False, case=False)]
labor_df = labor_df.sort_values('bill_number', ascending=True) # sort by bill number by default


# Page tabs
tab1, tab2, tab3 , tab4 = st.tabs(['All Bills', 'AI', 'Housing', 'Labor'])


############################### TAB 1: All Bills ###############################
with tab1:
   st.header("All Bills")
   
   # Search bar widget
   with st.form(key='search_form_all_bills'):
       search_term = st.text_input('Search for bills:', placeholder='Enter text to search')
       submit_button = st.form_submit_button(label='Search')

   # Filter data based on search term entered
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

############################### TAB 2: AI Bills ###############################
with tab2: 
    st.header("AI Bills")

    # Search bar widget
    with st.form(key='search_form_ai'):
        search_term = st.text_input('Search for bills:', placeholder='Enter text to search')
        submit_button = st.form_submit_button(label='Search')

    # Filter data based on search term entered
    def filter_data():
        # starting point is only AI-related bills
        bills_df = ai_df.copy()
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
            ai_df,
            use_container_width=True,
            hide_index=True)
        
        
############################# TAB 3: Housing Bills #############################

# In this tab, when a user clicks on a row of data, bill details are displayed
# in a dialog pop-up box

with tab3:
    # Title the page
    st.header("Housing Bills")
    
    # Make the aggrid dataframe
    data = aggrid_styler.draw_grid(
        housing_df)

    selected_rows = data.selected_rows
        
    @st.dialog('Bill Info', width='large')
    def bill_info():
        # Extract the values from the selected row
        number = selected_rows['bill_number'].iloc[0]
        name = selected_rows['bill_name'].iloc[0]
        author = selected_rows['author'].iloc[0]
        text = selected_rows['full_text'].iloc[0]
        chamber = selected_rows['chamber'].iloc[0]
        
        # Create first container for bill number and name
        with st.container(key='number_name'):
            # Display two columns in this container
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("##### Bill No.")
                st.markdown(number)
            with col2:
                st.markdown("##### Bill Name")
                st.markdown(name)
            
        # Create second container for chamber and author
        with st.container(key='chamber_author'):
            # Display two columns in this container
            col3, col4 = st.columns(2)
            with col3:
                st.markdown("##### Chamber")
                st.markdown(chamber)
            with col4:
                st.markdown("##### Author")
                st.markdown(author)

        # Create third container for bill text
        with st.container(key='bill_text'):
            st.markdown("##### Bill Text")
            expander = st.expander("See bill text")
            expander.write(text)
    
    # If a row is selected:
    if selected_rows is not None:
        if len(selected_rows) != 0:
            bill_info()
        
        
############################# TAB 4: Labor Bills ##############################

# In this tab, when a user clicks on a row of data, bill details are displayed
# below the dataframe in columns

with tab4: 
    # Title the page
    st.header("Labor Bills")
    
    # Make the aggrid dataframe
    data = aggrid_styler.draw_grid(
        labor_df)

    selected_rows = data.selected_rows
        
    # If a row is selected:
    if selected_rows is not None:
        if len(selected_rows) != 0:
                
            # Extract the values from the selected row
            number = selected_rows['bill_number'].iloc[0]
            name = selected_rows['bill_name'].iloc[0]
            author = selected_rows['author'].iloc[0]
            text = selected_rows['full_text'].iloc[0]
            chamber = selected_rows['chamber'].iloc[0]
                
            # Display in columns
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.markdown("##### Bill No.")
                st.markdown(number)
            with col2:
                st.markdown("##### Bill Name")
                st.markdown(name)
            with col3:
                st.markdown("##### Chamber")
                st.markdown(chamber)
            with col4:
                st.markdown("##### Author")
                st.markdown(author)
            with col5:
                st.markdown("##### Bill Text")
                st.markdown(text)

#import pandas as pd
    from io import BytesIO

    def to_csv(df) -> bytes:
        output = BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)
        return output.getvalue()

    st.download_button(
        "Download as CSV",
        data=to_csv(data['data']),
        file_name="output.csv",
        mime="text/csv"
        )




                    
#row['bill_name'].to_string(index=False)


#### EXTRA WIDGETS TO ADD LATER! 
# Filtering widgets

# Show a slider widget with the years using `st.slider`.
#years = st.slider("Years", 1986, 2006, (2000, 2016))

# Multiselect widget for chamber
#chambers = st.multiselect(
#    "origin_chamber_id",
#    [1,2],
#    [1,2]
#)
