import streamlit as st
from transformers import pipeline

# Load sentiment analysis model
classifier = pipeline("sentiment-analysis")

st.title("Sentiment Analysis App")
st.write("Enter a sentence and let BERT analyze its sentiment!")

text = st.text_area("Enter text:", "")

if st.button("Analyze"):
    if text:
        result = classifier(text)
        st.write(f"**Sentiment:** {result[0]['label']} (Score: {result[0]['score']:.2f})")
    else:
        st.warning("Please enter text to analyze.")
