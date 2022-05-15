import time
from selenium import webdriver

def alerts():

    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = 'https://testautomationpractice.blogspot.com/'
    Driver.get(application_url)
    Driver.implicitly_wait(10)

    Driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
    time.sleep(5)

    # Driver.switch_to_alert().accept()  ### for swtiching to alert ...will select 'OK'

    Driver.switch_to_alert().dismiss()   ### will select 'CANCEL'


    return Driver

alerts()
time.sleep(5)
