from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import numpy as np
import pandas as pd

iris = load_iris()
X = iris.data[: -1, :]
Y = iris.target[: -1]

logistic_reg = LogisticRegression(max_iter = 1000)
logistic_reg.fit(X, Y)

species = {0 : 'Setosa', 1 : 'Versicolor', 2 : 'Virginica'}

def result(feature_1, feature_2, feature_3, feature_4):
    features = np.array([feature_1, feature_2, feature_3, feature_4]).astype(np.float64).reshape(1, -1)
    res = species[logistic_reg.predict(features)[0]]
    return res

