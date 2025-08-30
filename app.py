

import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

#Load trained model

model = load_model("sentiment_model.h5")



word_index = imdb.get_word_index()
index_word = {v+3: k for k, v in word_index.items()}
index_word[0] = "<PAD>"
index_word[1] = "<START>"
index_word[2] = "<UNK>"


#Function to encode review

def encode_review(text, maxlen=200):
    words = text.lower().split()
    encoded = [1]  
    for w in words:
        if w in word_index and word_index[w] < 10000:
            encoded.append(word_index[w] + 3)
        else:
            encoded.append(2)  
    return pad_sequences([encoded], maxlen=maxlen)


#Streamlit UI

st.title("🎬 FlickMood – Movie Review Sentiment AI")
st.write("Type a movie review below and see if it's Positive or Negative!")

review = st.text_area("Enter your movie review here:")

if st.button("Predict"):
    if review.strip() == "":
        st.warning("Please enter a review first!")
    else:
        seq = encode_review(review)
        prediction = model.predict(seq)[0][0]
        sentiment = "Positive ✅" if prediction > 0.5 else "Negative ❌"
        st.success(f"Prediction: **{sentiment}** (Confidence: {prediction:.2f})")
