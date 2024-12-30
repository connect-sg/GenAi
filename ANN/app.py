import streamlit as st
import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pickle

# load the trained model
model = tf.keras.models.load_model('model.h5')

# load encoder and scaler
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender = pickle.load(file)

with open('one_hot_encoder_geo.pkl','rb') as file:
    one_hot_encoder_geo = pickle.load(file) 

with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file) 


# streamlit 
st.title('Customer Churn Prediction')       

# user input
geography = st.selectionbox('Geography', one_hot_encoder_geo.catergories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.silder('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1,4)
has_cr_card = st.selectbox('Has Credit Card', [0,1])
is_active_member = st.selectbox('Is Active Member', [0,1])

input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure], 
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_cred],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

# onde hot encoder for geography
geo_encoder = one_hot_encoder_geo.transform([[geography]]).toarray()
geo_encoder_df = pd.DataFrame(geo_encoder, columns =one_hot_encoder_geo.get_feature_names_out(['Geography']))

#combine one hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop= True), geo_encoder_df], axis = 1)

# scaler
input_data = scaler.transform(input_data)

# predict
pred = model.predict(input_data)
pred = pred[0][0]

if pred >0.5:
    st.write('The customer is likely to churn')
else:
    st.write('The customer is not likely to churn')
        