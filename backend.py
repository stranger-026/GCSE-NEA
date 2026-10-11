# Imports
import json
import time
import os
import sys
import subprocess

from flask import Flask, jsonify
from flask_cors import CORS

# Server setup 
def restart_server():
    subprocess.Popen(["python", "backend.py"])

app = Flask(__name__)
CORS(app)

# def restart_server():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)
#     app.run()

# Data
import random


cards_list = [
     {'color': 'yellow', 'number': '1'},
    {'color': 'yellow', 'number': '2'},
    {'color': 'yellow', 'number': '3'},
    {'color': 'yellow', 'number': '4'},
    {'color': 'yellow', 'number': '5'},
    {'color': 'yellow', 'number': '6'},
    {'color': 'yellow', 'number': '7'},
    {'color': 'yellow', 'number': '8'},
    {'color': 'yellow', 'number': '9'},
    {'color': 'yellow', 'number': '10'},
    {'color': 'red', 'number': '1'},
    {'color': 'red', 'number': '2'},
    {'color': 'red', 'number': '3'},
    {'color': 'red', 'number': '4'},
    {'color': 'red', 'number': '5'},
    {'color': 'red', 'number': '6'},
    {'color': 'red', 'number': '7'},
    {'color': 'red', 'number': '8'},
    {'color': 'red', 'number': '9'},
    {'color': 'red', 'number': '10'},
    {'color': 'black', 'number': '1'},
    {'color': 'black', 'number': '2'},
    {'color': 'black', 'number': '3'},
    {'color': 'black', 'number': '4'},
    {'color': 'black', 'number': '5'},
    {'color': 'black', 'number': '6'},
    {'color': 'black', 'number': '7'},
    {'color': 'black', 'number': '8'},
    {'color': 'black', 'number': '9'},
    {'color': 'black', 'number': '10'}
]

list_a = []
list_b = [] 

random.shuffle(cards_list)
winner = 'none'

# Endpoint for card request
@app.route('/card_info_request')
def card_info_reqeust():
    #  Get the cards from list
    card_a = cards_list.pop(random.randint(0, len(cards_list) - 1))
    list_a.append(card_a)
    card_b = cards_list.pop(random.randint(0, len(cards_list) - 1))
    list_b.append(card_b)

    # Compare the cards
    if card_a['color'] == card_b['color']:
        if card_a['number'] > card_b['number']:
            winner = 0
        else:
            winner = 1
    elif card_a['color'] == 'red' and card_b['color'] == 'black' or card_a['color'] == 'black' and card_b['color'] == 'yellow' or card_a['color'] == 'yellow' and card_b['color'] == 'red':
        winner = 0
    else:
        winner = 1
    
    # Preparing to send 
    round_data = {
       'current_score_0': str(card_a['number']), 
        'current_score_1': str(card_b['number']),
        'current_color_0': str(card_a['color']),
        'current_color_1': str(card_b['color']), 
        'winner': str(winner),
        'card_list' : str(len(cards_list)),
        'list_a': list_a,
        'list_b': list_b,
        'card_list': cards_list,


    }

    #  Sending
    return jsonify(round_data)


# Restart endpoint
@app.route('/restart_server_request', methods=['POST'])
def restart_server_func():
    # Reset lists 
    cards_list.extend(list_a)
    cards_list.extend(list_b)
    list_a.clear()
    list_b.clear()
    restart_server()
    return '', 204

#  Authentication




@app.route('/authen_request')
def authen_requets():
    return('idk')



# Running the server
if __name__ == '__main__':
    app.run()
