class AbstractItem:
    def __init__(self, name, sell_in, quality):
        if quality > 50:
            raise Exception("Quality cannot be higher than 50")
        if quality < 0:
            raise Exception("The Quality of an item is never negative")
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def pass_day(self):
        self._update_quality()
        self.sell_in = self.sell_in - 1
        return self
    
    def _update_quality(self):
        return self._decrease_quality(1)
    
    def _set_quality(self, quality):
        self.quality = quality
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0:
            self.quality = 0
        return self

    def _decrease_quality(self, factor):
        self._set_quality(self.quality - factor * (2 if self.sell_in <=0 else 1))
        return self
    
    def _increase_quality(self, factor):
        self._set_quality(self.quality + factor)
        return self

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)