import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from collections import Counter

data = {
    'marks': [93, 85, 78, 95, 82, 95, 70, 88, 92, 75, 80, 60, 95, 86, 98, 68, 55, 74, 81, 94, 58, 62, 76, 84, 91, 52, 64, 72],
    'priority': [1.7, 1.2, 1.8, 1.0, 1.3, 0.8, 0.9, 1.4, 1.7, 1.1, 1.6, 0.7, 1.0, 1.9, 2.0, 0.6, 0.4, 1.5, 1.2, 1.8, 0.3, 0.9, 1.0, 1.7, 1.4, 0.2, 0.8, 1.3]
}

df = pd.DataFrame(data)

# Standardize marks and priority
scaler = StandardScaler()
features = scaler.fit_transform(df[['marks', 'priority']])

# KMeans++ initialization
kmeans = KMeans(n_clusters=7, random_state=0, init='k-means++')
kmeans.fit(features)

# new column
df['cluster'] = kmeans.labels_

# Count of each cluster label
cluster_counts = Counter(df['cluster'])

# Create a mapping from current labels to new labels
label_mapping = {cluster_label: i for i, cluster_label in enumerate(sorted(cluster_counts.keys()))}

# Apply the new labels to the DataFrame
df['cluster'] = df['cluster'].map(label_mapping)

df_sorted = df.sort_values(by='cluster')

print(df_sorted)
