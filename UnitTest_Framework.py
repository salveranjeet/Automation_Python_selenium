import unittest

def setUpModule():   # will be executed befor executing a class

def tearDownModule():  # will be executed after executing a class


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):   # will execute every time before executing a method
        print("This is login Test")

    @classmethod
    def tearDown(self):   # will execute every time after executing a method
        print("This is logout Test")

    @classmethod
    def setUpClass(cls):    # will execute only once before executing all the methods
        print("Opening application")

    @classmethod
    def tearDownClass(cls):  # will execute only once after executing all the methods
        print("Close application")

    def test_search(self):
        print("This is search Test")

    def test_advancedSearch(self):
        print("This is advanced search Test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge Test")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge Test")

if __name__ == '__main__':
    unittest.main()

