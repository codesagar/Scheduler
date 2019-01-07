#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:39:35 2018

@author: sagar
"""

import sys
sys.path.insert(0, 'C:/Users/Sagar Patel/Dropbox/Scheduler/scripts')
from openpyxl import load_workbook
import pandas as pd
import numpy as np
from datetime import date, timedelta
from aux_functions import read_sheet, set_schedule, update_availability, availability_topics

#==============================================================================
# ## Mentor
#==============================================================================
scheduling_matrix = load_workbook("data/Faculty-Scientist_Scheduling_Matrix.xlsx",data_only=True)
mentor_schedule = read_sheet(scheduling_matrix,'Mentor_PGP2018')
mentor_schedule = mentor_schedule.replace({"":None," ":None,"  ":None,"   ":None})
mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date
mentor_schedule.set_index("Date",inplace=True, drop=False)


date_index = pd.date_range(start=date.today(), end=date(2019,12,31)).date
availability_matrix = pd.DataFrame(index=date_index,columns=availability_topics)
                          

#==============================================================================
# Hyderabad	05-Jan-19	PGP57-HYD
#==============================================================================
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Available'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
course_start_date = date(2019,1,5)  # Course starting date
course = "PGP"                    # Course type
location = "HYD"
availability_matrix = update_availability(availability_matrix, melted_mentor_schedule,course_start_date,course,location)

holidays = []
schedule = set_schedule(course_start_date, holidays, course, availability_matrix)
schedule.to_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv", index=False)


## Read after manual updates
schedule = pd.read_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv")
schedule['Date'] = pd.to_datetime(schedule['Date'],format="%d-%m-%Y").dt.date
for idx, row in schedule.iterrows():
    if row['Proposed'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Proposed']] = "PGP57-HYD"

mentor_schedule.to_csv("proposed_schedules/ms_checkpoint_"+location+" "+str(course_start_date)+".csv", index=False)                           


#==============================================================================
# Bengaluru	26-Jan-19	PGP58-BLR
#==============================================================================
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Available'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
course_start_date = date(2019,1,26)  # Course starting date
course = "PGP"                    # Course type
location = "BLR"
availability_matrix = update_availability(availability_matrix, melted_mentor_schedule,course_start_date,course,location)

holidays = []
schedule = set_schedule(course_start_date, holidays, course, availability_matrix)
schedule.to_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv", index=False)


## Read after manual updates
schedule = pd.read_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv")
schedule['Date'] = pd.to_datetime(schedule['Date'],format="%d-%m-%Y").dt.date
for idx, row in schedule.iterrows():
    if row['Proposed'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Proposed']] = "PGP58-BLR"

mentor_schedule.to_csv("proposed_schedules/ms_checkpoint_"+location+" "+str(course_start_date)+".csv", index=False)                           


#==============================================================================
# Hyderabad	10-Feb-19	PGP59-HYD
#==============================================================================
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Available'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
course_start_date = date(2019,2,10)  # Course starting date
course = "PGP"                    # Course type
location = "HYD"
availability_matrix = update_availability(availability_matrix, melted_mentor_schedule,course_start_date,course,location)

holidays = []
schedule = set_schedule(course_start_date, holidays, course, availability_matrix)
schedule.to_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv", index=False)


## Read after manual updates
schedule = pd.read_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv")
schedule['Date'] = pd.to_datetime(schedule['Date'],format="%d-%m-%Y").dt.date
for idx, row in schedule.iterrows():
    if row['Proposed'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Proposed']] = "PGP59-HYD"
                                                   
mentor_schedule.to_csv("proposed_schedules/ms_checkpoint_"+location+" "+str(course_start_date)+".csv", index=False)                           

#==============================================================================
# Hyderabad	25-Feb-19	60HYD-Rennes-MSc 
#==============================================================================
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Available'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
course_start_date = date(2019,2,25)  # Course starting date
course = "Rennes"                    # Course type
location = "HYD"
availability_matrix = update_availability(availability_matrix, melted_mentor_schedule,course_start_date,course,location)

holidays = []
schedule = set_schedule(course_start_date, holidays, course, availability_matrix)
schedule.to_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv", index=False)


## Read after manual updates
schedule = pd.read_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv")
schedule['Date'] = pd.to_datetime(schedule['Date'],format="%d-%m-%Y").dt.date
for idx, row in schedule.iterrows():
    if row['Proposed'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Proposed']] = "60HYD-Rennes-MSc"
                                                   
mentor_schedule.to_csv("proposed_schedules/ms_checkpoint_"+location+" "+str(course_start_date)+".csv", index=False)                           
        
                           

#==============================================================================
# Bengaluru	25-Feb-19	61BLR-Rennes-MSc  
#==============================================================================
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Available'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
course_start_date = date(2019,2,25)  # Course starting date
course = "Rennes"                    # Course type
location = "BLR"
availability_matrix = update_availability(availability_matrix, melted_mentor_schedule,course_start_date,course,location)

holidays = []
schedule = set_schedule(course_start_date, holidays, course, availability_matrix)
schedule.to_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv", index=False)


## Read after manual updates
schedule = pd.read_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv")
schedule['Date'] = pd.to_datetime(schedule['Date'],format="%d-%m-%Y").dt.date
for idx, row in schedule.iterrows():
    if row['Proposed'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Proposed']] = "61BLR-Rennes-MSc"
        
mentor_schedule.to_csv("proposed_schedules/ms_checkpoint_"+location+" "+str(course_start_date)+".csv", index=False)                           

                         
                           
#==============================================================================
# Mumbai	02-Mar-19	PGP62-MUM  
#==============================================================================
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Available'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
course_start_date = date(2019,3,1)  # Course starting date
course = "PGP"                    # Course type
location = "MUM"
availability_matrix = update_availability(availability_matrix, melted_mentor_schedule,course_start_date,course,location)

holidays = []
schedule = set_schedule(course_start_date, holidays, course, availability_matrix)
schedule.to_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv", index=False)


## Read after manual updates
schedule = pd.read_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv")
schedule['Date'] = pd.to_datetime(schedule['Date'],format="%d-%m-%Y").dt.date
for idx, row in schedule.iterrows():
    if row['Proposed'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Proposed']] = "PGP62-MUM"
                          
mentor_schedule.to_csv("proposed_schedules/ms_checkpoint_"+location+" "+str(course_start_date)+".csv", index=False)                           
                           
                           
#==============================================================================
# Bengaluru	23-Mar-19	PGP63-BLR  
#==============================================================================
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Available'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
course_start_date = date(2019,3,23)  # Course starting date
course = "PGP"                    # Course type
location = "BLR"
availability_matrix = update_availability(availability_matrix, melted_mentor_schedule,course_start_date,course,location)

holidays = []
schedule = set_schedule(course_start_date, holidays, course, availability_matrix)
schedule.to_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv", index=False)


## Read after manual updates
schedule = pd.read_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv")
schedule['Date'] = pd.to_datetime(schedule['Date'],format="%d-%m-%Y").dt.date
for idx, row in schedule.iterrows():
    if row['Proposed'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Proposed']] = "PGP63-BLR"             
                           
mentor_schedule.to_csv("proposed_schedules/ms_checkpoint_"+location+" "+str(course_start_date)+".csv", index=False)                           
                           
                           
#==============================================================================
# Hyderabad	31-Mar-19	PGP64-HYD  
#==============================================================================
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Available'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
course_start_date = date(2019,3,31)  # Course starting date
course = "PGP"                    # Course type
location = "HYD"
availability_matrix = update_availability(availability_matrix, melted_mentor_schedule,course_start_date,course,location)

holidays = []
schedule = set_schedule(course_start_date, holidays, course, availability_matrix)
schedule.to_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv", index=False)


## Read after manual updates
schedule = pd.read_csv("proposed_schedules/"+location+" "+str(course_start_date)+".csv")
schedule['Date'] = pd.to_datetime(schedule['Date'],format="%d-%m-%Y").dt.date
for idx, row in schedule.iterrows():
    if row['Proposed'] not in [None,""," ", np.nan]:
        mentor_schedule.loc[row['Date'],row['Proposed']] = "PGP64-HYD"                                                      

mentor_schedule.to_csv("proposed_schedules/ms_checkpoint_"+location+" "+str(course_start_date)+".csv", index=False)                           
                           
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")

melted_mentor_schedule = melted_mentor_schedule.replace({"":None," ":None,"  ":None,"   ":None})
#melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Type']=""
melted_mentor_schedule['Hours']=0
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].notnull(),'Type']="Corporate"
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].notnull(),'Hours']=4

melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("pgp|cpee|Complete|Batch",na=False,case=False).tolist(),'Type']="Academic"
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("pgp|cpee|Complete|Batch",na=False,case=False).tolist(),'Hours']=4
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("personal",na=False,case=False).tolist(),'Hours']=0
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("personal",na=False,case=False).tolist(),'Type']=""
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("Rennes",na=False,case=False).tolist(),'Hours']=2
#melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("cpee",na=False,case=False).tolist(),'Type']="Academic"
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("info|meet",na=False,case=False).tolist(),'Type']="Other"
#melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("batch",na=False,case=False).tolist(),'Type']="Other"
#melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("meet",na=False,case=False).tolist(),'Type']="Other"
melted_mentor_schedule['Binary'] = [1 if x in ["Corporate","Academic"] else 0 for x in melted_mentor_schedule['Type']]
#melted_mentor_schedule['Binary'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
#melted_mentor_schedule = melted_mentor_schedule.fillna('')                           
#melted_mentor_schedule['1W'] = melted_mentor_schedule.groupby('Mentor')['Binary'].rolling(7).sum().reset_index(0,drop=True)

melted_mentor_schedule['4W'] = melted_mentor_schedule.groupby('Mentor')['Hours'].rolling(28).sum().reset_index(0,drop=True)


melted_mentor_schedule.to_csv('proposed_schedules/final_melted_mentor_schedule.csv')