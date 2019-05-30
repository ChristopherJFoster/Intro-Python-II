# Write a class to hold player information, e.g. what room they are in
# currently.

newline = '\n'


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def look(self, item='room'):
        visible_items = self.items + self.current_room.items
        found = False
        for i in visible_items:
            if i.name == item:
                print(newline, end='')
                print(i.desc)
                print(newline, end='')
                found = True
                break
        if item == 'room':
            print(newline, end='')
            print(f'{self.current_room.name}')
            print(f'{self.current_room.desc}')
            print(newline, end='')
            print('In this location, you see:')
            for i in range(len(self.current_room.items)):
                print(f'{self.current_room.items[i].name}')
            print(newline, end='')
            found = True
        if found == False:
            print(newline, end='')
            print(f'There doesn\'t seem to be any {item} here.')
            print(newline, end='')

    def travel(self, direction):
        try:
            self.current_room = getattr(self.current_room, f'{direction}_to')
            self.look()
        except AttributeError:
            print(newline, end='')
            print(f'There is no path in that direction, {self.name}.')

    def addItem(self, item):
        self.items.append(item)
        print(newline, end='')
        print(f'You take the {item.name}.')
        print(newline, end='')

    def removeItem(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return item
        print(newline, end='')
        print(f'You don\'t have a {item_name} to drop!')
        print(newline, end='')
        return None
