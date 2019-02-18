#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
The main file of Room 4
'''
import json
import re
import Game1

state = 1

def objects_room_4():
    ''' The objects of Room 4 returned as a list '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    jar = str(data["game"][3]["objects"]["jar"]["name"]) + ", "
    rock = str(data["game"][3]["objects"]["rock"]["name"]) + ", "
    boots = str(data["game"][3]["objects"]["boots"]["name"]) + ", "
    fairy = str(data["game"][3]["objects"]["fairy"]["name"])
    objects = jar + rock + boots + fairy
    obts = re.sub(r"[^\w]", " ", objects).split()
    return list(obts)

def respond_options_state_1(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    if option == available[2] or option == available[3]:
        return data["game"][3]["description"][0]
    elif option == available[4]:
        return data["game"][3]["toSee"][0]
    elif option == available[5] or option == available[6]:
        return data["game"][3]["clues"][0]
    elif option == available[7] or option == available[8]:
        jar = str(data["game"][3]["objects"]["jar"]["name"]) + ", "
        rock = str(data["game"][3]["objects"]["rock"]["name"])
        return jar + rock

def jar_description():
    ''' jar description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][3]["objects"]["jar"]["description"][0]
    return description

def rock_description():
    ''' rock description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][3]["objects"]["rock"]["description"][0]
    return description

def boots_description():
    ''' boots description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][3]["objects"]["boots"]["description"]
    return description

def fairy_description():
    ''' fairy description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][3]["objects"]["fairy"]["description"]
    return description

