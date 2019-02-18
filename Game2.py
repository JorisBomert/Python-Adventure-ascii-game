#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
The main file of Room 2
'''
import json
import re
import Game1

state = 1

def objects_room_2():
    ''' The objects of Room 2 returned as a list '''
    with open("rooms.json", "r") as json_1:
        data = json.load(json_1)
    barrel = str(data["game"][1]["objects"]["barrel"]["name"]) + ", "
    honey = str(data["game"][1]["objects"]["honey"]["name"])
    objects = barrel + honey
    obts = re.sub(r"[^\w+$]", " ", objects).split()
    return list(obts)


def respond_options_state_1(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_1:
        data = json.load(json_1)
    if option == available[2] or option == available[3]:
        return data["game"][1]["description"]
    elif option == available[4]:
        return data["game"][1]["toSee"]
    elif option == available[5] or option == available[6]:
        return data["game"][1]["clues"][0]
    elif option == available[7] or option == available[8]:
        barrel = str(data["game"][1]["objects"]["barrel"]["name"])
        return barrel

def barrel_description():
    ''' barrel description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][1]["objects"]["barrel"]["description"][0]
    return description

def honey_description():
    ''' honey description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][1]["objects"]["honey"]["description"][0]
    return description

def respond_object_options_state_1(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_2()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(barrel_description())
            elif opt == objects[1]:
                print(honey_description())
        elif option.split(' ', 1)[0] == available[2]:
            if opt == objects[0]:
                print("There doesn't appear to be a way of opening this barrel. \
                        Maybe there is another way?")
        elif option.split(' ', 1)[0] == available[3] or option.split(' ', 1)[0] == available[4]:
            if opt == objects[0]:
                print(" The barrel falls apart and a jar of honey appears in between \
                the broken wooden parts")
                print("You suddenly noticed a bear that's sleeping in the cave...")
                print("Ghmpf ghmpf... mumbles the bear, Hungry hmpg hmfmzzzz zzzz")
                print()
                print("______________________________________________")
                state = state + 1
                return state
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")

def respond_options_state_2(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_1:
        data = json.load(json_1)
    if option == available[2] or option == available[3]:
        return data["game"][1]["description"]
    elif option == available[4]:
        return data["game"][1]["toSee"]
    elif option == available[5] or option == available[6]:
        return data["game"][1]["clues"][1]
    elif option == available[7] or option == available[8]:
        barrel = str(data["game"][1]["objects"]["barrel"]["name"]) + ", "
        honey = str(data["game"][1]["objects"]["honey"]["name"])
        return barrel + honey

def barrel_description_2():
    ''' second barrel description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][1]["objects"]["barrel"]["description"][1]
    return description

def respond_object_options_state_2(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_2()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(barrel_description_2())
            elif opt == objects[1]:
                print(honey_description())
        elif option.split(' ', 1)[0] == available[5] or option.split(' ', 1)[0] == available[6]:
            if opt == objects[1]:
                print("You move the honey closer towards the bear, right next to the cave...")
                print("The bear see's the honey and crawls out of it's cave, and starts eating away")
                print("'Mmm honey! My favorite' says the bear")
                print("This might be your chance to go forward into the cave! It's now or never...")
                print()
                print("______________________________________________")
                state = state + 1
                return state
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    elif option.split(' ', 1)[0] == available[3] or option.split(' ', 1)[0] == available[4]:
        if opt == "bear":
            print("Don't kick the bear you silly! Do you have a death wish?")
    else:
        print("There is no " + str(opt) + " in the room...")

def respond_options_state_3(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_1:
        data = json.load(json_1)
    if option == available[2] or option == available[3]:
        return data["game"][1]["description"]
    elif option == available[4]:
        return data["game"][1]["toSee"]
    elif option == available[5] or option == available[6]:
        return data["game"][1]["clues"][2]
    elif option == available[7] or option == available[8]:
        barrel = str(data["game"][1]["objects"]["barrel"]["name"]) + ", "
        honey = str(data["game"][1]["objects"]["honey"]["name"])
        return barrel + honey

def honey_description_2():
    ''' second honey description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][1]["objects"]["honey"]["description"][1]
    return description

def respond_object_options_state_3(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_2()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(barrel_description_2())
            elif opt == objects[1]:
                print(honey_description_2())
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")

def backwards():
    ''' When going backwards, reducing state by 1 '''
    global state
    state = state - 1
    return state
