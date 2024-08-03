# MountieBot

## Overview

MountieBot is a chatbot built using Python, TensorFlow, and NLTK. It processes user inputs, predicts the intent, and provides appropriate responses based on predefined intents and responses stored in a JSON file. This README provides a comprehensive guide on how to set up, train, and run MountieBot.

## Features

- Tokenizes and lemmatizes input text for processing.
- Utilizes a neural network model for intent classification.
- Generates responses based on the predicted intent.
- Saves and loads model and data for efficient use.

## Setup

### Prerequisites

Before running MountieBot, ensure you have the following installed:

- Python 3.x
- NLTK
- TensorFlow
- Keras
- NumPy

You can install the required Python packages using pip:

```sh
pip install numpy nltk tensorflow keras
```

### Download NLTK Data

MountieBot requires specific NLTK data packages. Downlaod them using the following comands:

```sh
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

## Training the Model

During training, the script will:

- Load and process the intents from the JSON file.
- Tokenize and lemmatize the patterns.
- Create training data.
- Build and train the neural network model.
- Save the lemmatized words, classes, and trained model.

## Running the Chatbot
After training, the script enters a chat loop where it continuously takes user input and responds accordingly.

## Improvements
Since the bot relies on predefined responses, I am currently expanding the intents file to accommodate more user inputs.
