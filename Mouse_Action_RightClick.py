import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def mouse_rightClick():

    driver_path = "C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe"
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = "https://swisnl.github.io/jQuery-contextMenu/demo.html"
    Driver.get(application_url)
    Driver.maximize_window()
    Driver.implicitly_wait(10)

    rightClickButton = Driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
    ActionChains(Driver).context_click(rightClickButton).perform()   #### context_click for right click

    time.sleep(5)
    return Driver

mouse_rightClick()
