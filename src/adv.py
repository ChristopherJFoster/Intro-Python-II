import sys

from player import Player
from room import Room
from item import Item

# Declare all the rooms

item = {
    'rope': Item('rope', 'A dusty old rope, probably about fifty units long'),
    'lamp': Item('lamp', 'A rusty—but apparently functional—lamp with less fuel than you\'d like'),
    'knife': Item('knife', '')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['rope'], item['knife']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['lamp']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# initialize player
newline = '\n'
print(newline, end='')
print('Welcome to the game, player!', newline)
playername = input(
    'Please enter your name, real or imagined: ')
player = Player(playername, room['outside'])
print(newline, end='')
print(f'Well, {player.name}, why don\'t we get started?')

# gameplay functions


def travel(direction):
    try:
        player.current_room = getattr(current_room, f'{direction}_to')
    except AttributeError:
        print(newline, end='')
        print(f'There is no path in that direction, {player.name}.')


# gameplay loop
while True:
    current_room = player.current_room
    print(newline, end='')
    print(f'{current_room.name}')
    print(f'{current_room.desc}')
    print(newline, end='')
    print('In this location, you see:')
    for i in range(len(current_room.items)):
        print(f'{current_room.items[i].name}')
    print(newline, end='')
    action = input('Action: ')
    if action in ('q', 'quit'):
        print(newline, end='')
        print('From the bottom of a heretofore unnoticed well, you hear: "Thank you for playing..."')
        print(newline, end='')
        sys.exit()
    elif action in ('n', 's', 'e', 'w'):
        travel(action)
    else:
        print('I don\'t understand what you\'re trying to do. Try n, s, e, or w...')
