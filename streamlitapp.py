import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction")
st.write("Enter the details of the house to predict its price.")

#User Inputs
medinc = st.number_input("median Income",
                          min_value=0.0, value=5.0)
housage = st.number_input("House Age",
                          min_value=0.0, value=20.0)
averooms = st.number_input("Average Rooms",
                           min_value=0.0, value=5.0)
avebedrms = st.number_input("Average Bedrooms",
                            min_value=0.0, value=1.0)
population = st.number_input("Population",
                             min_value=0.0, value=1000.0)
aveoccup = st.number_input("Average Occupancy",
                           min_value=0.0, value=3.0)
latitude = st.number_input("Latitude", value=36.0)
longitude = st.number_input("Longitude", value=-119.0)

if st.button("Predict House Price"):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame([{
        "MedInc": medinc,
        "HouseAge": housage,
        "AveRooms": averooms,
        "AveBedrms": avebedrms,
        "Population": population,
        "AveOccup": aveoccup,
        "Latitude": latitude,
        "Longitude": longitude
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    price = prediction * 100000  
    # Assuming the model predicts in units of $100,000

    st.success(f"Estimated house value: ${price:.2f}")
