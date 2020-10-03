from .abstractitem import AbstractItem

class AgedBrie(AbstractItem):

    def _update_quality(self):
        if self.sell_in <= 0:
            return self._decrease_quality(1)
        return self._increase_quality(1)
