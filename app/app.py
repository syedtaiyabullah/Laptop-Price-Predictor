import streamlit as st
import pickle
import numpy as np
import pandas as pd

# load model and dataframe
import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pipe = pickle.load(open(os.path.join(BASE_DIR, 'pipe.pkl'), 'rb'))
df = pickle.load(open(os.path.join(BASE_DIR, 'df.pkl'), 'rb'))

st.title("Laptop Price Predictor")

# brand
company = st.selectbox('Brand', df['Company'].unique())

# type of laptop
type_name = st.selectbox('Type', df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM (in GB)', [2,4,6,8,12,16,24,32,64])

# weight
weight = st.number_input('Weight of the Laptop (kg)', min_value=0.5, max_value=5.0)

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No','Yes'])

# IPS
ips = st.selectbox('IPS', ['No','Yes'])

# screen size
screen_size = st.slider('Screen Size (in inches)', 10.0, 18.0, 13.0)

# resolution
resolution = st.selectbox(
    'Screen Resolution',
    ['1920x1080','1366x768','1600x900','3840x2160',
     '3200x1800','2880x1800','2560x1600','2560x1440','2304x1440']
)

# cpu
cpu = st.selectbox('CPU', df['Cpu brand'].unique())

# storage
hdd = st.selectbox('HDD (in GB)', [0,128,256,512,1024,2048])
ssd = st.selectbox('SSD (in GB)', [0,8,128,256,512,1024])

# gpu
gpu = st.selectbox('GPU', df['Gpu brand'].unique())

# os
os = st.selectbox('OS', df['Os'].unique())  # Make sure column name matches exactly

if st.button('Predict Price'):

    # Convert Yes/No to 1/0
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2 + Y_res**2) ** 0.5) / screen_size

    # Create dataframe with correct column names
    query = pd.DataFrame({
        'Company': [company],
        'TypeName': [type_name],
        'Ram': [ram],
        'Weight': [float(weight)],
        'Touchscreen': [touchscreen],
        'Ips': [ips],
        'Ppi': [ppi],
        'Cpu brand': [cpu],
        'HDD': [hdd],
        'SSD': [ssd],
        'Gpu brand': [gpu],
        'Os': [os]
    })

    prediction = np.exp(pipe.predict(query)[0])

    st.title(f"The predicted price of this configuration is ₹ {int(prediction)}")