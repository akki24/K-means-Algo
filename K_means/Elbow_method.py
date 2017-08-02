# -*- coding: utf-8 -*-
"""
Created on Wed May 31 09:26:47 2017

@author: Akshaykumar.Kore
"""


from sklearn import datasets
import numpy as np
from scipy.cluster.vq import kmeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

data=datasets.load_iris()

original=data.data

print(original)

K = range(1,10)

# scipy.cluster.vq.kmeans
KM = [kmeans(original,k) for k in K]
centroids = [cent for (cent,var) in KM]   # cluster centroids

D_k = [cdist(original, cent, 'euclidean') for cent in centroids]
cIdx = [np.argmin(D,axis=1) for D in D_k]
dist = [np.min(D,axis=1) for D in D_k]
avgWithinSS = [sum(d)/original.shape[0] for d in dist]

##### plot ###
kIdx = 2

# elbow curve
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, avgWithinSS, 'b*-')
ax.plot(K[kIdx], avgWithinSS[kIdx], marker='o', markersize=12, 
    markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Average within-cluster sum of squares')
plt.title('Elbow for KMeans clustering')

# scatter plot
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(X[:,2],X[:,1], s=30, c=cIdx[k])
clr = ['b','g','r','c','m','y','k']
for i in range(K[kIdx]):
    ind = (cIdx[kIdx]==i)
    ax.scatter(original[ind,2],original[ind,1], s=30, c=clr[i], label='Cluster %d'%i)
plt.xlabel('Petal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Dataset, KMeans clustering with K=%d' % K[kIdx])
plt.legend()

plt.show()