import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import streamlit as st
import matplotlib.pyplot as plt
import pickle

sentence = "Enter Claudius King of "
model = load_model("next_word_lstm_model_with_early_stopping.h5")

with open('tokenizer.pickle','rb') as handle:
    tokenizer=pickle.load(handle)

print(model.summary())

def preprocessing_text(tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len-1):]  # Ensure the sequence length matches max_sequence_len-1
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    print("Preprocessed text is:")
    print("\n")
    print(token_list)
    print("\n")
    return token_list

def predict_next_word(text, tokenizer, model):
    max_sequence_len = model.input_shape[1] + 1
    token_list = preprocessing_text(tokenizer=tokenizer, text=text, max_sequence_len=max_sequence_len)
    predicted = model.predict(token_list, verbose=0)
    print(predicted)
    predicted_word_index = np.argmax(predicted, axis=1)
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

st.title("Next Word Predictior")
input_text=st.text_input("Enter the sequence of Words","To be or not to")
if st.button("Predict Next Word"):
    next_word = predict_next_word(text=input_text, tokenizer=tokenizer, model=model)
    st.write(f'Next word: {next_word}')
