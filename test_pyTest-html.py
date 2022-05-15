from selenium import webdriver
import pytest  # no need to import pytest-html, it will execute at the run-time

class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
        self.Driver = webdriver.Chrome(executable_path=driver_path)
        yield  #after yeild keyword whatever statment we created will be executed after test_Homepage
        self.Driver.close()

    def test_Homepage(self,setup): # by using setup fixture, setup method will be executed first
        application_url = 'https://opensource-demo.orangehrmlive.com/'
        self.Driver.get(application_url)
        self.Driver.maximize_window()
        assert self.Driver.title=="OrangeHRM"

    def test_Login(self,setup):
        application_url = 'https://opensource-demo.orangehrmlive.com/'
        self.Driver.get(application_url)
        self.Driver.maximize_window()
        self.Driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.Driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.Driver.find_element_by_id("btnLogin").click()
        assert self.Driver.title=="OrangeHRM"


## pytest -v -s --html=report.html test_pyTest-html.py


##  pytest -v -s --html=report.html --self-contained-html test_pyTest-html.py


## pytest -v -s --html=.\Reports\report.html --self-contained-html test_pyTest-html.py   #for saving report in Report directory

