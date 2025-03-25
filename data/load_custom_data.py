import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# define a funtion for cleaning data and clustering
def cluster_csv(data, columns: list[str]):

    X = data [columns].apply(pd.to_numeric, errors="coerce")
    X = X.dropna()


    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)

    k = 3

    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(x_scaled)

    data['cluster'] = clusters

    return data

# print(cluster_csv("../GUI/income.csv", columns=["Income($)", "Age"]))


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def cluster_excel(data, columns: list[str]):
    """
    Clusters the specified numerical columns in an Excel DataFrame.

    Parameters:
        data (pd.DataFrame): The Excel data as a DataFrame.
        columns (list[str]): List of column names to use for clustering.

    Returns:
        pd.DataFrame: The DataFrame with an added 'cluster' column.
    """

    X = data[columns].apply(pd.to_numeric, errors="coerce")
    X = X.dropna()

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)

    k = 3  # Number of clusters

    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(x_scaled)

    data["cluster"] = clusters  # Add clusters to DataFrame

    return data


