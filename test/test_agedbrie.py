# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from items import Item

class AgedBrieTest(unittest.TestCase):

    def test_after_passed_decrease(self):
        '''
        Once the sell by date has passed, Quality degrades twice as fast
        '''
        item = Item("Aged Brie", 0, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 8, "Once the sell by date has passed, Quality degrades twice as fast")
    
    def test_quality_never_negative(self):
        '''
        The Quality of an item is never negative
        '''
        item = Item("Aged Brie", 0, 0)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 0, "The Quality of an item is never negative")
        self.assertRaises(Exception, Item, "Aged Brie", 5, -1)

    def test_aged_brie(self):
        '''
        "Aged Brie" actually increases in Quality the older it gets
        '''
        item1 = Item("Aged Brie", 10, 10)
        item2 = Item("Aged Brie", 0, 10)
        GildedRose([item1,item2]).update_quality()
        self.assertEqual(item1.quality, 11, "'Aged Brie' actually increases in Quality the older it gets")
        self.assertEqual(item2.quality, 8, "Once the sell by date has passed, Quality degrades twice as fast")

    def test_quality_no_more_fifty(self):
        '''
        The Quality of an item is never more than 50
        '''
        item = Item("Aged Brie", 10,50)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 50, "The Quality of an item is never more than 50")
        self.assertRaises(Exception, Item, "Aged Brie", 10, 51)

    def test_decrease(self):
        '''
        At the end of each day our system lowers both values for every item
        '''
        item = Item("Aged Brie", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 11, "At the end of each day our system lowers both values for every item & 'Aged Brie' actually increases in Quality the older it gets")
        self.assertEqual(item.sell_in, 4, "At the end of each day our system lowers both values for every item & 'Aged Brie' actually increases in Quality the older it gets")


if __name__ == '__main__':
    unittest.main()
