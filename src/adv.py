import sys

from player import Player
from room import Room


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
# playername = input(
#     'Please enter your name, real or imagined: ')
# player = Player(playername, room['outside'])
player = Player('Gerold', room['outside'])
print(newline, end='')
print(f'Well, {player.name}, why don\'t we get started?')

# gameplay functions


# def travel(direction):
#     try:
#         player.current_room = [f'current_room.{direction}_to']
#     except AttributeError:
#         print(newline, end='')
#         print(f'There is no path in that direction, {player.name}.')


# gameplay loop
while True:
    current_room = player.current_room
    print(newline, end='')
    print(f'{current_room.name}')
    print(f'{current_room.desc}')
    print(newline, end='')
    action = input('Action: ')
    if action == 'q':
        print(newline, end='')
        print('From the bottom of a heretofore unnoticed well, you hear: "Thank you for playing..."')
        print(newline, end='')
        sys.exit()
    if action == 'n':
        try:
            player.current_room = current_room.n_to
        except AttributeError:
            print(newline, end='')
            print(f'There is no path in that direction, {player.name}.')
    if action == 'e':
        try:
            player.current_room = current_room.e_to
        except AttributeError:
            print(newline, end='')
            print(f'There is no path in that direction, {player.name}.')
    if action == 'w':
        try:
            player.current_room = current_room.w_to
        except AttributeError:
            print(newline, end='')
            print(f'There is no path in that direction, {player.name}.')
    if action == 's':
        try:
            player.current_room = current_room.s_to
        except AttributeError:
            print(newline, end='')
            print(f'There is no path in that direction, {player.name}.')
