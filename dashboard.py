#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testing out My Dashboard
Created on Dec 2, 2024
@author: danyasherbini

Page to add bills to user's private dashboard
"""

import streamlit as st
import pandas as pd
from src import aggrid_styler

# Initialize session state for selected bills if not already initialized
if 'selected_bills' not in st.session_state:
    st.session_state.selected_bills = []

st.title('Dashboard')

# Create a row with the button in the upper-right corner
col1, col2 = st.columns([3, 1])  # Adjust column widths for layout
with col2:
    if st.button('Clear Dashboard'):
        st.session_state.selected_bills = []
        st.success('Dashboard cleared!')

# Check if there are selected bills
if st.session_state.selected_bills:
    st.write('Selected Bills:')

    # Convert the session state list to a DataFrame for Ag-Grid
    dashboard_df = pd.DataFrame(st.session_state.selected_bills)

    # Display the DataFrame as an Ag-Grid table
    aggrid_styler.draw_bill_grid(dashboard_df)
else:
    st.write('No bills selected yet.')
