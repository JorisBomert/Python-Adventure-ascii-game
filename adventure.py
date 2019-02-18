#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Adventure.py is the main file. Run the game from this file.
This file uses other modules to execute code needed for the game
'''
import sys
import time
import argparser
import Room
import room_ascii
import Game1
import Game2
import Game3
import Game4
import Game5


def adventure():
    '''
    Argparse section
    '''
    opts = argparser.parse_options()
    opts = vars(opts)



def prompt():
    ''' Input function '''
    print("______________________________________________")
    print("what do you want to do?")
    choice = input("--> ")
    return choice



def room_1_state_1():
    ''' Room 1, state 1 '''
    Game1.introduction()
    print(Room.load_room_1_description())
    print(room_ascii.image_room_1_state_1())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_1_state_1()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_1_state_1()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        room_1_state_1()
    elif command == "bw" or command == "backwards":
        print("There is nothing to go backwards to...")
        room_1_state_1()
    elif command == "cheat":
        print(room_ascii.image_room_1_state_2())
        print(room_ascii.image_room_1_state_3())
        Game1.addItem("flashlight")
        room_1_state_4()
    elif command in Game1.always_available_options()[:]:
        print(Game1.respond_options_state_1(command))
        print()
        print("______________________________________________")
        room_1_state_1()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            if Game1.respond_object_options_state_1(command) == 2:
                room_1_state_2()
            else:
                print()
                print("______________________________________________")
                room_1_state_1()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_1_state_1()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_1_state_1()

def room_1_state_2():
    ''' Room 1, state 2 '''
    Game1.introduction()
    print(Room.load_room_1_description())
    print(room_ascii.image_room_1_state_2())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_1_state_2()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_1_state_2()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        room_1_state_2()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        Game1.backwards()
        room_1_state_1()
    elif command == "cheat":
        print(room_ascii.image_room_1_state_3())
        Game1.addItem("flashlight")
        room_1_state_4()
    elif command in Game1.always_available_options()[:]:
        print(Game1.respond_options_state_2(command))
        print()
        print("______________________________________________")
        room_1_state_2()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game1.respond_object_options_state_2(command)
            if stateCheck == 3:
                room_1_state_3()
            else:
                print()
                print("______________________________________________")
                room_1_state_2()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_1_state_3()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_1_state_2()

def room_1_state_3():
    ''' room 1, state 3 '''
    Game1.introduction()
    print(Room.load_room_1_description())
    print(room_ascii.image_room_1_state_3())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_1_state_3()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_1_state_3()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        room_1_state_3()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        Game1.backwards()
        room_1_state_2()
    elif command == "cheat":
        room_1_state_4()
    elif command in Game1.always_available_options()[:]:
        print(Game1.respond_options_state_3(command))
        print()
        print("______________________________________________")
        room_1_state_3()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game1.respond_object_options_state_3(command)
            if stateCheck == 4:
                room_1_state_4()
            else:
                print()
                print("______________________________________________")
                room_1_state_3()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_1_state_4()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_1_state_3()

def room_1_state_4():
    ''' room 1 state 4 '''
    Game1.introduction()
    print(Room.load_room_1_description())
    print(room_ascii.image_room_1_transition())
    command = prompt()
    if command == "fw" or command == "forward" or command == "cheat":
        room_2_state_1()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        Game1.backwards()
        room_1_state_3()
    elif command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_1_state_4()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_1_state_4()
    elif command in Game1.always_available_options()[:]:
        print(Game1.respond_options_state_4(command))
        print()
        print("______________________________________________")
        room_1_state_4()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            Game1.respond_object_options_state_4(command)
            print()
            print("______________________________________________")
            room_1_state_4()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_1_state_4()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_1_state_4()


def room_2_state_1():
    ''' room 2, state 1 '''
    Game1.introduction()
    print(Room.load_room_2_description())
    print(room_ascii.room_2_state_1())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_2_state_1()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_2_state_1()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_2_state_1()
    elif command == "bw" or command == "backwards":
        print("Walking backwards into the last area")
        print("______________________________________________")
        room_1_state_4()
    elif command == "cheat":
        print(room_ascii.room_2_state_2())
        room_2_state_3()
    elif command in Game1.always_available_options()[:]:
        print(Game2.respond_options_state_1(command))
        print()
        print("______________________________________________")
        room_2_state_1()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game2.respond_object_options_state_1(command)
            if stateCheck == 2:
                room_2_state_2()
            else:
                print()
                print("______________________________________________")
                room_2_state_1()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_2_state_2()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_2_state_1()

def room_2_state_2():
    ''' room 2, state 2 '''
    Game1.introduction()
    print(Room.load_room_2_description())
    print(room_ascii.room_2_state_2())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_2_state_2()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_2_state_2()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_2_state_2()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game2.backwards()
        room_2_state_1()
    elif command == "cheat":
        room_2_state_3()
    elif command in Game1.always_available_options()[:]:
        print(Game2.respond_options_state_2(command))
        print()
        print("______________________________________________")
        room_2_state_2()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game2.respond_object_options_state_2(command)
            if stateCheck == 3:
                room_2_state_3()
            else:
                print()
                print("______________________________________________")
                room_2_state_2()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_2_state_3()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_2_state_2()

def room_2_state_3():
    ''' room 2 state 3 '''
    Game1.introduction()
    print(Room.load_room_2_description())
    print(room_ascii.room_2_state_3())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_2_state_2()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_2_state_2()
    elif command == "fw" or command == "forward" or command == "cheat":
        print("Slowly sneaking past the bear and into the cave...")
        print("Quietly now! We don't want the bear to notice us...")
        print("______________________________________________")
        room_3_state_1()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game2.backwards()
        room_2_state_2()
    elif command in Game1.always_available_options()[:]:
        print(Game2.respond_options_state_3(command))
        print()
        print("______________________________________________")
        room_2_state_3()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            Game2.respond_object_options_state_3(command)
            print()
            print("______________________________________________")
            room_2_state_3()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_2_state_3()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_2_state_3()

def room_3_state_1():
    ''' room 3 state 1 '''
    Game1.introduction()
    print(Room.load_room_3_description_1())
    print(room_ascii.room_3_state_1())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_3_state_1()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_3_state_1()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_3_state_1()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game2.backwards()
        room_2_state_3()
    elif command == "cheat":
        print(room_ascii.room_3_state_2())
        Game1.useItem("flashlight")
        room_3_state_3()
    elif command in Game1.always_available_options()[:]:
        print(Game3.respond_options_state_1(command))
        print()
        print("______________________________________________")
        room_3_state_1()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game3.respond_object_options_state_1(command)
            if stateCheck == 2:
                room_3_state_2()
            else:
                print()
                print("______________________________________________")
                room_3_state_1()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_3_state_1()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_3_state_1()

def room_3_state_2():
    ''' room 3 state 2 '''
    Game1.introduction()
    print(Room.load_room_3_description_3())
    print(room_ascii.room_3_state_2())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_3_state_2()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_3_state_2()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_3_state_2()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game3.backwards()
        Game1.addItem("flashlight")
        room_3_state_1()
    elif command == "cheat":
        room_3_state_3()
    elif command in Game1.always_available_options()[:]:
        print(Game3.respond_options_state_2(command))
        print()
        print("______________________________________________")
        room_3_state_2()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game3.respond_object_options_state_2(command)
            if stateCheck == 3:
                room_3_state_3()
            else:
                print()
                print("______________________________________________")
                room_3_state_2()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_3_state_2()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_3_state_2()

def room_3_state_3():
    ''' room 3 state 3 '''
    Game1.introduction()
    print(Room.load_room_3_description_2())
    print(room_ascii.room_3_state_3())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_3_state_3()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_3_state_3()
    elif command == "fw" or command == "forward" or command == "cheat":
        print("Making yourself as small as possible")
        print("hmpffff... squeezing through the small opening")
        print("______________________________________________")
        room_4_state_1()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game3.backwards()
        room_3_state_2()
    elif command in Game1.always_available_options()[:]:
        print(Game3.respond_options_state_3(command))
        print()
        print("______________________________________________")
        room_3_state_3()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            Game3.respond_object_options_state_3(command)
            print()
            print("______________________________________________")
            room_3_state_3()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_3_state_3()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_3_state_3()

def room_4_state_1():
    ''' room 4 state 1 '''
    Game1.introduction()
    print(Room.load_room_4_description_1())
    print(room_ascii.room_4_state_1())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_4_state_1()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_4_state_1()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_4_state_1()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game4.backwards()
        room_3_state_3()
    elif command == "cheat":
        print(room_ascii.room_4_state_2())
        print(room_ascii.room_4_state_3())
        print(room_ascii.room_4_state_4())
        room_4_state_5()
    elif command in Game1.always_available_options()[:]:
        print(Game4.respond_options_state_1(command))
        print()
        print("______________________________________________")
        room_4_state_1()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game4.respond_object_options_state_1(command)
            if stateCheck == 2:
                room_4_state_2()
            else:
                print()
                print("______________________________________________")
                room_4_state_1()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_4_state_1()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_4_state_1()

def room_4_state_2():
    ''' room 4 state 2 '''
    Game1.introduction()
    print(Room.load_room_4_description_2())
    print(room_ascii.room_4_state_1())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_4_state_2()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_4_state_2()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_4_state_2()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game4.backwards()
        room_4_state_1()
    elif command == "cheat":
        print(room_ascii.room_4_state_3())
        print(room_ascii.room_4_state_4())
        room_4_state_5()
    elif command in Game1.always_available_options()[:]:
        print(Game4.respond_options_state_2(command))
        print()
        print("______________________________________________")
        room_4_state_2()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game4.respond_object_options_state_2(command)
            if stateCheck == 3:
                room_4_state_3()
            else:
                print()
                print("______________________________________________")
                room_4_state_2()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_4_state_2()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_4_state_2()

def room_4_state_3():
    ''' room 4 state 3 '''
    Game1.introduction()
    print(Room.load_room_4_description_2())
    print(room_ascii.room_4_state_2())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_4_state_3()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_4_state_3()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_4_state_3()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game4.backwards()
        room_4_state_2()
    elif command == "cheat":
        print(room_ascii.room_4_state_4())
        room_4_state_5()
    elif command in Game1.always_available_options()[:]:
        print(Game4.respond_options_state_3(command))
        print()
        print("______________________________________________")
        room_4_state_3()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game4.respond_object_options_state_3(command)
            if stateCheck == 4:
                room_4_state_4()
            else:
                print()
                print("______________________________________________")
                room_4_state_3()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_4_state_3()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_4_state_3()

def room_4_state_4():
    ''' room 4 state 4 '''
    Game1.introduction()
    print(Room.load_room_4_description_2())
    print(room_ascii.room_4_state_3())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_4_state_4()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_4_state_4()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_4_state_4()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game4.backwards()
        room_4_state_3()
    elif command == "cheat":
        room_4_state_5()
    elif command in Game1.always_available_options()[:]:
        print(Game4.respond_options_state_4(command))
        print()
        print("______________________________________________")
        room_4_state_4()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game4.respond_object_options_state_4(command)
            if stateCheck == 5:
                room_4_state_5()
            else:
                print()
                print("______________________________________________")
                room_4_state_4()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_4_state_4()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_4_state_4()

def room_4_state_5():
    ''' room 4 state 5 '''
    Game1.introduction()
    print(Room.load_room_4_description_2())
    print(room_ascii.room_4_state_4())
    print(Room.load_room_4_description_3())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_4_state_5()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_4_state_5()
    elif command == "fw" or command == "forward" or command == "cheat" or command == "ready":
        print("The fairy snaps her fingers and casts her spell")
        print("______________________________________________")
        room_5_state_0()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game4.backwards()
        Game1.addItem("boots")
        room_4_state_4()
    elif command in Game1.always_available_options()[:]:
        print(Game4.respond_options_state_5(command))
        print()
        print("______________________________________________")
        room_4_state_5()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            Game4.respond_object_options_state_5(command)
            print()
            print("______________________________________________")
            room_4_state_5()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_4_state_5()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_4_state_5()

def room_5_state_0():
    ''' POOF state room 5 '''
    print(room_ascii.room_5_state_1())
    time.sleep(2)
    Game1.addItem("ring")
    print(Room.load_room_5_description_2())
    room_5_state_1()

def room_5_state_1():
    ''' Room 5 state 1 '''
    Game1.introduction()
    print(Room.load_room_5_description_1())
    print(room_ascii.room_5_state_2())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_5_state_1()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_5_state_1()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_5_state_1()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game4.backwards()
        Game1.dropItem("ring")
        room_4_state_5()
    elif command == "cheat":
        print(room_ascii.room_5_state_2())
        room_5_state_3()
    elif command in Game1.always_available_options()[:]:
        print(Game5.respond_options_state_1(command))
        print()
        print("______________________________________________")
        room_5_state_1()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game5.respond_object_options_state_1(command)
            if stateCheck == 2:
                room_5_state_2()
            else:
                print()
                print("______________________________________________")
                room_5_state_1()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_5_state_1()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_5_state_1()

def room_5_state_2():
    ''' Room 5 state 2 '''
    Game1.introduction()
    print(Room.load_room_5_description_1())
    print(room_ascii.room_5_state_3())
    command = prompt()
    if command == "q" or command == "quit":
        print("Quitting the game, hope you had fun!")
        Game1.emptyInventory()
        sys.exit()
    elif command == "h" or command == "help":
        Game1.help_choice()
        print()
        print("______________________________________________")
        room_5_state_2()
    elif command == "inv" or command == "inventory":
        Game1.inv()
        room_5_state_2()
    elif command == "fw" or command == "forward":
        print("You cannot go forward yet")
        print("______________________________________________")
        room_5_state_2()
    elif command == "bw" or command == "backwards":
        print("Taking one step back...")
        print("______________________________________________")
        Game4.backwards()
        Game1.addItem("ring")
        room_5_state_1()
    elif command == "cheat":
        Game1.useItem("ring")
        room_5_state_3()
    elif command in Game1.always_available_options()[:]:
        print(Game5.respond_options_state_2(command))
        print()
        print("______________________________________________")
        room_5_state_2()
    elif command.split(' ', 1)[0] in Game1.object_options()[:]:
        try:
            stateCheck = Game5.respond_object_options_state_2(command)
            if stateCheck == 3:
                room_5_state_3()
            else:
                print()
                print("______________________________________________")
                room_5_state_2()
        except IndexError:
            print("This command needs to be used with an object")
            print("______________________________________________")
            room_5_state_2()
    elif command not in Game1.always_available_options()[:] or command not in Game1.object_options()[:]:
        print("Thats not a valid choice")
        print()
        print("______________________________________________")
        room_5_state_2()

def room_5_state_3():
    ''' Room 5 state 3 '''
    print(room_ascii.room_5_state_4())
    time.sleep(1)
    print(Room.load_room_5_ending())
    time.sleep(2)
    print("And they lived happily ever after....")
    time.sleep(2)
    print(room_ascii.ending())
    time.sleep(3)
    inp = input("Would you like to play again? y/n: ")
    if inp == "y" or inp == "yes":
        room_1_state_1()
    elif inp == "n" or inp == "no":
        print("Quitting the game, hope you had fun!")
        sys.exit()

if __name__ == "__main__":
    adventure()
    room_1_state_1()
