from sklearn.metrics import accuracy_score
from data import X_train, X_test, y_train, y_test
from training import knn_predict


# Get the predicted values
y_pred = knn_predict(X_train, y_train, X_test)


# calculate the acurracy score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")