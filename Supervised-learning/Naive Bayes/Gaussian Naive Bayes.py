#-*- encoding:utf-8 -*-
r'''
高斯贝叶斯分类器本质是一个线性分类器，
它是贝叶斯分类器在联合概率分布满足
高斯分布的特殊情况
'''
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
print clf.fit(X, Y)
#>>GaussianNB()
print(clf.predict([[-0.8, -1],[2,4]]))
#>>[1 2]


#批量训练，即将数据集分成一块块，对于大数据集十分有效
clf_pf = GaussianNB()
print clf_pf.partial_fit(X, Y,np.unique(Y))
#>>GaussianNB()
print(clf_pf.predict([[-0.8, -1],[2,4]]))
#>>[1 2]