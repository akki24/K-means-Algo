						
											K-Means Algorithm

Clustering:
	  It is the assignment of a set of observations into subsets (called clusters) so that observations in the same cluster are similar in some sense. 
	  Clustering is a method of unsupervised learning, and a common technique for statistical data analysis used in many fields.

K-Means Clustering:
	• K-means clustering is an algorithm to classify or to group your objects based on features into K number of group. 
	  K is positive integer number.
	• The grouping is done by minimizing the sum of squares of distances between data and the corresponding cluster centroid. 
	  Thus the purpose of K-mean clustering is to classify the data.

Where To Use K_means Algo:
		• K-means clustering is a type of unsupervised learning, which is used when you have unlabeled data(i.e. data without labeled categories). 
		• Where we don't know real output(We know only x values, dont know y values).


Steps Towards Solving Clustering Problems:
	• The basic step of k-means clustering is simple. 
	  In the beginning we determine number of cluster K and we assume the centroid or center of these clusters. 
	  We can take any random objects as the initial centroids or the first K objects in sequence can also serve as the initial centroids.
	• Then the K means algorithm will do the three steps below until convergence.

		Step 1: Begin with a decision on the value of k = number of clusters.

		Step 2:	Put any initial partition that classifies the data into k clusters. 
			You may assign the training samples randomly, or systematically as the following:
			
			1) Take the first k training sample as single-element clusters.
			2) Assign each of the remaining (N-k) training sample to the cluster with the nearest centroid. 
			   After each assignment, recomputed the centroid of the gaining cluster.

		Step 3: Take each sample in sequence and compute its distance from the centroid of each of the clusters. 
			If a sample is not currently in the cluster with the closest centroid, switch this sample to that cluster and 
			update the centroid of the cluster gaining the new sample and the cluster losing the sample.

		Step 4: Repeat step 3 until convergence is achieved, that is until a pass through the training sample causes no new assignments.

	In Simple Words Steps are:
		1) Determine the centroid coordinate.
		2) Determine the distance of each object to the centroids.
		3) Group the object based on minimum distance.

 
How To Determine Number of clusters(value of k):
		1) For small range of K value( 2-10), for each K value run (20-100times), 
		   take the clustering result with the lowest J(Cost Function) value among all K values;
		2) Elbow method 
		3) GAPs.(Still working) 
		4) Decide the K down streams: decide by the purposes/goals of the projects
		

	**Cost Function:
			








	Elbow Method:




How To Calculate Accuracy(In progress not found appropriate satisfactory ans yet):
		1) Purity (working )			 

		2)sklearn.metrics.calinski_harabaz_score----
			 If the ground truth labels are not known, the Calinski-Harabaz index (sklearn.metrics.calinski_harabaz_score) can be used 
			to evaluate the model, where a higher Calinski-Harabaz score relates to a model with better defined clusters.
			For k clusters, the Calinski-Harabaz score s is given as the ratio of the between-clusters dispersion mean and the within-cluster dispersion:
			
			s(k) = \frac{\mathrm{Tr}(B_k)}{\mathrm{Tr}(W_k)} \times \frac{N - k}{k - 1}
			
		where B_K is the between group dispersion matrix and W_K is the within-cluster dispersion matrix defined by:
			W_k = \sum_{q=1}^k \sum_{x \in C_q} (x - c_q) (x - c_q)^T
			B_k = \sum_q n_q (c_q - c) (c_q - c)^T


		3) sklearn.metrics.silhouette_score(X, labels, metric='euclidean', sample_size=None, random_state=None, **kwds)[source]
				Compute the mean Silhouette Coefficient of all samples.
				The Silhouette Coefficient is calculated using the mean intra-cluster distance (a) 
				and the mean nearest-cluster distance (b) for each sample. 
				The Silhouette Coefficient for a sample is (b - a) / max(a, b). 
				To clarify, b is the distance between a sample and the nearest cluster that the sample is not a part of. 
				Note that Silhouette Coefficent is only defined if number of labels is 2 <= n_labels <= n_samples - 1.
				This function returns the mean Silhouette Coefficient over all samples. 
				To obtain the values for each sample, use silhouette_samples.
				The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters. 
				Negative values generally indicate that a sample has been assigned to the wrong cluster, 
				as a different cluster is more similar.

assumption:

1)assume balanced cluster size within the dataset;

2)assume the joint distribution of features within each cluster is spherical: this means that features within a cluster have equal variance, 
and also features are independent of each other;

3)clusters have similar density;

cons:

1) uniform effect: often produce clusters with relatively uniform size even if the input data have different cluster size;

2) spherical assumption hard to satisfied: correlation between features break it, 
 would put extra weights on correlated features(should take actions depending on the problems); 
cannot find non-convex clusters or clusters with unusual shapes;

3) different densities: may work poorly with clusters with different densities but spherical shape;

4) K value not known: how to solve K? 1)for small range of K value, say 2-10, for each K value run lots of times(20-100times), 
take the clustering result with the lowest J value among all K values; 
2) using Elbow method to decide K value; 
3) GAPs; 4)decide the K down streams: decide by the purposes/goals of the projects

5) sensitive to outliers;

6) sensitive to initial points and local optimal, and there is no unique solution for a certain K value: 
thus run K mean for a K value lots of times(20-100times), then pick the results with lowest J;

pros:

1)practically work well even some assumptions are broken;

2)simple, easy to implement;

3)easy to interpret the clustering results;

4)fast and efficient in terms of computational cost, typically O(K*n*d);










	