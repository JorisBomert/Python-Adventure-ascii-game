#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
The main file of Room 1
'''
import json
from collections import OrderedDict
import re

state = 1

def introduction():
    ''' Game introdution that will appear at every room and every state '''
    print("Game introduction:")
    print("In each area you enter there are objects to interact with.")
    print("Try and solve each area to go to the next one")
    print("Press 'h' or 'help' to see all possible commands\n")
    print("###############################################")

def help_choice():
    ''' Help menu showing all options, output as dictionary '''
    options = OrderedDict({
        "h, help": "See all options",
        "i, info": "Description of the area",
        "fw, forward": "Go to the next area",
        "bw, backwards": "Go to the previous area",
        "look": "Look around in the area",
        "c, clue": "You get a clue on what to do next",
        "cheat": "Automatically solves the room for you",
        "o, object": "Shows all objects in the room",
        "ins, inspect <object>": "Look at the object in detail",
        "open <object>": "Open the object, when possible",
        "k, kick <object>": "Kicks the object and breaking it, when possible",
        "m, move <object>": "Moves an object, when possible",
        "use <object>": "Uses an object, when possible",
        "take <object>": "Picks up an objects and adds it to inventory, when possible",
        "drop <object>": "Drops an object from the inventory",
        "inv, inventory": "See all objects in your inventory",
        "kiss": "Kisses whatever there is to kiss, when possible"
        })
    print("Your available options are:")
    print(json.dumps(options, indent=4, sort_keys=False))

def always_available_options():
    ''' Options that always will be usable on their own'''
    opts = ['h', 'help', 'i', 'info', 'look', 'c', 'clue', 'o',
            'object']
    return opts

def respond_options_state_1(option):
    ''' The respond of the command given from always_available_options '''
    available = always_available_options()
    with open("rooms.json", "r") as json_1:
        data = json.load(json_1)
    if option == available[2] or option == available[3]:
        return data["game"][0]["description"]
    elif option == available[4]:
        return data["game"][0]["toSee"]
    elif option == available[5] or option == available[6]:
        return data["game"][0]["clues"][0]
    elif option == available[7] or option == available[8]:
        chest = str(data["game"][0]["objects"]["chest"]["name"]) + ", "
        flashlight = str(data["game"][0]["objects"]["flashlight"]["name"]) + ", "
        key = str(data["game"][0]["objects"]["key"]["name"])
        return chest + flashlight + key

def objects_room_1():
    ''' The objects of Room 1 returned as a list '''
    with open("rooms.json", "r") as json_1:
        data = json.load(json_1)
    chest = str(data["game"][0]["objects"]["chest"]["name"]) + ", "
    flashlight = str(data["game"][0]["objects"]["flashlight"]["name"]) + ", "
    key = str(data["game"][0]["objects"]["key"]["name"])
    objects = chest + flashlight + key
    obts = re.sub(r"[^\w]", " ", objects).split()
    return list(obts)

def object_options():
    ''' Options that requires an object for to be able to use '''
    opts = ['ins', 'inspect', 'open', 'k', 'kick', 'm', 'move', 'use', 'take',
            'drop', 'kiss']
    return opts

def chest_description():
    ''' description chest '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][0]["objects"]["chest"]["description"][0]
    return description

def flashlight_description():
    ''' description flashlight '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    return data["game"][0]["objects"]["flashlight"]["description"][0]

def key_description():
    ''' description key '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][0]["objects"]["key"]["description"][0]
    return description


def respond_object_options_state_1(option):
    ''' The respond of the command given from object_options '''
    available = object_options()
    objects = objects_room_1()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(chest_description())
            elif opt == objects[1]:
                print(flashlight_description())
            elif opt == objects[2]:
                print(key_description())
        elif option.split(' ', 1)[0] == available[3] or option.split(' ', 1)[0] == available[4]:
            if opt == objects[0]:
                print("Hmm... the chest is too valuable... I won't destroy it.")
        elif option.split(' ', 1)[0] == available[2]:
            if opt == objects[0]:
                print("The chest opens and in it there is a flashlight")
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
    available = always_available_options()
    with open("rooms.json", "r") as json_1:
        data = json.load(json_1)
    if option == available[2] or option == available[3]:
        return data["game"][0]["description"]
    elif option == available[4]:
        return data["game"][0]["toSee"]
    elif option == available[5] or option == available[6]:
        return data["game"][0]["clues"][1]
    elif option == available[7] or option == available[8]:
        chest = str(data["game"][0]["objects"]["chest"]["name"]) + ", "
        flashlight = str(data["game"][0]["objects"]["flashlight"]["name"]) + ", "
        key = str(data["game"][0]["objects"]["key"]["name"])
        return chest + flashlight + key

def chest_description_2():
    ''' second chest description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][0]["objects"]["chest"]["description"][1]
    return description

def flashlight_description_2():
    ''' second flashlight description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][0]["objects"]["flashlight"]["description"][1]
    return description


