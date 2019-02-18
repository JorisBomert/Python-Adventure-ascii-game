#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
The main file of Room 5
'''
import json
import re
import Game1

state = 1

def objects_room_5():
    ''' The objects of Room 5 returned as a list '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    fairy = str(data["game"][4]["objects"]["fairy"]["name"]) + ", "
    ring = str(data["game"][4]["objects"]["ring"]["name"]) + ", "
    princess = str(data["game"][4]["objects"]["princess"]["name"]) + ", "
    priest = str(data["game"][4]["objects"]["priest"]["name"])
    objects = fairy + ring + princess + priest
    obts = re.sub(r"[^\w]", " ", objects).split()
    return list(obts)

def respond_options_state_1(option):
    ''' The respond of the command given from always_available_options '''
    available = Game1.always_available_options()
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    if option == available[2] or option == available[3]:
        return data["game"][4]["description"]
    elif option == available[4]:
        return data["game"][4]["toSee"]
    elif option == available[5] or option == available[6]:
        return data["game"][4]["clues"][0]
    elif option == available[7] or option == available[8]:
        fairy = str(data["game"][4]["objects"]["fairy"]["name"]) + ", "
        ring = str(data["game"][4]["objects"]["ring"]["name"]) + ", "
        princess = str(data["game"][4]["objects"]["princess"]["name"]) + ", "
        priest = str(data["game"][4]["objects"]["priest"]["name"])
        return fairy + ring + princess + priest

def fairy_description():
    ''' fairy description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][4]["objects"]["fairy"]["description"]
    return description

def ring_description():
    ''' ring description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][4]["objects"]["ring"]["description"]
    return description

def princess_description():
    ''' princess description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][4]["objects"]["princess"]["description"]
    return description

def priest_description():
    ''' priest description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][4]["objects"]["priest"]["description"]
    return description

def respond_object_options_state_1(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_5()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(fairy_description())
            elif opt == objects[1]:
                print(ring_description())
            elif opt == objects[2]:
                print(princess_description())
            elif opt == objects[3]:
                print(priest_description())
        elif option.split(' ', 1)[0] == available[7]:
            if opt == objects[1]:
                Game1.useItem(opt)
                print("You kneel before the princess and put the wedding ring around her finger")
                print()
                print("The priest continues with the speach")
                print()
                print("______________________________________________")
                state = state + 1
                return state
            else:
                print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
        elif option.split(' ', 1)[0] == available[10]:
            if opt == objects[2]:
                print("Have some patience, you'll have plenty of time to kiss the princess later")
            elif opt == objects[3]:
                print("Don't kiss the priest you idiot!")
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
        return data["game"][4]["description"]
    elif option == available[4]:
        return data["game"][4]["toSee"]
    elif option == available[5] or option == available[6]:
        return data["game"][4]["clues"][1]
    elif option == available[7] or option == available[8]:
        fairy = str(data["game"][4]["objects"]["fairy"]["name"]) + ", "
        ring = str(data["game"][4]["objects"]["ring"]["name"]) + ", "
        princess = str(data["game"][4]["objects"]["princess"]["name"]) + ", "
        priest = str(data["game"][4]["objects"]["priest"]["name"])
        return fairy + ring + princess + priest

def respond_object_options_state_2(option):
    ''' The respond of the command given from object_options '''
    available = Game1.object_options()
    objects = objects_room_5()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(fairy_description())
            elif opt == objects[1]:
                print(ring_description())
            elif opt == objects[2]:
                print(princess_description())
            elif opt == objects[3]:
                print(priest_description())
        elif option.split(' ', 1)[0] == available[10]:
            if opt == objects[2]:
                Game1.useItem(opt)
                print("You kiss the princess and people in the church are cheering and applauding")
                print()
                print("______________________________________________")
                state = state + 1
                return state
            elif opt == objects[3]:
                print("Don't kiss the priest silly!")
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
