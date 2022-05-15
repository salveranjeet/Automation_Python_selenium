import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def mouse_doubleClick():

    driver_path = "C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe"
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = "https://testautomationpractice.blogspot.com/"
    Driver.get(application_url)
    Driver.maximize_window()
    Driver.implicitly_wait(10)

    element = Driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
    ActionChains(Driver).double_click(element).perform()

    time.sleep(5)
    return Driver

mouse_doubleClick()
