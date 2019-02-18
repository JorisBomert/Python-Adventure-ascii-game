#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Rooms.py is the file for the room functions
'''
import json


def load_room_1_description():
    ''' Description room 1 '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
        description_data = data["game"][0]["description"]
    return description_data

def load_room_2_description():
    ''' Description room 2 '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
        description_data = data["game"][1]["description"]
    return description_data

def load_room_3_description_1():
    ''' Description room 3 State 1 '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
        description_data = data["game"][2]["description"][0]
    return description_data

def load_room_3_description_2():
    ''' Description room 3 State 2 and above '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
        description_data = data["game"][2]["description"][1]
    return description_data

def load_room_3_description_3():
    ''' Description room 3 State 2 and above '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
        description_data = data["game"][2]["description"][2]
    return description_data

def load_room_4_description_1():
    ''' Description room 4 State 1 '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
        description_data = data["game"][3]["description"][0]
    return description_data

def load_room_4_description_2():
    ''' Description room 4 State 2 and above '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
        description_data = data["game"][3]["description"][1]
    return description_data

def load_room_4_description_3():
    ''' Description room 4 State 3 '''
    print("Finally out of this jar after being in there for over a 100 years!")
    print("Thank you! In return I shall do as I promised and make your wish come true")
    print("'Hmmm...' says the fairy while swirling her wand around.")
    print("So a beautiful princes you want to marry? That I can arrange.")
    print("Let me know when you are ready and I will cast my spell!")
    return "______________________________________________"

def load_room_5_description_1():
    ''' Description room 5 state 1 '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
        description_data = data["game"][4]["description"]
    return description_data

def load_room_5_description_2():
    ''' fairy talking in room 5 state 1,  '''
    print("Fairy: 'Don't worry, it's normal to be a bit confused after I used my spell on you.'")
    print("Just making your wish come true so you won't have to be lonely anymore!")
    print("Here, don't forget the wedding ring. 'Drops wedding ring in your pockets'")
    print()
    return "______________________________________________"

def load_room_5_ending():
    ''' Ending text, credits '''
    print("This was a story about a lonely woodcutter living on his own in the forrest.")
    print("Every night he sat and dreamt about how much he would want a lover in his life")
    print()
    print("Eventually the woodcutter got what he so dearly desired by not giving up and \
    keep going forward, even if it does not go in once...")
    print()
    return "______________________________________________"
