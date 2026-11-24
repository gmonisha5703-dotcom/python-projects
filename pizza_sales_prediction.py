# Pizza Sales Prediction Project

import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample Pizza Sales Dataset
data = {
    "Advertising": [100, 200, 300, 400, 500, 600],
    "Price": [200, 190, 180, 170, 160, 150],
    "Sales": [50, 80, 120, 150, 190, 230]
}

df = pd.DataFrame(data)

print("===== PIZZA SALES DATA =====")
print(df)

# Input and Output
X = df[["Advertising", "Price"]]
y = df["Sales"]

# Train Machine Learning Model
model = LinearRegression()
model.fit(X, y)

# Predict Future Sales
new_data = pd.DataFrame({
    "Advertising": [700],
    "Price": [140]
})

prediction = model.predict(new_data)

print("\n===== SALES PREDICTION =====")
print("Advertising Budget: 700")
print("Pizza Price: 140")
print("Predicted Pizza Sales:", round(prediction[0], 2))

print("\nPrediction Completed Successfully!")
