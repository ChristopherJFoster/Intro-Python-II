import sys

from player import Player
from room import Room
from item import Item

# Declare all the items

rope = Item('rope', 'A dusty old rope, probably about fifty units long')
lamp = Item('lamp', 'A rusty lamp with less fuel than you\'d like. The lamp is functional, however, since it is currently illuminating the room.')
knife = Item(
    'knife', '"What is a knife sharpener?" you imagine the previous\nowner of this knife wondering.')


# items = {
#     'rope': Item('rope', 'A dusty old rope, probably about fifty units long'),
#     'lamp': Item('lamp', 'A rusty lamp with less fuel than you\'d like. The lamp is functional, however, since it is currently illuminating the room.'),
#     'knife': Item('knife', '"What is a knife sharpener?" you imagine the previous owner of this knife wondering.')
# }

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons", [rope, knife]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [lamp]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", []),
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

# DRY variables
newline = '\n'
suggestion = 'Slow down, pardner. Try n, s, e, or w, or simple commands \nlike \'examine filth\', \'take treasure\', or \'drop scorpion\'.'


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


print(newline, end='')
print('Welcome to the game, player!', newline)
playername = input(
    'Please enter your name, real or imagined: ')
player = Player(playername, room['outside'])
print(newline, end='')
print(f'Well, {player.name}, why don\'t we get started?')
player.look()


# gameplay loop
while True:
    action = input('Action: ').lower().split(' ')
    if len(action) == 1:
        if action[0] in ('q', 'quit'):
            print(newline, end='')
            print(
                'From the bottom of a heretofore unnoticed well, you hear:\n"Thank you for playing..."')
            print(newline, end='')
            sys.exit()
        elif action[0] in ('n', 's', 'e', 'w'):
            player.travel(action[0])
        elif action[0] in ('i', 'inventory'):
            print(newline, end='')
            if len(player.items) == 0:
                print(
                    'You have nothing but the potato-sack trousers and soiled tunic \nyou apparently think fit to wear in public.')
            else:
                print('In addition to your shoddy clothes, you have:')
                for i in range(len(player.items)):
                    print(f'{player.items[i].name}')
        elif action[0] in ('get', 'take', 'drop', 'leave'):
            print(f'{action[0].capitalize()} what, exactly?')
        elif action[0] in ('examine', 'look'):
            player.look()
        else:
            print(newline, end='')
            print(suggestion)
            print(newline, end='')
    elif len(action) == 2:
        if action[0] in ('get', 'take'):
            player.takeItem(player.current_room.remove_item(action[1]))
        elif action[0] in ('drop', 'leave'):
            player.dropItem(action[1])
        elif action[0] in ('examine', 'look'):
            player.look(action[1])
        else:
            print(newline, end='')
            print(suggestion)
            print(newline, end='')
    else:
        print(newline, end='')
        print(suggestion)
        print(newline, end='')