def respond_object_options_state_1(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_4()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(jar_description())
            elif opt == objects[1]:
                print(rock_description())
            elif opt == objects[2]:
                print(boots_description())
            elif opt == objects[3]:
                print(fairy_description())
        elif option.split(' ', 1)[0] == available[3] or option.split(' ', 1)[0] == available[4]:
            if opt == objects[0]:
                print("Kicking the jar.")
                print("Ouch! That hurts, and the jar did not even break!")
                print("Huh? What? Suddenly sounds from the jar...")
                print("Oh hi there! I did not even see you come in the cave")
                print()
                print("Oh... You wondered why you could not break the jar...")
                print("Well you see... For many years ago I was bewitched and put into this jar \
        that's unbreakable by all but one thing, the Boots of Doom!")
                print("I would be cursed and locked up in this jar untill somebody saves me by breaking the jar")
                print()
                print("Maybe you would like to help me? In return I can make wishes come true! \
        I am a fairy you see...")
                print("You see the rock over there? Right under it you will find \
        the Boots of Doom that can break the jar!")
                print()
                print("______________________________________________")
                state = state + 1
                return state
            else:
                print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")


def respond_options_state_2(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    if option == available[2] or option == available[3]:
        return data["game"][3]["description"][0]
    elif option == available[4]:
        return data["game"][3]["toSee"][0]
    elif option == available[5] or option == available[6]:
        return data["game"][3]["clues"][1]
    elif option == available[7] or option == available[8]:
        jar = str(data["game"][3]["objects"]["jar"]["name"]) + ", "
        rock = str(data["game"][3]["objects"]["rock"]["name"]) + ", "
        fairy = str(data["game"][3]["objects"]["fairy"]["name"])
        return jar + rock + fairy

def jar_description_2():
    ''' second jar description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][3]["objects"]["jar"]["description"][1]
    return description

def respond_object_options_state_2(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_4()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(jar_description_2())
            elif opt == objects[1]:
                print(rock_description())
            elif opt == objects[2]:
                print(boots_description())
            elif opt == objects[3]:
                print(fairy_description())
        elif option.split(' ', 1)[0] == available[5] or option.split(' ', 1)[0] == available[6]:
            if opt == objects[1]:
                print("Pushing the rock, trying to move it")
                print("Hmpff... ")
                print("...And the rock falls rumbling to the ground...")
                print()
                print("______________________________________________")
                state = state + 1
                return state
            else:
                print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
        elif opt == "boots of doom":
            print("The boots are burried under a rock")
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")

def respond_options_state_3(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    if option == available[2] or option == available[3]:
        return data["game"][3]["description"][0]
    elif option == available[4]:
        return data["game"][3]["toSee"][0]
    elif option == available[5] or option == available[6]:
        return data["game"][3]["clues"][2]
    elif option == available[7] or option == available[8]:
        jar = str(data["game"][3]["objects"]["jar"]["name"]) + ", "
        boots = str(data["game"][3]["objects"]["boots"]["name"]) + ", "
        rock = str(data["game"][3]["objects"]["rock"]["name"]) + ", "
        fairy = str(data["game"][3]["objects"]["fairy"]["name"])
        return jar + boots + rock + fairy

def rock_description_2():
    ''' second rock description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][3]["objects"]["rock"]["description"][1]
    return description

def respond_object_options_state_3(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_4()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(jar_description_2())
            elif opt == objects[1]:
                print(rock_description_2())
            elif opt == objects[2]:
                print(boots_description())
            elif opt == objects[3]:
                print(fairy_description())
        elif option.split(' ', 1)[0] == available[8]:
            if opt == objects[2] or opt == "boots of doom":
                Game1.addItem(opt)
                print("Taking the Boots of Doom on")
                print("They feel really heavy!")
                print()
                print("______________________________________________")
                state = state + 1
                return state
            else:
                print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
        elif option.split(' ', 1)[0] == available[7]:
            if opt == objects[2]:
                print("To use the Boots of Doom you have to take them")
            else:
                print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")

def respond_options_state_4(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    if option == available[2] or option == available[3]:
        return data["game"][3]["description"][1]
    elif option == available[4]:
        return data["game"][3]["toSee"][1]
    elif option == available[5] or option == available[6]:
        return data["game"][3]["clues"][3]
    elif option == available[7] or option == available[8]:
        jar = str(data["game"][3]["objects"]["jar"]["name"]) + ", "
        rock = str(data["game"][3]["objects"]["rock"]["name"]) + ", "
        fairy = str(data["game"][3]["objects"]["fairy"]["name"])
        return jar + rock + fairy

def respond_object_options_state_4(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_4()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(jar_description_2())
            elif opt == objects[1]:
                print(rock_description_2())
            elif opt == objects[2]:
                print(boots_description())
            elif opt == objects[3]:
                print(fairy_description())
        elif option.split(' ', 1)[0] == available[3] or option.split(' ', 1)[0] == available[4]:
            if opt == objects[0]:
                Game1.useItem('boots')
                print("Kicking the jar with the Magical Boots of Doom.")
                print("The jar breaks and the fairy gets out.")
                print()
                print("______________________________________________")
                state = state + 1
                return state
            else:
                print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")

def respond_options_state_5(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    if option == available[2] or option == available[3]:
        return data["game"][3]["description"][1]
    elif option == available[4]:
        return data["game"][3]["toSee"][1]
    elif option == available[5] or option == available[6]:
        return data["game"][3]["clues"][4]
    elif option == available[7] or option == available[8]:
        rock = str(data["game"][3]["objects"]["rock"]["name"]) + ", "
        fairy = str(data["game"][3]["objects"]["fairy"]["name"])
        return rock + fairy

def respond_object_options_state_5(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_4()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(jar_description_2())
            elif opt == objects[1]:
                print(rock_description_2())
            elif opt == objects[2]:
                print(boots_description())
            elif opt == objects[3]:
                print(fairy_description())
        elif option.split(' ', 1)[0] == available[10]:
            if opt == objects[3]:
                print("You wildly start kissing the Fairy...")
                print()
                print("'Eeuww what are you doing?!' yells the fairy while pushing you away")
                return "______________________________________________"
            else:
                print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")

def backwards():
    ''' When going backwards, reducing state by 1 '''
    global state
    state = state - 1
    return state
