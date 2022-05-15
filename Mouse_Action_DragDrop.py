import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def mouse_drag_and_drop():

    driver_path = "C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe"
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
    # application_url = "https://testautomationpractice.blogspot.com/"
    Driver.get(application_url)
    Driver.maximize_window()
    Driver.implicitly_wait(10)

    source_element = Driver.find_element_by_id('box6')
    target_element = Driver.find_element_by_id('box106')

    ActionChains(Driver).drag_and_drop(source_element,target_element).perform()


    time.sleep(5)
    return Driver

mouse_drag_and_drop()
