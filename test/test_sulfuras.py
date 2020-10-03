# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from items import Item

class SulfurasTest(unittest.TestCase):

    def test_after_passed_decrease(self):
        '''
        Once the sell by date has passed, Quality degrades twice as fast
        '''
        item = Item("Sulfuras, Hand of Ragnaros", 0, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 80, "'Sulfuras', being a legendary item, never has to be sold or decreases in Quality, its Quality is 80 and it never alters")
    
    def test_quality_never_negative(self):
        '''
        The Quality of an item is never negative
        '''
        item1 = Item("Sulfuras, Hand of Ragnaros", 5, 0)
        item2 = Item("Sulfuras, Hand of Ragnaros", 0, 1)
        GildedRose([item1,item2]).update_quality()
        self.assertEqual(item1.quality, 80, "'Sulfuras', being a legendary item, never has to be sold or decreases in Quality, its Quality is 80 and it never alters")
        self.assertEqual(item2.quality, 80, "'Sulfuras', being a legendary item, never has to be sold or decreases in Quality, its Quality is 80 and it never alters")
        Item("Sulfuras, Hand of Ragnaros", 5, -1)

    def test_quality_no_more_fifty(self):
        '''
        The Quality of an item is never more than 50
        '''
        item = Item("Sulfuras, Hand of Ragnaros", 10,50)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 80, "'Sulfuras', being a legendary item, never has to be sold or decreases in Quality, its Quality is 80 and it never alters")
        Item("Sulfuras, Hand of Ragnaros", 10, 51)

    def test_sulfuras(self):
        '''
        "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
        '''
        sulfuras = Item("Sulfuras, Hand of Ragnaros", 5, 40)
        GildedRose([sulfuras]).update_quality()
        self.assertEqual(sulfuras.sell_in, 5, "'Sulfuras', being a legendary item, never has to be sold")
        self.assertEqual(sulfuras.quality, 80, "'Sulfuras', being a legendary item, never has to be decreases in Quality & its Quality is 80 and it never alters")

    def test_decrease(self):
        '''
        At the end of each day our system lowers both values for every item
        '''
        item = Item("Sulfuras, Hand of Ragnaros", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 80, "'Sulfuras', being a legendary item, never has to be decreases in Quality & its Quality is 80 and it never alters")

if __name__ == '__main__':
    unittest.main()
