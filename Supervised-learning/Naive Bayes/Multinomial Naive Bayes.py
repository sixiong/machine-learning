#-*- encoding:utf-8 -*-
r'''
高斯贝叶斯分类器本质是一个线性分类器，
它是贝叶斯分类器在联合概率分布满足
高斯分布的特殊情况
'''

import numpy as np
#随机生成大小为1~5之间的20行100维数据
X = np.random.randint(5, size=(20, 100))
print X
y = np.array([i+1 for i in range(20)])
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
print clf.fit(X, y)
#>>MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
test = np.random.randint(10,size=(2,100))
print test
print(clf.predict(test))


