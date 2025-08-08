import os
import numpy as np
import nltk
import json
import pickle
import random
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from .utils import clean_text

# Download NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INTENTS_PATH = os.path.join(BASE_DIR, 'intents', 'intents_file.json')
DATA_DIR = os.path.join(BASE_DIR, 'data')

def load_intents(file_path):
    with open(file_path) as file:
        return json.load(file)

def process_patterns(intents):
    tokenized_words = []
    classes = []
    documents = []
    ignoring_words = ['?', '!', ',', '.']

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            words = nltk.word_tokenize(pattern)
            tokenized_words.extend(words)
            documents.append((words, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    lemmatized_words = sorted(
        list(set([word.lower() for word in tokenized_words if word not in ignoring_words]))
    )
    lemmatized_words = sorted(list(set(clean_text(" ".join(lemmatized_words)))))
    classes = sorted(list(set(classes)))

    return lemmatized_words, classes, documents

def create_training_data(lemmatized_words, classes, documents):
    training_data = []
    empty_array = [0] * len(classes)

    for doc in documents:
        pattern_words = clean_text(" ".join(doc[0]))
        bag_of_words = [1 if w in pattern_words else 0 for w in lemmatized_words]

        output_row = list(empty_array)
        output_row[classes.index(doc[1])] = 1
        training_data.append([bag_of_words, output_row])

    random.shuffle(training_data)

    train_x = np.array([item[0] for item in training_data])
    train_y = np.array([item[1] for item in training_data])

    return train_x, train_y

def build_model(input_shape, output_shape):
    model = Sequential()
    model.add(Dense(128, input_shape=(input_shape,), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(output_shape, activation='softmax'))

    sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    return model

def main():
    intents = load_intents(INTENTS_PATH)
    lemmatized_words, classes, documents = process_patterns(intents)

    pickle.dump(lemmatized_words, open(os.path.join(DATA_DIR, 'lem_words.pkl'), 'wb'))
    pickle.dump(classes, open(os.path.join(DATA_DIR, 'classes.pkl'), 'wb'))

    train_x, train_y = create_training_data(lemmatized_words, classes, documents)

    model = build_model(len(train_x[0]), len(train_y[0]))
    model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

    model.save(os.path.join(DATA_DIR, 'chatbot_model.keras'))

if __name__ == "__main__":
    main()
