#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 07:53:05 2018

@author: sagar
"""
import sys
sys.path.insert(0, '/home/sagar/Dropbox/Scheduler/scripts/')
import pandas as pd
import numpy as np
from datetime import date
from aux_functions import next_dates, next_dates_weekday, next_dates_weekend


def flatten_unique(series):
    all_topics = [x for x in series.tolist() if str(x) != 'nan']
    unique_topics = set([item.strip() if isinstance(item,str) else item for sublist in all_topics for item in sublist])
    return list(unique_topics)


## Proficiency calculations
proficiency_matrix = pd.read_csv('data/HYD_Mentor_Topic.csv',index_col=0)
#proficiency_matrix = pd.read_csv('data/BLR_Mentor_Topic.csv',index_col=0)


mentor_schedule = pd.read_csv('data/melted_mentor_schedule.csv')
mentor_schedule['Date'] = pd.to_datetime(mentor_schedule['Date']).dt.date

date_index = pd.date_range(start=min(mentor_schedule['Date']), end=date(2019,12,31)).date

availability_matrix = pd.DataFrame(index=date_index,columns=proficiency_matrix.index)


for date_idx, row in availability_matrix.iterrows():
    if date_idx > date.today():
        for topic in availability_matrix.columns:
            available_mentors = mentor_schedule.loc[(mentor_schedule['Date']==date_idx) & (mentor_schedule['Binary']==0),'Mentor'].values.tolist()
            ranked = proficiency_matrix.loc[topic].loc[available_mentors].loc[proficiency_matrix.loc[topic].loc[available_mentors]>0].sort_values(ascending=False).to_dict() 
            availability_matrix.loc[date_idx][topic] = ranked


## Initial parameters
course_start_date = date(2019,1,1)  # Course starting date
course = "Rennes"  ## Rennes or PGP

# Pass a list of dates to be considered as study break
holidays = [date(2019,1,14),date(2019,2,11), date(2019,3,4)]
#holidays = [date(2018,10,2),date(2018,10,19),date(2018,11,7),date(2018,12,24),date(2018,12,25)]

if course=="Rennes":
    course_dates = next_dates_weekday(course_start_date,69+len(holidays))
    topic_flow = pd.read_csv('data/Rennes_Topic_Flow.csv')
else:
    course_dates = next_dates_weekend(course_start_date,48+len(holidays))
    topic_flow = pd.read_csv('data/PGP_Topic_Flow.csv')

#for d in course_dates:
#    if d in holidays:
#        print(d)

idx_cnt = 0
filler = pd.DataFrame({col:[np.nan] for col in topic_flow.columns})
for d in course_dates:
    if d in holidays:
        topic_flow = pd.concat([topic_flow.iloc[:idx_cnt,:].append(filler,ignore_index=True), topic_flow.iloc[idx_cnt:,:]]).reset_index(drop=True)
    idx_cnt +=1
    
topic_flow['Date'] = course_dates
if "Mapping" not in topic_flow.columns:
    topic_flow["Mapping"] = topic_flow["Module Text"]
    
topic_flow['Mapping'] = topic_flow['Mapping'].str.split('; ')
topic_flow['Best'] = ""
topic_flow['Best Score'] = ""
topic_flow['2nd Best'] = ""
topic_flow['2nd Best Score'] = ""
topic_flow['3rd Best'] = ""
topic_flow['3rd Best Scrore'] = ""
topic_flow['4rd Best'] = ""
topic_flow['4rd Best Scrore'] = ""
topic_flow['5rd Best'] = ""
topic_flow['5rd Best Scrore'] = ""
topic_flow['Mentor Dictionary'] = ""

        

### Manual Test ###
#date_lookup = date(2018,9,29)
#to_teach = ['Foundations of Probability and Statistics for Data Science']
#tc = to_teach[0]
#d_list = []
#d_keys = []
#for tc in to_teach:
#    d = availability_matrix.loc[date_lookup].loc[tc]
#    d_list.append(d)
#    d_keys.extend(list(d.keys()))
#td = pd.DataFrame(columns=set(d_keys),data=d_list)
#td.sum().idxmax()
#td.sum().nlargest(3)


skip_modules = [None, np.nan,'',' ','Essential Engineering Skills in Big Data Analytics Using R and Python', 'Language', 'Applying ML to Big Data Using Hadoop and Spark Ecosystem','Project viva']

row = topic_flow.iloc[34,:]

for idx, row in topic_flow.iterrows():
    if row['Mapping'] not in skip_modules and row['Date'] not in holidays:
        if row['Mapping'][0] not in skip_modules:
            to_teach = row['Mapping']
            d_list = []
            d_keys = []
            
            for tc in to_teach:
                tc = tc.strip()
                d = availability_matrix.loc[row['Date']].loc[tc]
                d_list.append(d)
                d_keys.extend(list(d.keys()))
            
            td = pd.DataFrame(columns=set(d_keys),data=d_list)
            topic_flow.loc[idx]['Mentor Dictionary'] = td.sum().to_dict()
    
            top = td.sum().nlargest(5)
            counter = topic_flow.columns.get_loc('Best')
            
            for name, score in top.iteritems():
                topic_flow.loc[idx][counter] = name
                topic_flow.loc[idx][counter+1] = score
                counter += 2


            
#        topic_flow.loc[idx]['Mentor'] = availability_matrix.loc[row['Date']].loc[to_teach].to_dict()

clean_columns = ['Day','Week', 'Date', 'Module', 'Module Text','Topics','Best','Best Score']
clean_columns.extend(topic_flow.columns.difference(clean_columns))
clean_schedule = topic_flow[clean_columns]
clean_schedule.to_csv("data/1-Jan-2019-Rennes-HYD.csv", index=False)






module = "CSE 7305c"
topics = flatten_unique(topic_flow['Mapping'][topic_flow['Module']==module])

for module in topic_flow['Module'].unique():
    if module not in ['LAB DAY','CUTe','MiTH','CSE 7212c','CSE 9099']:
        topics = flatten_unique(topic_flow['Mapping'][topic_flow['Module']==module])
        for tc in topics:
            d = availability_matrix.loc[date_lookup].loc[tc]
            d_list.append(d)
            d_keys.extend(list(d.keys()))
        td = pd.DataFrame(columns=set(d_keys),data=d_list)
            


topic_flow.set_index('Date', inplace=True)
topic_flow.to_csv("1st-Sep_HYD_test.csv")    