# -*- coding: utf-8 -*-
"""
Created on Wed May 24 19:25:09 2017

@author: Akshaykumar.Kore
"""
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

location=r'C:\[UCI] AAAI-14 Accepted Papers - Papers.csv'
df=pd.read_csv(location)
df.convert_objects(convert_numeric=True)
df.fillna(0,inplace=True)
#print(df)
'''
#df.drop(['title'],1,inplace=True)
#Replace the missing data with -9999 because most algos identify that as an outlier
#x=np.array(df.drop(['Index'],1).astype(float))
#model=KMeans(n_clusters=6)
#var=model.fit(x)
#print(var)'''

def handle_non_numerical_data(df):
    columns=df.columns.values
    
    for column in columns:
        text_digit_vals={}
        def convert_to_int(val):
            return text_digit_vals[val]
        if df[column].dtype !=np.int64 and df[column].dtype != np.float64:
            column_contents=df[column].values.tolist()
            unique_elements=set(column_contents)
            x=0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique]=x
                    x+=1
                    
            df[column]=list(map(convert_to_int,df[column]))
    return df
        
        
df=handle_non_numerical_data(df)
#print(df)

x=np.array(df.drop(['title'],1))

model=KMeans(n_clusters=2)
var=model.fit(x)

print(model.labels_,model.inertia_)

#print(calinski_harabaz_score(x, model.labels_))
        
        
        
        
        
        
        
        
        
        
        
        