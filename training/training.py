import numpy as np
from scipy.spatial.distance import euclidean
from collections import Counter


# Implement the k_NN algorithm
def knn_predict(X_train, y_train, X_test, k=3):
    y_pred = []
    for test_point in X_test:
        # Calculate the distance 
        # between test point and all the training points
        distances = [euclidean(test_point, train_point) for train_point in X_train]

        # get all the indices of the k nearest neigbours
        k_indices = np.argsort(distances)[:k]

        # Get the labels of the k nearest neighbours
        k_labels = [y_train[index] for index in k_indices]

        # Assign the majority class
        majority = Counter(k_labels).most_common(1)[0][0]

        y_pred.append(majority)
    
    return np.array(y_pred)

