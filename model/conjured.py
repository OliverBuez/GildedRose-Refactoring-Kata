from .abstractitem import AbstractItem

class Conjured(AbstractItem):
    
    def _update_quality(self):
        return self._decrease_quality(2)
