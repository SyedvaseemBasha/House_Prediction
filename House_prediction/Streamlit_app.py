import streamlit as st
import requests
import pickle
import numpy as np

# Load the saved models
with open('scaler.pkl', 'rb') as f:
    scaled = pickle.load(f)

with open('best_model_.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("House Price Prediction")

# Get user input
medinc = st.number_input("Median Income (1 = $100,000)", min_value=0.0, format="%.2f")
houseage = st.number_input("House Age", min_value=0, format="%d")
AveRooms = st.select_slider("Avg Rooms", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
AveBedrms = st.select_slider("Avg Bedrooms", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Population = st.number_input("Population", min_value=0, format="%d")
AveOccup = st.number_input("Average Occupancy", min_value=0.0, format="%.2f")
Latitude = st.number_input("Latitude", min_value=-150.0, format="%.2f")
Longitude = st.number_input("Longitude", min_value=-150.0, format="%.2f")


# Button to predict
if st.button("Predict Price (1 = $100,000)"):
    features = np.array([medinc, houseage, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude])

    # Remove index 3 value (AvgBedrms)
    features = np.delete(features, 3)

    # Apply log transformation on indices 2, 3, and 4
    indices_to_transform = [2, 3, 4]
    for idx in indices_to_transform:
        if idx < len(features):  # Check to avoid out-of-bounds errors
            features[idx] = np.log1p(features[idx])

    # Reshape and scale features
    features = features.reshape(1, -1)
    scaled_features = scaled.transform(features)

    # Make prediction
    prediction = model.predict(scaled_features)[0]

    # Display result
    st.success(f"Predicted Price: ${prediction:.2f}")        

