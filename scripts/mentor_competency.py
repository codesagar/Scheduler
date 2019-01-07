#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:44:28 2018

@author: sagar
"""

import pandas as pd
import numpy as np


internal= ['Dr. Dakshinamurthy Kolluru','Dr. Sridhar Pappu','Dr. Surya Kompalli','Dr. Praphul Chandra',
           'Dr. Manoj Duse','Dr. Anand Narasimhamurthy','Dr. Rohit Lotlikar','Dr. Kishore Konda',
           'Dr. Ventakesh Sunkad','Dr. Anand Jayaraman']

base = {'Not Comfortable':0,'Comfortable':1,'Proficient':2,'Expert':3}

near_factor = 2.1
# Try 1.6 or 2.1 for different solution

near = {key: value * near_factor for key,value in base.items()}
near['Distance'] = "Near"

far = base.copy()
far['Distance'] = "Far"

contingency = pd.DataFrame(columns=['Distance','Not Comfortable','Comfortable','Proficient','Expert'], data=[far,near])

contingency_melted = pd.melt(contingency, id_vars='Distance', value_vars=['Not Comfortable','Comfortable','Proficient','Expert'], var_name='Proficiency', value_name='Score')

topics_proficiency = pd.read_csv('data/Topics-Proficiency-Modified-3.csv',index_col = 1)

HYD = ["Dr. Dakshinamurthy Kolluru","Dr. Sridhar Pappu","Dr. Surya Kompalli",
             "Dr. Kishore Konda","Dr. Sreerama Murthy","Dr. Anand Jayaraman","Dr. Manish Gupta"]


hyd_matrix = topics_proficiency.copy()
blr_matrix = topics_proficiency.copy()
mum_matrix = topics_proficiency.copy()

hyd_matrix = hyd_matrix.replace(['nan',np.nan],0)
hyd_matrix.loc[:,HYD]=hyd_matrix.loc[:,HYD].replace(near)
hyd_matrix.loc[:,hyd_matrix.columns.difference(HYD)] = hyd_matrix.loc[:,hyd_matrix.columns.difference(HYD)].replace(far)
hyd_matrix[internal] = hyd_matrix[internal] * 1.6
hyd_matrix.to_csv('data/HYD_Mentor_Topic.csv')


blr_matrix = blr_matrix.replace(['nan',np.nan],0)
blr_matrix.loc[:,HYD]=blr_matrix.loc[:,HYD].replace(far)
blr_matrix.loc[:,blr_matrix.columns.difference(HYD)] = blr_matrix.loc[:,blr_matrix.columns.difference(HYD)].replace(near)
blr_matrix[internal] = blr_matrix[internal] * 1.6
blr_matrix.to_csv('data/BLR_Mentor_Topic.csv')

mum_matrix = mum_matrix.replace(['nan',np.nan],0)
mum_matrix = mum_matrix.replace(base)
mum_matrix[internal] = mum_matrix[internal] * 1.6
blr_matrix.to_csv('data/MUM_Mentor_Topic.csv')
