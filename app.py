import streamlit as st
import pandas as pd
import numpy as np
import pickle 

# load model
rfr = pickle.load(open('rfr.pkl', 'rb'))
x_train = pd.read_csv('x_train.csv')

def pred(Gender,Age,Height,Weight,Duration,Heart_rate,Body_Temp):
    features = np.array([[Gender,Age,Height,Weight,Duration,Heart_rate,Body_Temp]])
    prediction = rfr.predict(features).reshape(1, -1)
    return prediction[0]

# web application title

st.title("Calories Burn Prediction App")
Gender = st.selectbox('Gender',x_train['Gender'].unique())
Age = st.selectbox('Age',x_train['Age'].unique())
Height = st.selectbox('Height',x_train['Height'].unique())
weight = st.selectbox('Weight',x_train['Weight'].unique())
Duration = st.selectbox('Duration',x_train['Duration'].unique())
Heart_Rate = st.selectbox('Heart Rate',x_train['Heart_Rate'].unique())
Body_Temp = st.selectbox('Body Temperature',x_train['Body_Temp'].unique())

result = pred(Gender,Age,Height,weight,Duration,Heart_Rate,Body_Temp)

if st.button('Predict'):
    if result:
        st.write("The predicted calories burned is: ", result)