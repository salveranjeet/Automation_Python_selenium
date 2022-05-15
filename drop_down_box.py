from selenium import webdriver
from selenium.webdriver.support.ui import Select   # for drop-down operations
import time

def dropDown():
    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = 'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'
    Driver.get(application_url)
    Driver.implicitly_wait(10)

    drpDwn = Select(Driver.find_element_by_id('RESULT_RadioButton-9'))

    #capturing all the options in drop-down
    all_options = drpDwn.options
    for options in all_options:
        print(options.text)

    #count number of options
    print(len(drpDwn.options))

    # selection of values
    # drpDwn = Select(Driver.find_element_by_id('RESULT_RadioButton-9'))
    drpDwn.select_by_visible_text('Morning')  #selection of values by visible text


    return Driver

dropDown()
time.sleep(10)



