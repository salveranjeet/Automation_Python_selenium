from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def input_boxes():
    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = 'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'
    Driver.get(application_url)
    Driver.implicitly_wait(10)
    # Driver.maximize_window()

    ### How to find how many input boxes present in webPage (search for comman parameter)
    inputboxes = Driver.find_elements(By.CLASS_NAME,"text_field")
    print(len(inputboxes))

    ## How to provide value into the text-box-(send_keys)
    Driver.find_element_by_id('RESULT_TextField-1').send_keys("Salman")
    Driver.find_element_by_id('RESULT_TextField-2').send_keys("Khan")

    return Driver

input_boxes()
time.sleep(10)

