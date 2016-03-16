from sklearn.neighbors import NearestNeighbors
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(X)
test = np.array([[0,0],[0.1,0.9]])
distances, indices = nbrs.kneighbors(test)
print indices
print distances
print nbrs.kneighbors_graph(X).toarray()

from sklearn.neighbors import KDTree
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
kdt = KDTree(X, leaf_size=30, metric='euclidean')
print kdt.query(X, k=2, return_distance=False)  
print kdt.valid_metrics        

