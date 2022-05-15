##packages required for this project
# selenium
# pytest
# allure-pytest

from selenium import webdriver
import pytest
import allure

class test_orangeHRM:

    def test_logo(self):
        driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
        self.Driver = webdriver.Chrome(executable_path=driver_path)
        application_url = 'https://opensource-demo.orangehrmlive.com/'
        self.Driver.get(application_url)
        self.Driver.maximize_window()

        status = self.Driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if status == True:
            assert True
        else:
            assert False

        self.Driver.close()

    def test_listEmployees(self):
        pytest.skip("Skipping Test")

    def test_login(self):
        driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
        self.Driver = webdriver.Chrome(executable_path=driver_path)
        application_url = 'https://opensource-demo.orangehrmlive.com/'
        self.Driver.get(application_url)
        self.Driver.maximize_window()
        self.Driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.Driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.Driver.find_element_by_id('btnLogin').click()
        page_title = self.Driver.title

        if page_title == "OrangeHRM":
            self.Driver.close()
            assert True

        else:
            self.Driver.close()
            assert False
        # assert self.Driver.title=="OrangeHRM"






