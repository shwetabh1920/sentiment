!pip install textblob
import streamlit as st
from textblob import TextBlob
st.title('Sentiment Analysis')
st.write('Enter the text to analyze below:')
text = st.text_input('Text Input')
if st.button('Analyze Sentiment'):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        st.write('Positive')
    elif sentiment < 0:
        st.write('Negative')
    else:
        st.write('Neutral')
