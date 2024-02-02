import pandas as pd
from sklearn.cluster import KMeans

# Load the data set
data = {
    'timestamp': ['2022-01-01 13:00:00', '2022-01-02 10:30:00', '2022-01-03 15:45:00', '2022-01-04 14:00:00',
                  '2022-01-06 13:30:00', '2022-01-06 1:15:00', '2022-01-07 09:45:00', '2022-01-08 20:00:00',
                  '2022-01-09 13:30:00', '2022-01-10 1:20:00'],  
    'stress_level': [3, 1, 2, 5, 1, 3, 4, 2, 5, 1],  
    'concentration_level': [8, 10, 9, 6, 10, 8, 7, 9, 6, 10],  
    'study_time': [60, 90, 90, 50, 20, 55, 70, 100, 40, 110],  # in minutes
    'marks': [80, 95, 95, 85, 5, 8, 75, 90, 85, 5],  # exam marks
}
df = pd.DataFrame(data)

# Convert the timestamp column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract the hour of the day from the timestamp column
df['hour'] = df['timestamp'].dt.hour

# Group the data into 3 clusters using K-means clustering
X = df[['hour', 'stress_level', 'concentration_level', 'study_time']]
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
df['cluster'] = kmeans.labels_

# Analyze the clusters to identify the best time of day to study and the amount of time you should study
for i in range(3):
    cluster_df = df[df['cluster'] == i]
    avg_study_time = cluster_df['study_time'].mean()
    avg_hour = cluster_df['hour'].mean()
    if avg_hour < 12:
        time_of_day = 'AM'
    else:
        time_of_day = 'PM'
    print(f"Cluster {i}: Study for {avg_study_time:.0f} minutes around {avg_hour % 12:.0f}:00 {time_of_day}")
