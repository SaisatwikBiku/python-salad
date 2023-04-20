# import necessary libraries to implement Random Forest Regressor as the engine of the model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# Load the CSV file as the Data Frame
df = pd.read_csv("Queries.csv")

# Split the data into input (X) and target (y) variables
X = df["Top queries"]
y = df[["Clicks", "Impressions"]]

# Split the data into train and test variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the input data to convert them into required data format
vectorizer = TfidfVectorizer()
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Scale the target data
# z-score normalization
scaler = StandardScaler()
y_train_scaled = scaler.fit_transform(y_train)
y_test_scaled = scaler.transform(y_test)

# Train the Random Forest Regressor model
engine = RandomForestRegressor(n_estimators=100, random_state=42)
engine.fit(X_train_vect, y_train_scaled)

# Take input from the user
query = input("Enter a query: ")

# Vectorize the user input
query_vect = vectorizer.transform([query])

# Predict Clicks and Impressions for the user input
y_pred_scaled = engine.predict(query_vect)
y_pred = scaler.inverse_transform(y_pred_scaled)

# Print predicted Clicks and Impressions
print("Predicted Clicks: ", int(y_pred[0, 0]))
print("Predicted Impressions: ", int(y_pred[0, 1]))

# Calculate and print accuracy metrics
y_test_pred_scaled = engine.predict(X_test_vect)
y_test_pred = scaler.inverse_transform(y_test_pred_scaled)
print("Accuracy: ", r2_score(y_test, y_test_pred))
print("Mean Absolute Error: ", mean_absolute_error(y_test, y_test_pred))