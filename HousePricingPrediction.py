# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -----------------------------
# 1️⃣ Load the dataset
# -----------------------------
# Example CSV: house_prices.csv with columns - Area, Bedrooms, Age, Price
data = pd.read_csv("./housing.csv")

# Show basic info
print("Dataset Preview:")
print(data.head())

# -----------------------------
# 2️⃣ Handle missing values
# -----------------------------
data = data.dropna()

# -----------------------------
# 3️⃣ Define features and target
# -----------------------------
X = data[['Area', 'Bedrooms', 'Age']]   # independent variables
y = data['Price']                        # dependent variable

# -----------------------------
# 4️⃣ Split data into training and testing sets
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# 5️⃣ Create and train the Random Forest model
# -----------------------------
model = RandomForestRegressor(
    n_estimators=100,     # number of trees
    random_state=42,
    max_depth=None,
    min_samples_split=2
)

model.fit(X_train, y_train)

# -----------------------------
# 6️⃣ Make predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# 7️⃣ Evaluate model performance
# -----------------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Evaluation:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# -----------------------------
# 8️⃣ Predict for a new sample
# -----------------------------
# Example: Area = 2500 sq.ft, Bedrooms = 4, Age = 5 years
new_house = pd.DataFrame([[2500, 4, 5]], columns=['Area', 'Bedrooms', 'Age'])
predicted_price = model.predict(new_house)

print(f"\n🏡 Predicted price for {new_house.values.tolist()[0]}: ₹{predicted_price[0]:,.2f}")
