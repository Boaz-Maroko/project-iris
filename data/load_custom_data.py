import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# define a funtion for cleaning data and clustering
def cluster_csv(csv_path, columns: list[str]):

    data = pd.read_csv(csv_path)

    X = data [columns]

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)

    k = 3

    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(x_scaled)

    data['cluster'] = clusters

    


