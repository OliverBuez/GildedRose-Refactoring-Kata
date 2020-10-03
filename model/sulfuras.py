from .abstractitem import AbstractItem

class Sulfuras(AbstractItem):
    def __init__(self, name, sell_in, _=None):
        self.name = name
        self.sell_in = sell_in
        self.quality = 80
    
    def pass_day(self):
        pass
