# Next Word Predictor App

## Project Description

This project is a Next Word Prediction application that uses a deep learning model to predict the next word in a sentence based on the context provided by the preceding words. The application is designed to assist in text generation, autocomplete functions, and natural language processing tasks. It leverages a Long Short-Term Memory (LSTM) network, which is a type of recurrent neural network (RNN) well-suited for sequence prediction problems.

## Database Used

The application is trained on the text of *Hamlet* by William Shakespeare. This choice of dataset provides a challenging and rich source of English language structures, allowing the model to learn complex patterns in word usage and sentence formation.

## Model Architecture

The core of the application is an LSTM model. LSTMs are ideal for this task due to their ability to remember and utilize long-term dependencies in sequences of data. Unlike traditional RNNs, LSTMs can effectively handle the vanishing gradient problem, making them more efficient at learning long-range dependencies.

### Why LSTM?

LSTM was chosen for this project because of its ability to capture the context and structure of language over long sequences of text. In natural language processing, the meaning of a word often depends on the previous words, sometimes stretching back many words or even sentences. LSTM networks are designed to maintain information across these long sequences, making them particularly effective for predicting the next word in a text sequence.

Additionally, the model was trained with an early stopping mechanism. Early stopping is a form of regularization used to prevent overfitting, which occurs when a model becomes too closely fit to the training data and loses its ability to generalize to new, unseen data. By stopping the training process when performance on a validation dataset stops improving, we ensure that the model maintains good predictive power.

## Directions to Use the Predictor App

To use the Next Word Predictor app, follow these steps:

1. **Clone the Repository**: 
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/srivabhi22/next-word-predictor.git

2. **Navigate to the Project Directory**: 
   ```bash
   cd next-word-predictor

3. **Install the Required Dependencies**: 
   ```bash
   pip install -r requirements.txt

4. **Run the Predictor**: 
   ```bash
   python prediction.py

