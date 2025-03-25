from sklearn.model_selection import train_test_split
import pandas as pd
from data import iris_data


# Split the data into features (X) and labels why
X = iris_data.iloc[:, :-1].values
y = iris_data.iloc[:, -1].values


# Split into Training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def data_split(data: pd.DataFrame) -> tuple:
    x = data.select_dtypes(include=["number"]).iloc[:, :-1].values
    y = data.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test


