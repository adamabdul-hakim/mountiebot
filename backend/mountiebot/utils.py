import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np

# Initialize once
lemmatizer = WordNetLemmatizer()

def clean_text(text_in):
    """Tokenize and lemmatize a string."""
    words = nltk.word_tokenize(text_in)
    return [lemmatizer.lemmatize(word.lower()) for word in words]

def bag_of_words(text_in, vocabulary):
    """Convert input sentence into a bag-of-words numpy array."""
    sentence_words = clean_text(text_in)
    bag = [1 if word in sentence_words else 0 for word in vocabulary]
    return np.array(bag)
