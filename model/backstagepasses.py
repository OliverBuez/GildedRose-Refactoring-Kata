from .abstractitem import AbstractItem

class BackstagePasses(AbstractItem):
    
    def _update_quality(self):
        if self.sell_in <= 0:
            return self._set_quality(0)
        if self.sell_in <= 5:
            return self._increase_quality(3)
        if self.sell_in <= 10:
            return self._increase_quality(2)
        return self._increase_quality(1)
