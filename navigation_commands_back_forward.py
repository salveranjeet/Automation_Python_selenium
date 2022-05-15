from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#### "back" and "forward" click on browser ####

def back_and_fwd_navigation():

    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)

    application_url1 = 'https://opensource-demo.orangehrmlive.com/'
    application_url2 = 'https://demoqa.com/'

    Driver.get(application_url1) # 1st this url will be opened
    time.sleep(5)
    print(Driver.title)

    Driver.get(application_url2) # 2nd again in same window this url will be opened
    time.sleep(5)
    print(Driver.title)

    Driver.back()   # going back to 1st window from 2nd window
    time.sleep(5)
    print(Driver.title)

    Driver.forward()  # going from 1st window to 2nd window
    time.sleep(5)
    print(Driver.title)

    return Driver

back_and_fwd_navigation()


