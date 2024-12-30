import streamlit as st

st.title('streamlit Text input')

name = st.text_input('Enter your name:')

age = st.slider('select your age:', 0, 100,10)
st.write(f"age, {age}")

options = ['Python', 'Java', 'C++', 'JS']
choice = st.selectbox("Choose your favorite language:", options)
st.write(f'your selected {choice}.')

if name:
    st.write(f"Hello , {name}")

uploaded_file = st.file_uploader("Choose a CSV file", type= 'CSV')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)    