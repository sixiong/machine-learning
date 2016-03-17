###Naive Bayes###

Naive Bayes models can be used to tackle large scale classification problems for which the full training set might not fit in memory. To handle this case, MultinomialNB, BernoulliNB, and GaussianNB expose a partial_fit method that can be used incrementally as done with other classifiers as demonstrated in [Out-of-core classification of text documents](http://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#example-applications-plot-out-of-core-classification-py). Both discrete classifiers support sample weighting; GaussianNB does not.
Contrary to the fit method, the first call to partial_fit needs to be passed the list of all the expected class labels.

###参考链接###
[naive_bayes](http://scikit-learn.org/stable/modules/naive_bayes.html)

[平凡而又神奇的贝叶斯方法](http://mindhacks.cn/2008/09/21/the-magical-bayesian-method/)