def respond_object_options_state_2(option):
    ''' Respond of the command given from object_options in state 2 '''
    available = object_options()
    objects = objects_room_1()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(chest_description_2())
            elif opt == objects[1]:
                print(flashlight_description_2())
            elif opt == objects[2]:
                print(key_description())
        elif option.split(' ', 1)[0] == available[8]:
            if opt == objects[1]:
                addItem(opt)
                print("You have picked up the " + str(opt))
                print()
                print("______________________________________________")
                state = state + 1
                return state
        elif option.split(' ', 1)[0] == available[6]:
            if opt == objects[2]:
                print("Are you sure there is nothing you want to take with you \
                before you go on?")
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")


def respond_options_state_3(option):
    ''' The respond of the command given from always_available_options '''
    available = always_available_options()
    with open("rooms.json", "r") as json_1:
        data = json.load(json_1)
    if option == available[2] or option == available[3]:
        return data["game"][0]["description"]
    elif option == available[4]:
        return data["game"][0]["toSee"]
    elif option == available[5] or option == available[6]:
        return data["game"][0]["clues"][2]
    elif option == available[7] or option == available[8]:
        chest = str(data["game"][0]["objects"]["chest"]["name"]) + ", "
        key = str(data["game"][0]["objects"]["key"]["name"])
        return chest + key

def flashlight_description_3():
    ''' third flashlight description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][0]["objects"]["flashlight"]["description"][2]
    return description

def respond_object_options_state_3(option):
    ''' Respond of the command given from object_options in state 3 '''
    available = object_options()
    objects = objects_room_1()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(chest_description_2)
            elif opt == objects[1]:
                print(flashlight_description_3())
            elif opt == objects[2]:
                print(key_description())
        elif option.split(' ', 1)[0] == available[5] or option.split(' ', 1)[0] == available[6]:
            if opt == objects[2]:
                print("You move the key to the door and unlock it.")
                print("The door squeaks and opens slowly....")
                print("Could it be time to go forward and see what awaits you next?")
                print("______________________________________________")
                state = state + 1
                return state
            else:
                print(str(opt) + " cannot be moved...")
        else:
            print("You cannot " + str(option.split(' ', 1)[0]) + " the " + str(opt))
    else:
        print("There is no " + str(opt) + " in the room...")

def respond_options_state_4(option):
    ''' The respond of the command given from always_available_options '''
    available = always_available_options()
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    if option == available[2] or option == available[3]:
        return data["game"][0]["description"]
    elif option == available[4]:
        return data["game"][0]["toSee"]
    elif option == available[5] or option == available[6]:
        return data["game"][0]["clues"][3]
    elif option == available[7] or option == available[8]:
        chest = str(data["game"][0]["objects"]["chest"]["name"]) + ", "
        key = str(data["game"][0]["objects"]["key"]["name"])
        return chest + key

def key_description_2():
    ''' second key description '''
    with open("rooms.json", "r") as json_file:
        data = json.load(json_file)
    description = data["game"][0]["objects"]["key"]["description"][1]
    return description

def respond_object_options_state_4(option):
    ''' Respond of the command given from object_options in state 4 '''
    available = object_options()
    objects = objects_room_1()
    opt = option.split(' ', 1)[1]
    global state
    if opt in objects:
        if option.split(' ', 1)[0] == available[0] or option.split(' ', 1)[0] == available[1]:
            if opt == objects[0]:
                print(chest_description_2())
            elif opt == objects[1]:
                print(flashlight_description_3())
            elif opt == objects[2]:
                print(key_description_2())
        elif option.split(' ', 1)[0] == available[5] or option.split(' ', 1)[0] == available[6]:
            if opt == objects[2]:
                print(str(opt) + " cannot be moved agian.")
            else:
                print(str(opt) + " cannot be moved...")
    else:
        print("There is no " + str(opt) + " in the room...")


def backwards():
    ''' When going backwards, reducing state by 1 '''
    global state
    state = state - 1
    return state

#inventory
def inv():
    ''' Shows items in inventory '''
    with open('inventory.data') as f:
        lines = f.readlines()
        if lines:
            for line in lines:
                print("Searching in your pockets... you find:")
                print(line[:])
                print()
                print("______________________________________________")
        else:
            print("Your inventory is empty")
            print()
            print("______________________________________________")

def addItem(item):
    ''' Function for adding items to the inventory '''
    with open('inventory.data', 'a') as f:
        f.write(item + ',')

def dropItem(item):
    ''' Function for dropping an item from inventory '''
    with open('inventory.data') as f:
        lines = f.readlines()
        if lines:
            inventory = lines[0].split(',')
            if item in inventory:
                while item in inventory:
                    inventory.remove(item)
                newInventory = ','.join(inventory)
                with open('inventory.data', 'w') as f:
                    f.write(newInventory)
                print("you have now dropped " + item)
            else:
                print("You do not have this item in your inventory")

def useItem(item):
    ''' Uses an item from inventory, after its been used it gets removed '''
    with open('inventory.data') as f:
        lines = f.readlines()
        if lines:
            inventory = lines[0].split(',')
            if item in inventory:
                while item in inventory:
                    inventory.remove(item)
                newInventory = ','.join(inventory)
                with open('inventory.data', 'w') as f:
                    f.write(newInventory)
                print("'Using' " + item)
            else:
                print("You do not have this item in your inventory")


def emptyInventory():
    ''' Drop all items from inventory, only used when quitting the game'''
    open('inventory.data', 'w').close()
