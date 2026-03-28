import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(sys.argv[1])

print("🔄 Running K-Means clustering...")

#Select numeric features for clustering 
features = ["price", "freight_value", "review_score"]
features = [f for f in features if f in df.columns]

X = df[features].dropna()

#Scale the features 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means with 3 clusters 
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

df_clustered = X.copy()
df_clustered["cluster"] = kmeans.labels_

# Count samples per cluster 
cluster_counts = df_clustered["cluster"].value_counts().sort_index()

output = """K-Means Clustering Results
===========================
Number of clusters: 3
Features used: {}

Samples per cluster:
{}

Cluster Interpretation:
- Cluster 0: {} orders
- Cluster 1: {} orders
- Cluster 2: {} orders
""".format(
    ", ".join(features),
    cluster_counts.to_string(),
    cluster_counts.get(0, 0),
    cluster_counts.get(1, 0),
    cluster_counts.get(2, 0)
)

with open("clusters.txt", "w") as f:
    f.write(output)

print("✅ clusters.txt saved!")
print(output)