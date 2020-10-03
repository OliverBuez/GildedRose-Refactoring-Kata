# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from items import Item

class AbstractItemTest(unittest.TestCase):

    def test_after_passed_decrease(self):
        '''
        Once the sell by date has passed, Quality degrades twice as fast
        '''
        item = Item("test", 0, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 8, "Once the sell by date has passed, Quality degrades twice as fast")
    
    def test_quality_never_negative(self):
        '''
        The Quality of an item is never negative
        '''
        item1 = Item("test1", 5, 0)
        item2 = Item("test2", 0, 1)
        GildedRose([item1,item2]).update_quality()
        self.assertEqual(item1.quality, 0, "The Quality of an item is never negative")
        self.assertEqual(item2.quality, 0, "The Quality of an item is never negative")
        self.assertRaises(Exception, Item, "test", 5, -1)

    def test_quality_no_more_fifty(self):
        '''
        The Quality of an item is never more than 50
        '''
        self.assertRaises(Exception, Item, "test1", 10, 51)


    def test_decrease(self):
        '''
        At the end of each day our system lowers both values for every item
        '''
        item = Item("test", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 9, "At the end of each day our system lowers both values for every item")


if __name__ == '__main__':
    unittest.main()
