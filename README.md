# 🧠 Next Word Prediction using LSTM

A Deep Learning based **Natural Language Processing (NLP)** project that predicts the **next word in a text sequence** using an **LSTM (Long Short-Term Memory) neural network**.

The model is trained on **Shakespeare's Hamlet dataset** and deployed using **Streamlit** to provide an interactive web interface.

---

## 🚀 Project Overview

Next word prediction is widely used in:

- Search engines
- Text autocomplete
- AI writing assistants
- Chatbots

This project trains an **LSTM-based language model** to learn patterns from text and predict the most probable next word based on previous words.

Example:

Input
```
To be or not to
```

Output
```
be
```

---

## 🏗️ Project Architecture

```
Dataset (Hamlet Text)
        │
        ▼
Text Preprocessing
        │
        ▼
Tokenization
        │
        ▼
Sequence Generation
        │
        ▼
LSTM Model Training
        │
        ▼
Early Stopping
        │
        ▼
Trained Model (.h5)
        │
        ▼
Streamlit Web Application
        │
        ▼
User Input → Next Word Prediction
```

---

## 📂 Project Structure

```
Text-Prediction-Using-LSTM
│
├── app.py
├── experiments.ipynb
├── hamlet.txt
├── tokenizer.pickle
├── next_word_lstm.h5
├── next_word_lstm_model_with_early_stopping.h5
├── requirements.txt
├── README.md
└── LICENSE
```

### File Description

| File | Description |
|-----|-------------|
| app.py | Streamlit web application |
| experiments.ipynb | Jupyter notebook used to train the model |
| hamlet.txt | Dataset used for training |
| tokenizer.pickle | Saved tokenizer |
| next_word_lstm.h5 | Trained LSTM model |
| next_word_lstm_model_with_early_stopping.h5 | Model trained using early stopping |
| requirements.txt | Required Python libraries |
| README.md | Project documentation |

---

## ⚙️ Technologies Used

- Python
- TensorFlow / Keras
- LSTM Neural Networks
- Natural Language Processing (NLP)
- Streamlit
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

---

## 📊 Model Details

The model uses **LSTM (Long Short-Term Memory)** networks which are designed for **sequence learning problems**.

### Key Features

- Learns sequential dependencies in text
- Handles long-term context
- Prevents overfitting using **Early Stopping**
- Predicts next word using probability distribution

---

## 🧪 Training Process

1. Load Hamlet text dataset
2. Clean and preprocess the text
3. Convert text into tokens
4. Generate input-output sequences
5. Train an LSTM model
6. Apply Early Stopping
7. Save trained model and tokenizer

---

## 💻 Installation

Clone the repository

```
git clone https://github.com/patelshweta56/Text-Prediction-Using-LSTM.git
```

Move to project directory

```
cd Text-Prediction-Using-LSTM
```

Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app

```
streamlit run app.py
```

Then open your browser

```
http://localhost:8501
```

---

## 🌐 Streamlit Deployment

Steps to deploy:

1. Push project to GitHub
2. Open **Streamlit Cloud**
3. Connect GitHub repository
4. Select **app.py**
5. Deploy the application

---

## 📈 Future Improvements

- Train on larger datasets
- Implement transformer-based models
- Improve prediction accuracy
- Add multi-word prediction
- Improve UI design
- Deploy using Docker

---

## 🎯 Use Cases

- Text autocomplete
- AI writing assistants
- Chatbots
- NLP research
- Language modeling systems

---

## 👨‍💻 Author

**Shweta Patel**

GitHub  
https://github.com/patelshweta56

---

## 📜 License

This project is licensed under the **MIT License**.
