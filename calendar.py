#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calendar Page
Created on Nov 26, 2024
@author: danyasherbini

This page of the app features a calendar of legislative deadlines and/or events.
"""

import os
import pandas as pd
import numpy as np
import streamlit as st
from src import aggrid_styler
from src.utils import to_csv
from streamlit_calendar import calendar


PATH = '/Users/danyasherbini/Documents/GitHub/lt-streamlit'
os.chdir(PATH)
os.getcwd()


# Show the page title and description
#st.set_page_config(page_title='Legislation Tracker', layout='wide') #can add page_icon argument
st.title('Calendar')
st.write(
    """
    This page shows important deadlines and/or events in the legislative cycle. 
    """
)

############################ LOAD AND SET UP DATA #############################

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_calendar_data():
    assembly_data = pd.read_csv('/Users/danyasherbini/Documents/GitHub/lt-streamlit/data/assembly_calendar.csv')
    return assembly_data

assembly_data = load_calendar_data()


################################## CALENDAR ###################################
   
calendar_options = {
    #"editable": "true",
    "selectable": "true",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridMonth,dayGridWeek,listMonth",
    },
    #"slotMinTime": "06:00:00",
    #"slotMaxTime": "18:00:00",
    "initialView": "dayGridMonth",
    # can add additional features to the calendar, such as locations like rooms or buildings:
    #"resourceGroupField": "building",
    #"resources": [
    #    {"id": "a", "building": "Building A", "title": "Building A"},
    #    {"id": "b", "building": "Building A", "title": "Building B"},
    #    {"id": "c", "building": "Building B", "title": "Building C"},
    #],
}

# assembly calendar events as json list
calendar_events = [
  {
    "title": "Statutes take effect.",
    "start": "2025-01-01",
    "end": "2025-01-02",
    "allDay": "true"
  },
  {
    "title": "Legislature reconvenes.",
    "start": "2025-01-06",
    "end": "2025-01-07",
    "allDay": "true"
  },
  {
    "title": "Budget bill must be submitted by Governor.",
    "start": "2025-01-10",
    "end": "2025-01-11",
    "allDay": "true"
  },
  {
    "title": "Martin Luther King, Jr. Day observed.",
    "start": "2025-01-20",
    "end": "2025-01-21",
    "allDay": "true"
  },
  {
    "title": "Last day to submit bill requests to the Office of Legislative Counsel.",
    "start": "2025-01-24",
    "end": "2025-01-25",
    "allDay": "true"
  },
  {
    "title": "Presidents’ Day observed.",
    "start": "2025-02-17",
    "end": "2025-02-18",
    "allDay": "true"
  },
  {
    "title": "Last day for bills to be introduced.",
    "start": "2025-02-21",
    "end": "2025-02-22",
    "allDay": "true"
  },
  {
    "title": "Cesar Chavez Day observed.",
    "start": "2025-03-31",
    "end": "2025-04-01",
    "allDay": "true"
  },
  {
    "title": "Spring Recess begins upon adjournment.",
    "start": "2025-04-10",
    "end": "2025-04-11",
    "allDay": "true"
  },
  {
    "title": "Legislature reconvenes from Spring Recess.",
    "start": "2025-04-21",
    "end": "2025-04-22",
    "allDay": "true"
  },
  {
    "title": "Last day for policy committees to hear and report to fiscal committees fiscal bills introduced in their house.",
    "start": "2025-05-02",
    "end": "2025-05-03",
    "allDay": "true"
  },
  {
    "title": "Last day for policy committees to hear and report to the Floor nonfiscal bills introduced in their house.",
    "start": "2025-05-09",
    "end": "2025-05-10",
    "allDay": "true"
  },
  {
    "title": "Last day for fiscal committees to hear and report to the Floor bills introduced in their house.",
    "start": "2025-05-23",
    "end": "2025-05-24",
    "allDay": "true"
  },
  {
    "title": "Last day for fiscal committees to meet prior to June 9.",
    "start": "2025-05-23",
    "end": "2025-05-24",
    "allDay": "true"
  },
  {
    "title": "Memorial Day observed.",
    "start": "2025-05-26",
    "end": "2025-05-27",
    "allDay": "true"
  },
  {
    "title": "Floor sessions.",
    "start": "2025-06-02",
    "end": "2025-06-07",
    "allDay": "true"
  },
  {
    "title": "Last day for each house to pass bills introduced in that house.",
    "start": "2025-06-06",
    "end": "2025-06-07",
    "allDay": "true"
  },
  {
    "title": "Committee meetings may resume.",
    "start": "2025-06-09",
    "end": "2025-06-10",
    "allDay": "true"
  },
  {
    "title": "Budget bill must be passed by midnight.",
    "start": "2025-06-15",
    "end": "2025-06-16",
    "allDay": "true"
  },
  {
    "title": "Independence Day observed.",
    "start": "2025-07-04",
    "end": "2025-07-05",
    "allDay": "true"
  },
  {
    "title": "Last day for policy committees to hear and report bills.",
    "start": "2025-07-18",
    "end": "2025-07-19",
    "allDay": "true"
  },
  {
    "title": "Summer Recess begins upon adjournment, provided Budget Bill has been passed.",
    "start": "2025-07-18",
    "end": "2025-07-19",
    "allDay": "true"
  },
  {
    "title": "Legislature reconvenes from Summer Recess.",
    "start": "2025-08-18",
    "end": "2025-08-19",
    "allDay": "true"
  },
  {
    "title": "Last day for fiscal committees to hear and report bills to the Floor.",
    "start": "2025-08-29",
    "end": "2025-08-30",
    "allDay": "true"
  },
  {
    "title": "Labor Day observed.",
    "start": "2025-09-01",
    "end": "2025-09-02",
    "allDay": "true"
  },
  {
    "title": "Floor sessions.",
    "start": "2025-09-02",
    "end": "2025-09-13",
    "allDay": "true"
  },
  {
    "title": "Last day to amend on the Floor.",
    "start": "2025-09-05",
    "end": "2025-09-06",
    "allDay": "true"
  },
  {
    "title": "Last day for each house to pass bills.",
    "start": "2025-09-12",
    "end": "2025-09-13",
    "allDay": "true"
  },
  {
    "title": "Interim Recess begins upon adjournment.",
    "start": "2025-09-12",
    "end": "2025-09-13",
    "allDay": "true"
  },
  {
    "title": "Last day for Governor to sign or veto bills passed by the Legislature before Sept. 12 and in the Governor’s possession on or after Sept. 12.",
    "start": "2025-10-12",
    "end": "2025-10-13",
    "allDay": "true"
  },
  {
    "title": "Statutes take effect.",
    "start": "2026-01-01",
    "end": "2026-01-02",
    "allDay": "true"
  },
  {
    "title": "Legislature reconvenes.",
    "start": "2026-01-05",
    "end": "2026-01-06",
    "allDay": "true"
  }
]

# custom css formatting
custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""

# load calendar
calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)

