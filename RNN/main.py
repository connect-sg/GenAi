# import libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

# load word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# load model
model = load_model('simple_run_imdb.h5')

def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])


def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2)+3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen = 500)

    return padded_review

def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)

    prediction = model.predict(preprocessed_input)

    sentiment = 'Positive' if prediction[0][0] >0.5 else 'Negative'

    return sentiment, prediction[0][0]


# streamlit app
import streamlit as st
st.title('IMDB movie Review sentiment analysis')
st.write('Enter a movie review to calssify it as positive or negative.')


# user input
user_input = st.text_area('Movie Review')

if st.button('classify'):
    preprocess_input = preprocess_text(user_input)

    # predict

    prediction  = model.predict(preprocess_input)
    sentiment =  'Positive' if prediction[0][0] >0.5 else 'Negative'

    st.write(f'Sentiment : {sentiment}')
    st.write(f'prediction score: {prediction[0][0]}')
else:
    st.write('Please enter a moview review')    