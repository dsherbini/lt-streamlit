#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ag Grid DataFrame Formatter
Created on Oct 3, 2024
@author: danyasherbini

This script contains a dictionary of original column names, display column names, 
and column widths that are used to format the Ag Grid data frames in the Streamlit
app.
"""


formatter = {
    'bill_number': ('Bill Number', {'width': 120}),
    'bill_name': ('Bill Name', {'width': 200}),
    'origin_chamber_id': ('Chamber',{'width': 100}),
    'author': ('Author', {'width': 160}),
    'full_text': ('Bill Text', {'width': 200}),
}

format_dict = dict(formatter)