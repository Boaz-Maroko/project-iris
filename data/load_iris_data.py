import pandas as pd
from sklearn.datasets import load_iris


# Load the iris data set

iris = load_iris()

# Convert the dataset into a pandas Dataframe
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_data['species'] = iris.target

iris_data['species'] = iris_data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
