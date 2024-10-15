#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ag Grid DataFrame Styler
Created on Oct 3, 2024
@author: danyasherbini

This script contains settings for interactive Ag Grid data frames on Streamlit, 
which are clickable/editable data tables.
"""

from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

# Set max height for all data tables
MAX_TABLE_HEIGHT = 500

# Data grid configuration
def draw_grid(
        df,
        formatter: dict = None,
        selection='single',
        use_checkbox=True,
        fit_columns=False,
        theme='streamlit',
        max_height: int = MAX_TABLE_HEIGHT,
        wrap_text: bool = False,
        auto_height: bool = False,
        #grid_options: dict = None,
        key=None,
        css: dict = None
):

    # Initialize the dataframe
    gb = GridOptionsBuilder()
    
    # Configure default column settings
    gb.configure_default_column(
        enableFilter=True,
        filter='agTextColumnFilter'
        #filterable=True,
        #groupable=True,
        #editable=False,
        #wrapText=wrap_text,
        #autoHeight=auto_height
    )


    # Configure dataframe options
    gb.configure_grid_options(enableSorting=True, enableFilter=True)
    
    # Styling for columns
    for latin_name, (cyr_name, style_dict) in formatter.items():
        gb.configure_column(latin_name, header_name=cyr_name, **style_dict)
    
    # Configure how user selects rows
    gb.configure_selection(selection_mode=selection, use_checkbox=use_checkbox)

    return AgGrid(
        df,
        gridOptions=gb.build(),
        update_mode=GridUpdateMode.SELECTION_CHANGED | GridUpdateMode.VALUE_CHANGED,
        allow_unsafe_jscode=True,
        fit_columns_on_grid_load=fit_columns,
        height=max_height,
        theme=theme,
        key=key,
        custom_css=css
    )


