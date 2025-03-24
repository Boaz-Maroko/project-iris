import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from training import knn_predict
from training.testing import y_pred
from data import X_test, X_train, y_train
import seaborn as sns
from data import iris_data


# reduce dimensions to 2D for visualization
pca = PCA(n_components=2)
X_train_2d = pca.fit_transform(X_train)
X_test_2d = pca.fit_transform(X_test)


# Plot decision boundaries
x_min, x_max = X_train_2d[:, 0].min() - 1, X_train_2d[:, 0].max() + 1
y_min, y_max = X_train_2d[:, 1].min() - 1, X_train_2d[:, 1].max() + 1


xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
grid_points = np.c_[xx.ravel(), yy.ravel()]
grid_pred = knn_predict(X_train_2d, y_train, grid_points, k=3)
grid_pred = grid_pred.reshape(xx.shape)


# plt.contour(xx, yy, grid_pred, alpha=0.4)
# plt.scatter(X_train_2d[:, 0], X_train_2d[:, 1], c=y_train, s=20, edgecolor='k')
# plt.scatter(X_test_2d[:, 0], X_test_2d[:, 1], c=y_pred, s=100, marker="x", edgecolor="k")
# plt.title("k-NN Decision Boundaries")

sns.pairplot(iris_data, hue="species", markers=["o", "s", "D"])
plt.show()