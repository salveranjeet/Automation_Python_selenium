import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest   #(decorator) to skip a test method
    def test_search(self):
        print("This is search Test")

    @unittest.skip("I am skipping this Test method")  # skipping test method by giving a reason
    def test_AdvancedSearch(self):
        print("This is Advanced search Test")


    @unittest.skipIf(1==1,"1==1 is True so condition satisfied")   # skipping test method if condition is true
    def test_prepaidRecharge(self):
        print("This is prepaid recharge Test")

    def test_postpaidRecharge(self):
        print("This is postpaid recharge Test")

    def test_loginByGmail(self):
        print("Login by Gmail Test")

    def test_loginByTwitter(self):
        print("Login by Twitter account")

if __name__ == '__main__':
    unittest.main()
