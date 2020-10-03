from model.agedbrie import AgedBrie
from model.conjured import Conjured
from model.backstagepasses import BackstagePasses
from model.sulfuras import Sulfuras
from model.abstractitem import AbstractItem

def Item(name, sell_in, quality):
    if name.startswith("Aged Brie"):
        return AgedBrie(name, sell_in, quality)
    if name.startswith("Conjured"):
        return Conjured(name, sell_in, quality)
    if name.startswith("Backstage passes"):
        return BackstagePasses(name, sell_in, quality)
    if name.startswith("Sulfuras"):
        return Sulfuras(name, sell_in, quality)
    return AbstractItem(name, sell_in, quality)
