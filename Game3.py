#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
The main file of Room 3
'''
import json
import re
import Game1


state = 1

def objects_room_3():
    ''' The objects of Room 3 returned as a list '''
    with open("rooms.json", "r") as json_1:
        data = json.load(json_1)
    pickaxe = str(data["game"][2]["objects"]["pickaxe"]["name"]) + ", "
    gap = str(data["game"][2]["objects"]["gap"]["name"])
    objects = pickaxe + gap
    obts = re.sub(r"[^\w+$]", " ", objects).split()
    return list(obts)

def respond_options_state_1(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    if option == available[2] or option == available[3]:
        return data["game"][2]["description"][0]
    elif option == available[4]:
        return data["game"][2]["toSee"][0]
    elif option == available[5] or option == available[6]:
        return data["game"][2]["clues"][0]
    elif option == available[7] or option == available[8]:
        return "It's too dark to see any objects!"


def respond_object_options_state_1(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    opt = option.split(' ', 1)[1]
    global state
    if option.split(' ', 1)[0] == available[7]:
        Game1.useItem(opt)
        state = state + 1
        print("The flashlight lights up the whole cave")
        print()
        print("______________________________________________")
        return state
    else:
        print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))

def respond_options_state_2(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    if option == available[2] or option == available[3]:
        return data["game"][2]["description"][1]
    elif option == available[4]:
        return data["game"][2]["toSee"][1]
    elif option == available[5] or option == available[6]:
        return data["game"][2]["clues"][1]
    elif option == available[7] or option == available[8]:
        pickaxe = str(data["game"][2]["objects"]["pickaxe"]["name"]) + ", "
        gap = str(data["game"][2]["objects"]["gap"]["name"])
        return pickaxe + gap

def pickaxe_description():
    ''' pickaxe description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][2]["objects"]["pickaxe"]["description"][0]
    return description

def gap_description():
    ''' gap description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][2]["objects"]["gap"]["description"][0]
    return description

def respond_object_options_state_2(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_3()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(pickaxe_description())
            elif opt == objects[1]:
                print(gap_description())
        elif option.split(' ', 1)[0] == available[7]:
            if opt == objects[0]:
                print("You use the pickaxe and start hacking away onto the rocks.")
                print("The small gap seems to be increasing in width.")
                print()
                print("______________________________________________")
                state = state + 1
                return state
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
        return data["game"][2]["description"][1]
    elif option == available[4]:
        return data["game"][2]["toSee"][1]
    elif option == available[5] or option == available[6]:
        return data["game"][2]["clues"][2]
    elif option == available[7] or option == available[8]:
        pickaxe = str(data["game"][2]["objects"]["pickaxe"]["name"]) + ", "
        gap = str(data["game"][2]["objects"]["gap"]["name"])
        return pickaxe + gap

def pickaxe_description_2():
    ''' pickaxe description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][2]["objects"]["pickaxe"]["description"][1]
    return description

def gap_description_2():
    ''' gap description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][2]["objects"]["gap"]["description"][1]
    return description

def respond_object_options_state_3(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_3()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(pickaxe_description_2())
            elif opt == objects[1]:
                print(gap_description_2())
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")

def backwards():
    ''' When going backwards, reducing state by 1 '''
    global state
    state = state - 1
    return state
