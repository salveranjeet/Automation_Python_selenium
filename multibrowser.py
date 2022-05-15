from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Firefox
# def launch_browser():
#     driver_path = 'C:\\Users\\ranje\\Downloads\\geckodriver-v0.30.0-win32\\geckodriver.exe'
#     Driver = webdriver.Firefox(executable_path = driver_path)
#     application_url = 'https://demoqa.com/'
#     Driver.get(application_url)
#     print(Driver.title)
#     Driver.maximize_window()
#     return Driver
#
# launch_browser()

#chrome
def launch_browser():
    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path = driver_path)
    application_url = 'http://automationpractice.com/index.php'
    Driver.get(application_url)

    print(Driver.title)   ##### returns "title" of the page
    print(Driver.current_url)   #### returns "URL" of page
    Driver.maximize_window()

    # Driver.close() #### closes the parent window(will close one browser at a time
    # Driver.quit() #### will close all the browsers

    return Driver

launch_browser()
time.sleep(10)

