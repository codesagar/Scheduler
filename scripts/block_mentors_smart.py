#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:40:10 2018

@author: sagar
"""

from openpyxl import load_workbook
import pandas as pd
from datetime import date
from aux_functions import date_range, next_dates, this_weekend, read_sheet
import numpy as np

#==============================================================================
# ## Mentor
#==============================================================================
scheduling_matrix = load_workbook("data/Faculty-Scientist_Scheduling_Matrix.xlsx",data_only=True)
mentor_schedule = read_sheet(scheduling_matrix,'Mentor_PGP2018')

#mentor_schedule.to_csv("data/mentor_schedule.csv",index=False)

### HYD B57-58
#mentor_schedule = pd.read_csv('data/mentor_schedule.csv')
mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date
mentor_schedule.set_index("Date",inplace=True, drop=False)

schedule = pd.read_csv("data/5-Jan-2019-HYD.csv")
schedule['Date'] = pd.to_datetime(schedule['Date']).dt.date



        
mentor_schedule.to_csv("data/mentor_schedule.csv",index=False)



### BLR B56
mentor_schedule = pd.read_csv('data/mentor_schedule.csv')
mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date
mentor_schedule.set_index("Date",inplace=True, drop=False)

schedule = pd.read_csv("data/1-Dec-2018-BLR.csv")
schedule['Date'] = pd.to_datetime(schedule['Date']).dt.date


for idx, row in schedule.iterrows():
    if row['Best'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Best']] = "PGP56-BLR"

mentor_schedule.to_csv("data/mentor_schedule.csv",index=False)



### HYD Rennes - 1st Jan
mentor_schedule = pd.read_csv('data/mentor_schedule.csv')
mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date
mentor_schedule.set_index("Date",inplace=True, drop=False)

schedule = pd.read_csv("data/1-Jan-2019-Rennes-HYD.csv")
schedule['Date'] = pd.to_datetime(schedule['Date']).dt.date


for idx, row in schedule.iterrows():
    if row['Best'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Best']] = "Rennes-HYD"

mentor_schedule.to_csv("data/mentor_schedule.csv",index=False)



### BLR Rennes - 1st Jan
mentor_schedule = pd.read_csv('data/mentor_schedule.csv')
mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date
mentor_schedule.set_index("Date",inplace=True, drop=False)

schedule = pd.read_csv("data/1-Jan-2019-Rennes-BLR.csv")
schedule['Date'] = pd.to_datetime(schedule['Date']).dt.date


for idx, row in schedule.iterrows():
    if row['Best'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Best']] = "Rennes-BLR"

mentor_schedule.to_csv("data/mentor_schedule.csv",index=False)



### BLR PGP - 23rd Mar
mentor_schedule = pd.read_csv('data/mentor_schedule.csv')
mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date
mentor_schedule.set_index("Date",inplace=True, drop=False)

schedule = pd.read_csv("data/23-Mar-2019-BLR.csv")
schedule['Date'] = pd.to_datetime(schedule['Date']).dt.date


for idx, row in schedule.iterrows():
    if row['Best'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Best']] = "PGP61-BLR"

mentor_schedule.to_csv("data/mentor_schedule.csv",index=False)




### HYD 2 PGP - 23rd Mar
mentor_schedule = pd.read_csv('data/mentor_schedule.csv')
mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date
mentor_schedule.set_index("Date",inplace=True, drop=False)

schedule = pd.read_csv("data/23-Mar-2019-BLR.csv")
schedule['Date'] = pd.to_datetime(schedule['Date']).dt.date


for idx, row in schedule.iterrows():
    if row['Best'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Best']] = "PGP62-HYD"
    if row['2nd Best'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['2nd Best']] = "PGP63-HYD"

mentor_schedule.to_csv("data/mentor_schedule.csv",index=False)