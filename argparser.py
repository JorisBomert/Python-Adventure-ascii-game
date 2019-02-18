#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This argparse will be used for the adventure game. This is where all the
options will be parsed
'''

import argparse



VERSION = "v1.0.0 (11-10-2017)"
info = "This is a text adventure. This game is about a lonely woodcutter who goes on an adventure"
about = "Good day, my name is Joris and I am the game developer. I hope you enjoy the game!"
cheat = "Magically solves everything in the room for you, so you get to go on to the next room in once"

options = {}

argparse_title = "Text based adventure game, By Joris Bomert, version 1.0.0"

def parse_options():
    """
    Parse all command line options and arguments and return them as a dictionary.
    """
    parser = argparse.ArgumentParser(description=argparse_title,
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     usage="\n  [options] [arguments]")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-i", "--info", dest="info",
                       help="Gives a description about the game",
                       action="version", version=info)
    group.add_argument("-v", "--version", dest="version",
                       help="Shows the version of the game",
                       action="version", version=VERSION)
    group.add_argument("-a", "--about", dest="about",
                       help="About the developer",
                       action="version", version=about)
    group.add_argument("-c", "--cheat", dest="cheat",
                       help="Automatically solves the room for you",
                       action="version", version=cheat)

    args = parser.parse_args()

    options["args"] = vars(args)

    return parser.parse_args()
