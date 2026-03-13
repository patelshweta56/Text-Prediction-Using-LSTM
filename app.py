import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Page configuration
st.set_page_config(
    page_title="Next Word Prediction",
    page_icon="🧠",
    layout="centered"
)


# Load model and tokenizer with caching
@st.cache_resource
def load_resources():
    model = load_model("next_word_lstm_model_with_early_stopping.h5")

    with open("tokenizer.pickle", "rb") as f:
        tokenizer = pickle.load(f)

    return model, tokenizer


model, tokenizer = load_resources()


# Function to predict next word
def predict_next_word(model, tokenizer, text, max_sequence_len):

    token_list = tokenizer.texts_to_sequences([text])[0]

    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len - 1):]

    token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')

    predicted = model.predict(token_list, verbose=0)

    predicted_word_index = np.argmax(predicted, axis=1)[0]

    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word

    return ""


# App UI
st.title("🧠 Next Word Prediction using LSTM")

st.write(
    "Enter a sequence of words and the model will predict the **next most probable word**."
)

input_text = st.text_input(
    "Enter text sequence:",
    "To be or not to"
)


if st.button("Predict Next Word"):

    if input_text.strip() == "":
        st.warning("⚠ Please enter some text.")

    else:
        max_sequence_len = model.input_shape[1] + 1

        next_word = predict_next_word(
            model,
            tokenizer,
            input_text,
            max_sequence_len
        )

        st.success(f"Predicted Next Word: **{next_word}**")


st.markdown("---")

st.caption(
    "Built using LSTM Neural Networks | Streamlit | TensorFlow"
)
