# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 12:28:17 2017

@author: Akshaykumar.Kore
"""


import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np


location=r'C:\transauminesexpactivity.csv'
df=pd.read_csv(location)
df1 = df[['Unique_Advisor_Id','Unique_Investment_Id','Month']]
df.convert_objects(convert_numeric=True)
df.fillna(0,inplace=True)

df=df.drop(['Unique_Advisor_Id','Unique_Investment_Id','Month','Unnamed: 0','Unnamed: 5','Unnamed: 6'],1)

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



minmax=preprocessing.MinMaxScaler(feature_range=(0,1))


scale=minmax.fit_transform(df)

x=pd.DataFrame(scale)

result = pd.concat([df1, x], axis=1)

model=KMeans(n_clusters=2)
model.fit(x)

model.labels_
 
print(model.cluster_centers_)

print(model.inertia_)
colormap=np.array(['red','blue','green','black','pink'])
#print(plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[model.labels_],s=40))
 
print(plt.scatter(result.Unique_Advisor_Id,result.Unique_Investment_Id,c=colormap[model.labels_],s=40))
plt.xlabel('Advisor Id')
plt.ylabel('Investment Id')
plt.title('Invesco Dataset, KMeans clustering with K=%d')
plt.legend()

plt.show()
