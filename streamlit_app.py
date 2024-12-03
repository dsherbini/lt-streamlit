#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sketching Leg Tracker using Streamlit
Created on Oct 2, 2024
@author: danyasherbini

This script sketches a prototype of the Legislation Tracker app using 
Streamlit, an open-source framework to build data apps in Python.
"""

import streamlit as st

# Pages
bills = st.Page('bills.py', title='Bills', icon='📝')
legislators = st.Page('legislators.py', title='Legislators', icon='💼')
calendar = st.Page('calendar2.py', title='Calendar', icon='📅')
dashboard = st.Page('dashboard.py', title='My Dashboard', icon='📌')


# Build navigation bar
pg = st.navigation([bills,legislators,calendar, dashboard])
st.set_page_config(page_title='Legislation Tracker', layout='wide')

# Add logo
st.logo(
    '/Users/danyasherbini/Documents/GitHub/lt-streamlit/logo.png',
    link="https://techequity.us"
)

# Run the pages
pg.run()