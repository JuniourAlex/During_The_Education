import unittest
from main import sum, num, dev

class MainTesting(unittest. TestCase):
    def test1_sum (self):
        return self.assertEquals(sum(2, 2), 4)

    def test2_num (self):
        return self.assertEquals(num(4, 2), 2)

    def test3_dev(self):
        return self.assertEquals(dev(6, 2), 3)

unittest.main()