# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:16:22 2017

@author: Akshaykumar.Kore
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import preprocessing

from sklearn.metrics import accuracy_score

import pandas as pd
import numpy as np

iris=datasets.load_iris()

x=pd.DataFrame(iris.data)

minmax=preprocessing.MinMaxScaler(feature_range=(0,1))

scale=minmax.fit_transform(x)

x=pd.DataFrame(scale)

x.columns=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']

y=pd.DataFrame(iris.target)

y.columns=['Targets']

model=KMeans(n_clusters=3)
model.fit(x)

model.labels_
 
x['Targets']=iris.target
x['k-means predicted labels']=model.labels_
print(model.cluster_centers_)

print(model.inertia_)


colormap=np.array(['red','blue','green'])
print(plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[model.labels_],s=40))
 

plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[y.Targets],s=40)



