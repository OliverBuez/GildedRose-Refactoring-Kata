# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from items import Item

class ConjuredTest(unittest.TestCase):

    def test_after_passed_decrease(self):
        '''
        Once the sell by date has passed, Quality degrades twice as fast
        '''
        item = Item("Conjured", 0, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 6, "Once the sell by date has passed, Quality degrades twice as fast & 'Conjured' items degrade in Quality twice as fast as normal items")
    
    def test_quality_never_negative(self):
        '''
        The Quality of an item is never negative
        '''
        item1 = Item("Conjured", 5, 0)
        item2 = Item("Conjured", 0, 1)
        GildedRose([item1,item2]).update_quality()
        self.assertEqual(item1.quality, 0, "The Quality of an item is never negative")
        self.assertEqual(item2.quality, 0, "The Quality of an item is never negative")
        self.assertRaises(Exception, Item, "Conjured", 5, -1)

    def test_quality_no_more_fifty(self):
        '''
        The Quality of an item is never more than 50
        '''
        self.assertRaises(Exception, Item, "Conjured", 10, 51)

    def test_decrease(self):
        '''
        At the end of each day our system lowers both values for every item
        '''
        item = Item("Conjured", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 8, "At the end of each day our system lowers both values for every item & 'Conjured' items degrade in Quality twice as fast as normal items")
    
    def test_conjured_items(self):
        '''
        "Conjured" items degrade in Quality twice as fast as normal items
        '''
        item = Item("Conjured", 10, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 8, "'Conjured' items degrade in Quality twice as fast as normal items")


if __name__ == '__main__':
    unittest.main()
