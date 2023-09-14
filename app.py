import streamlit as st 
import pandas as pd
import numpy as np
import pickle

# Load the model
model_path = "finalized_model.pkl"
with open (model_path, "rb") as model_file:
  model = pickle.load(model_file)

# Create a Streamlit app and add input fields for TV, radio, and newspaper advertising
st.title('💰Video Games Sales Prediction')
st.write("*Developed for 🌎 with ❤️‍🔥 by Muhammad Ahsan👨🏻‍💻🇵🇰*")
st.write('Enter the advertising budget below to predict sales.')

# Taking the input from user
new_tv = st.number_input('TV Advertising', min_value=0.0, max_value=1000.0, step=0.1)
new_radio = st.number_input('Radio Advertising', min_value=0.0, max_value=1000.0, step=0.1)
new_newspaper = st.number_input('Newspaper Advertising', min_value=0.0, max_value=1000.0, step=0.1)

# Button to trigger the prediction
if st.button('Predict'):
    new_value = pd.DataFrame([[new_tv, new_radio, new_newspaper]])
    new_value_scaled = scaler.transform(new_value)
    prediction = model.predict(new_value_scaled)
    st.markdown(f"Prediction result: **{prediction[0]}**")


