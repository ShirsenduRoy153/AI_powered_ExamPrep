import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from datetime import datetime

# Sample dataset with timestamps
data = {
    'timestamp': ['2022-01-01 10:00:00', '2022-01-02 10:30:00', '2022-01-03 15:45:00', '2022-01-04 14:00:00',
                  '2022-01-05 10:30:00', '2022-01-06 10:15:00', '2022-01-07 09:45:00', '2022-01-08 20:00:00',
                  '2022-01-09 1:30:00', '2022-01-10 10:20:00'],  
    'stress_level': [3, 4, 2, 1, 1, 1, 4, 2, 5, 1],  
    'concentration_level': [8, 7, 9, 10, 10, 8, 7, 9, 6, 10],  
    'study_time': [60, 45, 90, 50, 120, 55, 70, 100, 40, 110],  
}

df = pd.DataFrame(data)

# Convert timestamp strings to datetime objects
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Step 1: Feature Engineering
df['hour_of_day'] = df['timestamp'].dt.hour  # Extract hour of the day as a feature

features = df[['stress_level', 'concentration_level', 'hour_of_day']]

# Step 2: Define Target Variable
target = df['study_time']

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 4: Choose Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Step 5: Train the Model
model.fit(X_train, y_train)

# Step 6: Evaluate the Model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Step 7: Optimal Study Time Prediction
# You can now use the trained model to predict the optimal study time for new data

# For example, if you have a new set of features:
new_data = pd.DataFrame({'stress_level': [3], 'concentration_level': [8], 'hour_of_day': [12]})
predicted_study_time = model.predict(new_data)

# Format the output as "HH:MM:SS"
formatted_time = datetime.strptime('00:00:00', '%H:%M:%S') + pd.to_timedelta(predicted_study_time[0], unit='m')
formatted_time_str = formatted_time.strftime('%H:%M:%S')

print(f'Predicted Optimal Study Time: {formatted_time_str}')
