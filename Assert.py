import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def test_Name(self):
        # driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
        # self.Driver = webdriver.Chrome(executable_path=driver_path)
        # # self.Driver = None
        # application_url = 'https://opensource-demo.orangehrmlive.com/'
        # self.Driver.get(application_url)
        # self.Driver.implicitly_wait(10)

        # title = self.Driver.title

        #### 1. assertEqual()    # if we have two parameters to compare
        # self.assertEqual("OrangeHRM",title,"ErrorMessage-Title not same")

        #### 2. assertNotEqual()
        # self.assertNotEqual("OrangeHRM",title,"ErrorMessage-Title same")

        #### 3. assertTrue()  # when we have more than 2 parameters
        # self.assertTrue(title == "OrangeHRM")


        #### 4. assertFalse()
        # self.assertFalse(title == "Orange")

        #### 5. assertIsNone  (if result is none then unittest will pass vice-versa)
        # self.assertIsNone(self.Driver)

        #### 6. assertIsNotNone
        # self.assertIsNotNone(self.Driver)

        #### 7. assertIn
        # list = {"python","selenium","java"}
        # self.assertIn("python",list)

        #### 8. assertNotIn
        # list = {"python", "selenium", "java"}
        # self.assertNotIn("c++",list)

    ##### Relational comparisons #####

        #### 9.assertGreater
        # self.assertGreater(100,10)   # test will pass whenever 1ST VALUE IS GREATER THAN SECONDE VALUE

        #### 10. assertGreterEqual
        # self.assertGreaterEqual(50,50) # test will pass whenever 1ST VALUE IS GREATER than or equal to SECONDE VALUE

        #### 11. assertLess
        # self.assertLess(10,50)  # test will pass whenever 1ST VALUE IS lesser THAN SECONDE VALUE

        #### 11. assertLess
        self.assertLessEqual(50, 50)  # test will pass whenever 1ST VALUE IS lesser THAN or equal to SECONDE VALUE

if __name__ == '__main__':
    unittest.main()






