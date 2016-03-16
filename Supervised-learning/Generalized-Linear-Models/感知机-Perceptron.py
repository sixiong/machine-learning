import numpy as np
from sklearn.linear_model import SGDClassifier, Perceptron

r'''
特点：
二分类
特征空间线性可分
'''
X = np.array([(3,3),(4,3),[1,1]])
y = np.array(['b','b','a'])
module = Perceptron(n_iter=20,verbose=1)
print module.get_params()
module.fit(X,y)
print module.predict(np.array([(0,0),(2,10),(4,5),(1,1)]))
print module.get_params(deep=True)