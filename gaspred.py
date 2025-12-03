import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ----------- CHANGE THIS PATH IF NEEDED -----------
FILE_PATH = r"C:/Users/T.Haneesh/Downloads/feeds (2).csv"
# ---------------------------------------------------

# Load CSV
df = pd.read_csv(FILE_PATH)

# We only need time and field1
df['created_at'] = pd.to_datetime(df['created_at'])
df = df[['created_at', 'field1']]

# Drop missing values if any
df = df.dropna()

# Reset index
df = df.reset_index(drop=True)

# Create X as index numbers (0,1,2,3...) and y as field1 (gas value)
X = np.array(df.index).reshape(-1, 1)
y = np.array(df['field1'])

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict next 30 values
future_index = np.array(range(len(df), len(df) + 30)).reshape(-1, 1)
future_predictions = model.predict(future_index)

# ----------- EXTRA ANALYSIS -----------
average = np.mean(y)
maximum = np.max(y)
minimum = np.min(y)
trend_slope = model.coef_[0]

# Print results
print("\n------ DATA ANALYSIS ------")
print("Average value:", average)
print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("Trend slope:", trend_slope)

print("\n------ NEXT 30 PREDICTED VALUES ------")
print(future_predictions)

# ----------- PLOT EVERYTHING -----------

plt.figure(figsize=(10,5))
plt.plot(df['field1'], label='Original Data')
plt.plot(range(len(df), len(df) + 30), future_predictions, label='Predicted (next 30)', linestyle='dashed')
plt.title("Pollution / Gas Data + Prediction")
plt.xlabel("Time Index")
plt.ylabel("Value")
plt.legend()
plt.show()
