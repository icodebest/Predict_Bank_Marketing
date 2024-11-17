# predict.py

import joblib
import pandas as pd
from feature_processing import process_features  # Import the function from feature_processing.py

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')

# Function to make predictions
def make_prediction(input_data):
    # Step 1: Process the input features using the process_features function
    processed_data = process_features(input_data)
    
    # Step 2: Make the prediction
    prediction = model.predict(processed_data)
    
    # Step 3: Return the prediction (1 or 0 for your binary classification)
    return prediction[0]  # Returns the first prediction in case of a single input

# Example of how to use the function
if __name__ == "__main__":
    # Sample input data (replace this with your actual input)
    input_data = {
        'marital': 'single',
        'education': 'tertiary',
        'default': 'no',
        'housing': 'yes',
        'loan': 'no',
        'contact': 'cellular',
        'job': 'blue-collar',  # Choose from available jobs
        'month': 'may',  # Choose from available months
        'age': 30,  # Add the missing numerical features
        'pdays': 100,  # Add the missing numerical features
        'balance': 1500,  # Add the missing numerical features
        'campaign': 2,  # Add the missing numerical features
        'previous': 1,  # Add the missing numerical features
        'day': 5,  # Add the missing numerical features
        'duration': 200  # Add the missing numerical features
    }

    # Get the prediction
    prediction = make_prediction(input_data)
    
    # Print the prediction
    print(f"The prediction for the input data is: {'Success' if prediction == 1 else 'Failure'}")
