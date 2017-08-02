# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:56:34 2017

@author: Akshaykumar.Kore
"""


import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

from sklearn.metrics import accuracy_score
from sklearn.metrics import calinski_harabaz_score
import pandas as pd
import numpy as np

#loading iris data
iris=datasets.load_iris()

x=pd.DataFrame(iris.data)
x.columns=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']

#x['Targets']=iris.target


#y=pd.DataFrame(iris.target)
#y.columns=['Targets']


model=KMeans(n_clusters=3)
model.fit(x)
model.labels_
#x['Targets']=iris.target
#x['k-means predicted labels']=model.labels_

print(model.cluster_centers_)

print(model.inertia_)
 
colormap=np.array(['red','blue','green','black','pink'])
#print(plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[model.labels_],s=40))
 
print(plt.scatter(x.Petal_Length,x.Petal_Width,c=colormap[model.labels_],s=40))
#print(accuracy_score(y.Targets, model.labels_,normalize=True))

print(calinski_harabaz_score(x, model.labels_))
#print(accuracy_score(y.Targets, model.labels_,normalize=False)) 



