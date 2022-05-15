import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def mouse_hover():

    driver_path = "C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe"
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = "https://opensource-demo.orangehrmlive.com/"
    Driver.get(application_url)
    Driver.maximize_window()
    Driver.find_element_by_id('txtUsername').send_keys('Admin')
    Driver.find_element_by_id('txtPassword').send_keys('admin123')
    Driver.find_element_by_id('btnLogin').click()
    Driver.implicitly_wait(10)

    admin = Driver.find_element_by_id('menu_admin_viewAdminModule')
    userManagement = Driver.find_element_by_id('menu_admin_UserManagement')
    user = Driver.find_element_by_id('menu_admin_viewSystemUsers')

    #### mouse hover
    ActionChains(Driver).move_to_element(admin).move_to_element(userManagement).move_to_element(user).click().perform()

    time.sleep(5)
    return Driver

mouse_hover()
