import random
import json

import torch

from datetime import datetime


from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

sk1 = False
sk2 = False
sk3 = False
sk4 = False
sk5 = False
sk6 = False


sk11 = False
sk12 = False
sk13 = False

skillsarray = []
questiontime = " "
questiontimearray = []


def checkskills():
    if sk11 is True and sk12 is True and sk13 is True:
        skillsarray.append("Work under pressure")


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

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

currentQ = ""
t = ""
bot_name = "HR Bot"
print("Let's chat! (type 'quit' to exit)")
while True:


    sentence = input("You: ")
    # print(currentQ)
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    dt_object = datetime.fromtimestamp(timestamp)
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    print("you answered at =", dt_object)
    questiontime = t + " " + date_time
    questiontimearray.append(questiontime)

    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    #t1 = t[predicted.item()]

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                t = intent["tag"]
                print(f"{bot_name}: {random.choice(intent['responses'])}")
                print(t)
                currentQ = random.choice(intent['responses'])
                if tag == "question2":
                    sk11 = True
                    checkskills()
                    #skillsarray.append("work under presure")
                    #print("you have skill 1")

                if tag == "question18":
                    sk12 = True
                    checkskills()
                   # skillsarray.append("team worker")
                   # print("you have skill 2")
                if tag == "question17":
                    sk13 = True
                    checkskills()
                    #skillsarray.append("Helper")
                    #print("you have skill 3")

                if tag == "question21":
                    print(skillsarray)
                    print(questiontimearray)



    else:

        print(f"{bot_name}: I do not understand...")


