import streamlit as st 
import pandas as pd
import numpy as np
import pickle

# Load the model
model_path = "finalized_model.pkl"
with open (model_path, "rb") as model_file:
  model = pickle.load(model_file)
