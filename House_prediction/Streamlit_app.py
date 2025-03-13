import streamlit as st
import requests

st.title("House Price Prediction")

# Get user input
medinc = st.number_input("Median Income", min_value=0.0, format="%.2f")
houseage = st.number_input("House Age", min_value=0, format="%d")
rooms = st.number_input("Average Rooms", min_value=0.0, format="%.2f")

if st.button("Predict"):
    # Call the API
    response = requests.post("http://your-api-url.com/predict",
                             json={"features": [medinc, houseage, rooms]})
    
    if response.status_code == 200:
        st.success(f"Predicted Price: ${response.json()['predicted_price']:.2f}")
    else:
        st.error(f"Error: {response.json()['error']}")
