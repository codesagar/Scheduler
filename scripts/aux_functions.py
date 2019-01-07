from dateutil.rrule import DAILY, rrule, SA, SU, MO, TU, WE, TH, FR
from datetime import timedelta, date
import pandas as pd
import numpy as np

def flatten_unique(series):
    all_topics = [x for x in series.tolist() if str(x) != 'nan']
    unique_topics = set([item.strip() if isinstance(item,str) else item for sublist in all_topics for item in sublist])
    return list(unique_topics)


def date_range(start_date, end_date):
    out = []
    for dt in rrule(DAILY, dtstart=start_date, until=end_date, byweekday=(SA,SU)):
        out.append(dt.date())
    return out


def next_dates(start_date, n):
    out = []
    for dt in rrule(DAILY, dtstart=start_date, until=start_date + timedelta(n*7), byweekday=(SA,SU)):
        out.append(dt.date())
    return out


def next_dates_weekend(start_date, n):
    out = []
    for dt in rrule(DAILY, dtstart=start_date, until=start_date + timedelta((1+n)*7/2), byweekday=(SA,SU)):
        out.append(dt.date())
    return out[:n]


def next_dates_weekday(start_date, n):
    out = []
    for dt in rrule(DAILY, dtstart=start_date, until=start_date + timedelta((1+n)*7/5), byweekday=(MO, TU, WE, TH, FR)):
        out.append(dt.date())
    return out[:n]


def this_weekend():
    out = []
    for dt in rrule(DAILY, dtstart=date.today(), until=date.today() + timedelta(7), byweekday=(SA,SU)):
        out.append(dt.date())
    return out


def last_weekend():
    out = []
    for dt in rrule(DAILY, dtstart=date.today() - timedelta(7), until=date.today(), byweekday=(SA,SU)):
        out.append(dt.date())
    return out


def read_sheet(xlsx, sheet_name):
    sheet = pd.DataFrame(xlsx[sheet_name].values)
    sheet = sheet.rename(columns=sheet.iloc[0])
    sheet = sheet.iloc[1:,sheet.iloc[0,:].notnull().tolist()]
    if "Date" in sheet.columns:
        sheet['Date'] = pd.to_datetime(sheet['Date']).dt.date
    return sheet


def set_schedule(course_start_date, holidays, course, availability_matrix):
    if course=="Rennes":
        course_dates = next_dates_weekday(course_start_date,69+len(holidays))
        topic_flow = pd.read_csv('data/Rennes_Topic_Flow.csv')
    else:
        course_dates = next_dates_weekend(course_start_date,48+len(holidays))
        topic_flow = pd.read_csv('data/PGP_Topic_Flow.csv')
    
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
    
    skip_modules = [None, np.nan,'',' ','Essential Engineering Skills in Big Data Analytics Using R and Python', 'Language', 'Applying ML to Big Data Using Hadoop and Spark Ecosystem','Project viva']
    
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
    
    if course=="PGP":
        clean_columns = ['Day','Week', 'Date', 'Module', 'Module Text','Topics','Best','Best Score']
    else:
        clean_columns = ['Day', 'Date', 'Module', 'Module Text','Best','Best Score']
    
    clean_columns.extend(topic_flow.columns.difference(clean_columns))
    clean_schedule = topic_flow[clean_columns]
    return (clean_schedule)


def update_availability(availability_matrix, mentor_schedule,course_start_date,course,location):
    if course=="Rennes":
        delta = timedelta(140)
    else:
        delta = timedelta(230)

    if location=="HYD":
        proficiency_matrix = pd.read_csv('data/HYD_Mentor_Topic.csv',index_col=0)
    elif location=="BLR":
        proficiency_matrix = pd.read_csv('data/BLR_Mentor_Topic.csv',index_col=0)
    elif location=="MUM":
        proficiency_matrix = pd.read_csv('data/MUM_Mentor_Topic.csv',index_col=0)

    for date_idx, row in availability_matrix.iterrows():
        if date_idx >= course_start_date and date_idx < course_start_date + delta:
            for topic in availability_matrix.columns:
                available_mentors = mentor_schedule.loc[(mentor_schedule['Date']==date_idx) & (mentor_schedule['Available']==0),'Mentor'].values.tolist()
                ranked = proficiency_matrix.loc[topic].loc[available_mentors].loc[proficiency_matrix.loc[topic].loc[available_mentors]>0].sort_values(ascending=False).to_dict() 
                availability_matrix.loc[date_idx][topic] = ranked
    return(availability_matrix)


availability_topics = ['Foundations of Probability and Statistics for Data Science',
       'Statistics and Probability in Decision Modeling', 'Linear Regression',
       'Logistic Regression', 'Time Series', 'PCA', 'Regularization',
       'Naive Bayes', 'Methods and Algorithms in Machine Learning',
       'Clustering', 'Decision Trees', 'Association Rules',
       'KNN & Collabrative Filtering', 'SVM',
       'Ensembles Bagging (RF) & Boosting (GBM)', 'Architecting ML Solutions',
       'Data Management', 'AI and Decision Sciences', 'ANN', 'Deep Learning',
       'CNN', 'RNN & LSTM', 'Linear Programming',
       'Monte Carlo Simulations & Genetic Algorithm',
       'Text Mining - TF-IDF, Matrix Factorization (SVD)',
       'Text Mining - Page Rank, Text Classification & Sentiment Analysis',
       'Big Data', 'Art and Science of Data Visualisation', 'Blockchain',
       'Crypto currencies']
