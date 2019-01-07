#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:26:31 2018

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
#scheduling_matrix = load_workbook("data/Faculty-Scientist_Scheduling_Matrix.xlsx",data_only=True)
#mentor_schedule = read_sheet(scheduling_matrix,'Mentor_PGP2018')

#mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date
#mentor_schedule.set_index("Date",inplace=True, drop=False)

melted_mentor_schedule = pd.read_csv('data/melted_mentor_schedule.csv')
melted_mentor_schedule['Date'] = pd.to_datetime(melted_mentor_schedule['Date']).dt.date
melted_mentor_schedule['Hours'] = 0
schedule = pd.read_csv("data/5-Jan-2019-HYD.csv")
schedule['Date'] = pd.to_datetime(schedule['Date']).dt.date

#row = schedule.iloc[2]
#sum((melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']))
#sum(melted_mentor_schedule['Mentor'] == row['Best'])
#sum(melted_mentor_schedule['Date'] == row['Date'])

for idx, row in schedule.iterrows():
    if row['Best'] not in [None,""," ", np.nan]:
#        mentor_schedule.loc[row['Date'],row['Best']] = "PGP57-HYD"
#        melted_mentor_schedule.loc[(melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']),"Hours"] = 4
        melted_mentor_schedule.loc[(melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']),"Allocation"] = "PGP57-HYD"
#        melted_mentor_schedule.loc[(melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']),"Binary"] = 1
#        melted_mentor_schedule.loc[(melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']),"Type"] = "Academic"
    if row['2nd Best'] not in [None,""," ", np.nan]:
#        mentor_schedule.loc[row['Date'],row['2nd Best']] = "PGP58-HYD"
#        melted_mentor_schedule.loc[(melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']),"Hours"] = 4
        melted_mentor_schedule.loc[(melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']),"Allocation"] = "PGP58-HYD"
#        melted_mentor_schedule.loc[(melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']),"Binary"] = 1
#        melted_mentor_schedule.loc[(melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']),"Type"] = "Academic"
        
melted_mentor_schedule = melted_mentor_schedule.replace({"":None," ":None,"  ":None,"   ":None})
#melted_mentor_schedule = pd.melt(mentor_schedule,id_vars=['Date'],var_name="Mentor",value_name="Allocation")
melted_mentor_schedule['Type']=""
melted_mentor_schedule['Hours']=0
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].notnull(),'Type']="Corporate"
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("pgp|cpee|Complete|Batch",na=False,case=False).tolist(),'Type']="Academic"
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("pgp|cpee|Complete|Batch",na=False,case=False).tolist(),'Hours']=4
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


melted_mentor_schedule.to_csv('data/updated_melted_mentor_schedule.csv',index=False)




melted_mentor_schedule = pd.read_csv('data/updated_melted_mentor_schedule.csv')
melted_mentor_schedule['Date'] = pd.to_datetime(melted_mentor_schedule['Date']).dt.date
melted_mentor_schedule.set_index("Date",inplace=True, drop=False)

schedule = pd.read_csv("data/1-Dec-2018-BLR.csv")

for idx, row in schedule.iterrows():
    if row['Best'] not in [None,""," ", np.nan]:
#        mentor_schedule.loc[row['Date'],row['Best']] = "PGP56-BLR"
        melted_mentor_schedule.loc[(melted_mentor_schedule['Mentor'] == row['Best']) & (melted_mentor_schedule['Date'] == row['Date']),"Allocation"] = "PGP56-BLR"
        

melted_mentor_schedule = melted_mentor_schedule.replace({"":None," ":None,"  ":None,"   ":None})
melted_mentor_schedule['Date'] = pd.to_datetime(melted_mentor_schedule['Date']).dt.date
melted_mentor_schedule['Type']=""
melted_mentor_schedule['Hours']=0
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].notnull(),'Type']="Corporate"
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("pgp|cpee|Complete|Batch|Rennes",na=False,case=False).tolist(),'Type']="Academic"
melted_mentor_schedule.loc[melted_mentor_schedule['Allocation'].str.contains("pgp|cpee|Complete|Batch",na=False,case=False).tolist(),'Hours']=4
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

test= melted_mentor_schedule[-melted_mentor_schedule['Allocation'].isnull()]
pt = pd.pivot_table(data=test,values='Allocation',index=test.index,columns=test['Mentor'],aggfunc=lambda x: str(x[0]))

melted_mentor_schedule.isnull().sum()
melted_mentor_schedule.to_csv('data/updated_melted_mentor_schedule.csv',index=False)
