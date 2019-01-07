#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:27:03 2018

@author: sagar
"""

from openpyxl import load_workbook
import pandas as pd
from datetime import date
from aux_functions import date_range, next_dates, this_weekend, read_sheet


#==============================================================================
# ## Mentor
#==============================================================================
scheduling_matrix = load_workbook("data/Faculty-Scientist_Scheduling_Matrix.xlsx",data_only=True)
mentor_schedule = read_sheet(scheduling_matrix,'Mentor_PGP2018')
mentor_schedule = mentor_schedule.replace({"":None," ":None,"  ":None,"   ":None})
mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date
melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")


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


melted_mentor_schedule.to_csv('data/melted_mentor_schedule.csv')





# =============================================================================
# melted_mentor_schedule['Type']=""
# melted_mentor_schedule['Hours']=0
# melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].notnull(),'Type']="Corporate"
# melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("pgp|cpee|Complete|Batch",na=False,case=False).tolist(),'Type']="Academic"
# #melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("cpee",na=False,case=False).tolist(),'Type']="Academic"
# melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("info|meet",na=False,case=False).tolist(),'Type']="Other"
# #melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("batch",na=False,case=False).tolist(),'Type']="Other"
# #melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("meet",na=False,case=False).tolist(),'Type']="Other"
# melted_mentor_schedule['Binary'] = [1 if x in ["Corporate","Academic"] else 0 for x in melted_mentor_schedule['Type']]
# #melted_mentor_schedule['Binary'] = [0 if x==None else 1 for x in melted_mentor_schedule['Allocation']]
# #melted_mentor_schedule = melted_mentor_schedule.fillna('')                           
# #melted_mentor_schedule['1W'] = melted_mentor_schedule.groupby('Mentor')['Binary'].rolling(7).sum().reset_index(0,drop=True)
# melted_mentor_schedule['4W'] = melted_mentor_schedule.groupby('Mentor')['Binary'].rolling(28).sum().reset_index(0,drop=True)
# melted_mentor_schedule.to_csv('data/melted_mentor_schedule.csv')
# =============================================================================

#==============================================================================
# ## Testing
# #test = melted_mentor_schedule[melted_mentor_schedule['Binary']==1]
# #print(test['Allocation'].unique())
# #test = melted_mentor_schedule[(melted_mentor_schedule['Allocation'].isnull() & melted_mentor_schedule['Binary']==1)]
# #melted_mentor_schedule['Allocation'].isnull() = melted_mentor_schedule[melted_mentor_schedule['Allocation'].notnull()]
# 
#==============================================================================

#==============================================================================
# ## DS
#==============================================================================
ds_schedule = read_sheet(scheduling_matrix,'DS_PGP2018')
ds_schedule = ds_schedule.replace({"":None," ":None,"  ":None,"   ":None})
ds_schedule['Date'] = pd.to_datetime(ds_schedule['Date']).dt.date

melted_ds_schedule = pd.melt(ds_schedule,id_vars=['Date'],var_name="DataScientist",value_name="Allocation")
melted_ds_schedule['Type']=""
melted_ds_schedule.loc[melted_ds_schedule['Allocation'].notnull(),'Type']="Corporate"
melted_ds_schedule.loc[melted_ds_schedule['Allocation'].str.contains("pgp",na=False,case=False).tolist(),'Type']="Academic"
melted_ds_schedule.loc[melted_ds_schedule['Allocation'].str.contains("cpee",na=False,case=False).tolist(),'Type']="Academic"
melted_ds_schedule.loc[melted_ds_schedule['Allocation'].str.contains("info",na=False,case=False).tolist(),'Type']="Other"
melted_ds_schedule.loc[melted_ds_schedule['Allocation'].str.contains("meet",na=False,case=False).tolist(),'Type']="Other"
melted_ds_schedule['Binary'] = [0 if x==None else 1 for x in melted_ds_schedule['Allocation']]
#melted_ds_schedule = melted_ds_schedule.fillna('')                           
#melted_ds_schedule['1W'] = melted_ds_schedule.groupby('DataScientist')['Binary'].rolling(7).sum().reset_index(0,drop=True)
melted_ds_schedule['4W'] = melted_ds_schedule.groupby('DataScientist')['Binary'].rolling(28).sum().reset_index(0,drop=True)

melted_ds_schedule.to_csv('data/melted_ds_schedule.csv')
