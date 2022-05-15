import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def radioButton_checkBox():

    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = 'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'
    Driver.get(application_url)
    Driver.implicitly_wait(10)
    # Driver.maximize_window()

    #explicit wait
    try:
        wait = WebDriverWait(Driver,20)
        time.sleep(10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='RESULT_RadioButton-7_0']")))
        element.click()
    except:
        print("Error from Explicit wait")

    return Driver

radioButton_checkBox()


# Driver.quit()

    ##working with the radio-buttons
# status = Driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()  # returns True or FALSE
# print(status)

# Driver.find_element_by_id('RESULT_RadioButton-7_0').click()   #selecting radio button

# status = Driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()  # returns True or FALSE
# print(status)

#     return Driver
#
# radioButton_checkBox()
