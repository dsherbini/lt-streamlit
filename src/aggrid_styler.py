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

# Ag grid styler function for bills table
def draw_bill_grid(
        df,
        formatter: dict = None,
        selection='single',
        use_checkbox=True,
        #header_checkbox = True,
        fit_columns=False,
        theme='streamlit',
        max_height: int = 500,
        wrap_text: bool = False,
        auto_height: bool = False,
        key=None,
        css: dict = None
):

    # Initialize the GridOptionsBuilder from the dataframe passed into the function
    builder = GridOptionsBuilder().from_dataframe(df)
    
    # Configure default column settings for all columns
    builder.configure_default_column(
        enableFilter=True,
        filter='agTextColumnFilter',
        # floating filter: adds a row under the header row for the filter
        floatingFilter=True,
        #columnSize='sizeToFit'
        )
    
    # Configure special settings for certain columns (batch)
    builder.configure_columns(['full_text','leginfo_link','coauthors','bill_history','leg_session'],hide=True)
    
    # Configure special settings for individual columns 
    builder.configure_column('bill_number',pinned='left') 
    builder.configure_column('date_introduced',filter='agDateColumnFilter')
    builder.configure_column('chamber',filter='agSetColumnFilter')
    
    # Configure how user selects rows
    builder.configure_selection(selection_mode=selection, use_checkbox=use_checkbox)
    
    # Build the grid options dictionary
    grid_options = builder.build()

    return AgGrid(
        df,
        # pass the grid options dictionary built above
        gridOptions=grid_options,
        # ensures the df is updated dynamically
        update_mode=GridUpdateMode.SELECTION_CHANGED | GridUpdateMode.VALUE_CHANGED,
        allow_unsafe_jscode=True,
        fit_columns_on_grid_load=fit_columns,
        max_height=max_height,
        theme=theme,
        key=key,
        css=css
    )


# Ag grid styler function for legislators table
def draw_leg_grid(
        df,
        formatter: dict = None,
        #selection='single', -- selection turned off for legislators
        #use_checkbox=True,
        #header_checkbox = True,
        fit_columns=False,
        theme='streamlit',
        max_height: int = 500,
        wrap_text: bool = False,
        auto_height: bool = False,
        key=None,
        css: dict = None
):

    # Initialize the GridOptionsBuilder from the dataframe passed into the function
    builder = GridOptionsBuilder().from_dataframe(df)
    
    # Configure default column settings for all columns
    builder.configure_default_column(
        enableFilter=True,
        filter='agTextColumnFilter',
        # floating filter: adds a row under the header row for the filter
        floatingFilter=True,
        columnSize='sizeToFit'
        )
    
    # Configure special settings for certain columns (batch)
    builder.configure_columns(['legislator_id'],hide=True)
    
    # Configure special settings for individual columns 
    builder.configure_column('name',pinned='left',filter='agSetColumnFilter') 
    builder.configure_column('district',filter='agNumberColumnFilter')
    builder.configure_column('party',filter='agSetColumnFilter')
    builder.configure_column('chamber',filter='agSetColumnFilter')
    
    # Configure how user selects rows -- turned off for legislators
    #builder.configure_selection(selection_mode=selection, use_checkbox=use_checkbox)
    
    # Build the grid options dictionary
    grid_options = builder.build()

    return AgGrid(
        df,
        # pass the grid options dictionary built above
        gridOptions=grid_options,
        # ensures the df is updated dynamically
        update_mode=GridUpdateMode.SELECTION_CHANGED | GridUpdateMode.VALUE_CHANGED,
        allow_unsafe_jscode=True,
        fit_columns_on_grid_load=fit_columns,
        max_height=max_height,
        theme=theme,
        key=key,
        css=css
    )

