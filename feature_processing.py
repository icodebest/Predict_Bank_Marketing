# feature_processing.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

# Load the saved scaler and label encoder
scaler = joblib.load('scaler.pkl')  # Ensure you save the scaler during training

# Function to process features and return scaled data
def process_features(input_features):
    # Mapping for label encoding
    categorical_mappings = {
        'marital': {'single': 0, 'married': 1, 'divorced': 2},
        'education': {'secondary': 0, 'tertiary': 1, 'primary': 2},
        'default': {'yes': 1, 'no': 0},
        'housing': {'yes': 1, 'no': 0},
        'loan': {'yes': 1, 'no': 0},
        'contact': {'cellular': 1, 'telephone': 0}
    }

    # Convert categorical features using mappings
    for feature, mapping in categorical_mappings.items():
        if input_features[feature] in mapping:
            input_features[feature] = mapping[input_features[feature]]

    # One hot encoding for job and month
    job_mapping = {
        'blue-collar': 0, 'entrepreneur': 1, 'housemaid': 2, 'management': 3,
        'retired': 4, 'self-employed': 5, 'services': 6, 'student': 7, 
        'technician': 8, 'unemployed': 9
    }
    month_mapping = {
        'aug': 0, 'dec': 1, 'feb': 2, 'jan': 3, 'jul': 4, 'jun': 5, 
        'mar': 6, 'may': 7, 'nov': 8, 'oct': 9, 'sep': 10
    }

    # One-hot encoding for job and month
    input_features['job_' + input_features['job']] = 1
    for job in job_mapping.keys():
        if job != input_features['job']:
            input_features['job_' + job] = 0

    input_features['month_' + input_features['month']] = 1
    for month in month_mapping.keys():
        if month != input_features['month']:
            input_features['month_' + month] = 0

    # Convert input features to DataFrame
    input_df = pd.DataFrame([input_features])

    # Ensure that the input features have the same order as when the scaler was fitted
    input_df = input_df.reindex(columns=scaler.feature_names_in_, fill_value=0)

    # Apply the saved scaler
    input_scaled = scaler.transform(input_df)

    return input_scaled
