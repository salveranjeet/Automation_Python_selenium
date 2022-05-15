##### Orange-HRM Login test #####
import time
import unittest
from selenium import webdriver
import HtmlTestRunner

class htmlReporting(unittest.TestCase):

    def setUp(self) -> None:
        driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
        self.Driver = webdriver.Chrome(executable_path=driver_path)
        # application_url = 'https://opensource-demo.orangehrmlive.com/'
        # cls.Driver.get(application_url)
        # cls.Driver.maximize_window()


    def test_verifyHomePageTitle(self):
        application_url = 'https://opensource-demo.orangehrmlive.com/'
        self.Driver.get(application_url)
        # time.sleep(5)
        self.Driver.maximize_window()
        self.assertEqual("OrangeHRM",self.Driver.title,"webpage Title is not matching")

    def test_verifyLogin(self):
        application_url = 'https://opensource-demo.orangehrmlive.com/'
        self.Driver.get(application_url)
        time.sleep(5)
        self.Driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.Driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.Driver.find_element_by_id('btnLogin').click()
        # time.sleep(5)
        self.assertEqual("OrangeHRM", self.Driver.title, "webpage Title is not matching")

    def tearDown(self) -> None:
        self.Driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = "E:\\python_code\\Reports"))



### to generate report we have to run the code through terminal

### python test_htmlReporting.py --> This is the command to run in terminal

