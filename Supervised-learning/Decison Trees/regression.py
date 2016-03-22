# encoding=utf-8
'''
与分类不同的是，其y值可以为非整形
'''
from sklearn import tree
X = [[0, 0], [2, 2]]
y = [0.5, 2.5]
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, y)
print clf.predict([[1.8,1.3]])

'''
y值也可以为多维数据
'''
from sklearn import tree
X = [[0, 0], [2, 2]]
y = [[-1.,-1.],[1.,1.]]
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, y)
print clf.predict([[1.8,1.3]])