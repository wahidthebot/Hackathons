from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime

app = Flask(__name__)

# Generate a date range for one year (e.g., 2024)
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

# Generate synthetic temperature data
np.random.seed(0)  # For reproducibility
temperatures = []

for date in dates:
    if date.month in [12, 1, 2]:  # Winter
        temp = np.random.randint(50, 60)  # Winter temperatures
    elif date.month in [3, 4, 5]:  # Spring
        temp = np.random.randint(78, 85)  # Spring temperatures
    elif date.month in [6, 7, 8]:  # Summer
        temp = np.random.randint(81, 95)  # Summer temperatures
    elif date.month in [9, 10, 11]:  # Fall
        temp = np.random.randint(60, 70)  # Fall temperatures
    temperatures.append(temp)

# Create DataFrame
data = {
    'Date': dates,
    'Temperature': temperatures
}

df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())

# Save the DataFrame to a CSV file (optional)
df.to_csv('ny_weather_data.csv', index=False)



df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df['DayOfYear'] = df['Date'].dt.dayofyear

# Create and train the linear regression model
X = df[['DayOfYear']]
y = df['Temperature']
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return render_template('weather_predictor.html')

@app.route('/predict', methods=['POST'])
def predict():
    days_ahead = request.json.get('days_ahead', 1)
    print("Days ahead received:", days_ahead)  # Log for debugging

    # Calculate the target day
    current_day_of_year = datetime.now().timetuple().tm_yday
    target_day = current_day_of_year + days_ahead
    print("Target day:", target_day)  # Log the target day

    # Validate target_day
    if target_day <= 0 or target_day > 366:
        return jsonify({'error': 'Invalid day of year'})

    try:
        prediction = model.predict(np.array([[target_day]]))
        print("Raw Prediction:", prediction)  # Log the raw prediction

        # Adjust for seasonal temperature
        current_month = datetime.now().month
        seasonal_adjustment = 0

        if current_month in [12, 1, 2]:  # Winter
            seasonal_adjustment = -15  # Decrease in winter
        elif current_month in [3, 4, 5]:  # Spring
            seasonal_adjustment = -5  # Mild increase in spring
        elif current_month in [6, 7, 8]:  # Summer
            seasonal_adjustment = 10  # Increase in summer
        elif current_month in [9, 10, 11]:  # Fall
            seasonal_adjustment = 5  # Mild increase in fall

        adjusted_prediction = prediction[0] + seasonal_adjustment
        print("Adjusted Prediction:", adjusted_prediction)  # Log the adjusted prediction
        return jsonify({'predicted_temperature': adjusted_prediction})

    except Exception as e:
        print("Error during prediction:", e)  # Log the exception
        return jsonify({'error': 'Error in prediction. Please try again.'})



if __name__ == '__main__':
    app.run(debug=True)
