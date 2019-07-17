class Item:
    def __init__(self, name, desc, light):
        self.name = name
        self.desc = desc
        self.light = light

    def onTake(self):
        print(f'You take the {self.name}.')

    def onDrop(self):
        print(f'You drop the {self.name}.')
