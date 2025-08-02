import pickle
import nltk
import numpy as np
import json
from keras.models import load_model
import random
from mountiebot.utils import clean_text, bag_of_words

# Load data files
intents_file = json.loads(open('intents/intents_file.json').read())
lem_words = pickle.load(open('data/lem_words.pkl', 'rb'))
classes = pickle.load(open('data/classes.pkl', 'rb'))
bot_model = load_model('data/chatbot_model.keras')

def class_prediction(sentence, model):
    if sentence.strip() == "":
        return [{"intent": "no_input", "probability": "1.0"}]

    p = bag_of_words(sentence, lem_words)
    result = model.predict(np.array([p]))[0]
    ER_THRESHOLD = 0.60
    f_results = [[i, r] for i, r in enumerate(result) if r > ER_THRESHOLD]
    f_results.sort(key=lambda x: x[1], reverse=True)
    intent_prob_list = []
    for i in f_results:
        intent_prob_list.append({"intent": classes[i[0]], "probability": str(i[1])})
    if not intent_prob_list:
        intent_prob_list.append({"intent": "unknown", "probability": "1.0"})
    return intent_prob_list

def get_bot_response(ints, intents):
    tag = ints[0]['intent']
    intents_list = intents['intents']
    result = "I'm sorry, I don't understand that."
    for intent in intents_list:
        if intent['tag'] == tag:
            result = random.choice(intent['responses'])
            break
    return f"MountieBot: {result}"

def bot_response(text_input):
    ints = class_prediction(text_input, bot_model)
    response = get_bot_response(ints, intents_file)
    return response

# Chat loop
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        print(bot_response(user_input))

