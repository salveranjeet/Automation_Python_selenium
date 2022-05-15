from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def condition_commands():
    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = 'https://opensource-demo.orangehrmlive.com/'
    Driver.get(application_url)
    Driver.maximize_window()

    usr = Driver.find_element_by_id('txtUsername')

    ### returns TRUE or FALSE
    print(usr.is_displayed())
    print(usr.is_enabled())

    pwd = Driver.find_element_by_id('txtPassword')
    print(pwd.is_displayed())
    print(pwd.is_enabled())

    usr.send_keys('Admin')
    pwd.send_keys('admin123')

    Driver.find_element_by_id('btnLogin').click()
    return Driver

condition_commands()
