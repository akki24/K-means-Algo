# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:04:23 2017

@author: Akshaykumar.Kore
"""
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics
from sklearn.metrics import accuracy_score
import numpy as np

iris=datasets.load_iris()

#indexes of test data 
test_index=[1,50,100,103,133,122,149]

train_target=np.delete(iris.target,test_index)
train_data=np.delete(iris.data,test_index,axis=0)

test_target=iris.target[test_index]
test_data=iris.data[test_index]



model=KMeans(n_clusters=3)
model.fit(train_data)
print(model.cluster_centers_)
model.labels_

#predict will return cluster index for data 
print(model.predict(test_data))

#Sum of distances of samples to their closest cluster center.
print(model.inertia_)
#print(calinski_harabaz_score(train_data, model.labels_))
'''print(accuracy_score(train_data, model.labels_,normalize=True))

print(accuracy_score(y.Targets, model.labels_,normalize=False)) 
'''


