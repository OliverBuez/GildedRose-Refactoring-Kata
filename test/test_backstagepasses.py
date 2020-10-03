# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from items import Item

class BackstagePassesTest(unittest.TestCase):

    def test_after_passed_decrease(self):
        '''
        Once the sell by date has passed, Quality degrades twice as fast
        '''
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 0, "Quality drops to 0 after the concert")
    
    def test_quality_never_negative(self):
        '''
        The Quality of an item is never negative
        '''
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 1)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 0, "The Quality of an item is never negative")
        self.assertRaises(Exception, Item, "Backstage passes to a TAFKAL80ETC concert", 5, -1)

    def test_quality_no_more_fifty(self):
        '''
        The Quality of an item is never more than 50
        '''
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10,50)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 50, "The Quality of an item is never more than 50")
        self.assertRaises(Exception, Item, "Backstage passes to a TAFKAL80ETC concert", 10, 51)

    def test_backstage_passes(self):
        '''
        "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
	    Quality drops to 0 after the concert
        '''
        item1 = Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)
        item2 = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
        item3 = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        GildedRose([item1,item2, item3]).update_quality()
        self.assertEqual(item1.quality, 12, "Quality increases by 2 when there are 10 days or less")
        self.assertEqual(item2.quality, 13, "Quality increases by 3 when there are 5 days or less")
        self.assertEqual(item3.quality, 0, "Quality drops to 0 after the concert")

    def test_decrease(self):
        '''
        At the end of each day our system lowers both values for every item
        '''
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.quality, 13, "At the end of each day our system lowers both values for every item & Quality increases by 3 when there are 5 days or less")


if __name__ == '__main__':
    unittest.main()
