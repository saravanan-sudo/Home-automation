import datetime
import json
import random

import pyjokes
import pywhatkit
import torch

from audio2 import take_command
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

import pyttsx3

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Friday"


def talk(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # changing index changes voices but ony 0 and 1 are working here
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 30)
    engine.say(command)
    engine.runAndWait()


# sentence = "do you use credit cards?"

sentence = take_command()
if 'play' in sentence:
    song = sentence.replace('play', '')
    talk('playing the ' + song + 'in Youtube')
    pywhatkit.playonyt(song)
    exit()
elif 'time' in sentence:
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)
    print('Current time is ' + time)
    exit()
elif 'who is' in sentence:
    person = sentence.replace('who the heck is', '')
    info = sentence.summary(person, 1)
    print(info)
    talk(info)
    exit()
    exit()
elif 'are you single' in sentence:
    talk('I am in a relationship with wifi')
    exit()
elif 'joke' in sentence:
    talk(pyjokes.get_joke())
    exit()

sentence = tokenize(sentence)
X = bag_of_words(sentence, all_words)
X = X.reshape(1, X.shape[0])
X = torch.from_numpy(X).to(device)

output = model(X)
_, predicted = torch.max(output, dim=1)

tag = tags[predicted.item()]

probs = torch.softmax(output, dim=1)
prob = probs[0][predicted.item()]
if prob.item() > 0.75:
    for intent in intents['intents']:
        if tag == intent["tag"]:
            voiceout = random.choice(intent['responses'])
            test = f"{bot_name}: {voiceout}"
            print(test)
            talk(voiceout)
else:
    dont = "I do not understand..."
    print(f"{bot_name}: {dont} ")
    talk(dont)

