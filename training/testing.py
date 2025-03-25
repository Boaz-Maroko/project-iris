from sklearn.metrics import accuracy_score
from data import cluster_csv
from training import knn_predict
from data import data_split


# Get the predicted values
# y_pred = knn_predict(X_train, y_train, X_test)

# data = cluster_csv("../GUI/income.py")

# calculate the acurracy score
def check_accuracy(y_test, y_pred) -> int:
    accuracy = accuracy_score(y_test, y_pred)

    return f"{accuracy * 100:.2f}%"
    