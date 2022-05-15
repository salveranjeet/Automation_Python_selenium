import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):

    def test_Google(self):
        driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
        self.Driver = webdriver.Chrome(executable_path=driver_path)
        application_url = 'https://www.google.com/'
        self.Driver.get(application_url)
        print(self.Driver.title)
        self.Driver.close()

    def test_Bing(self):
        driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
        self.Driver = webdriver.Chrome(executable_path=driver_path)
        application_url = 'https://www.bing.com/'
        self.Driver.get(application_url)
        print(self.Driver.title)
        self.Driver.close()

if __name__== "__main__":
    unittest.main()
