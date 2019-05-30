# Implement a class to hold room information. This should have name and
# description attributes.

newline = '\n'


class Room:
    def __init__(self, name, desc, items, lit):
        self.name = name
        self.desc = desc
        self.items = items
        self.lit = lit

    def addItem(self, item):
        if item != None:
            self.items.append(item)
            print(newline, end='')
            print(f'You\'ve dropped the {item.name}.')
            print(newline, end='')

    def removeItem(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return item
        print(newline, end='')
        print(f'There doesn\'t seem to be any {item_name} here.')
        print(newline, end='')
        return None
