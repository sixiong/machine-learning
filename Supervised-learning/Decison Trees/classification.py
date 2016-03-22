# encoding=utf-8
'''
二分类
'''
from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

print clf.predict([[2.,2.]])
print clf.predict_proba([[2.,2.],[0.8,0.8]])

'''
多分类
'''
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

from sklearn.externals.six import StringIO
with open("iris.dot", 'w') as f:
	f = tree.export_graphviz(clf, out_file=f)

from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("iris.pdf")

from IPython.display import Image  
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
						feature_names=iris.feature_names,  
						class_names=iris.target_names,  
						filled=True, rounded=True,  
						special_characters=True)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())  