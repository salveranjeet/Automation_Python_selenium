import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver_path = "C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe"
Driver = webdriver.Chrome(executable_path=driver_path)
application_url = "https://testautomationpractice.blogspot.com/"
Driver.get(application_url)

Driver.implicitly_wait(20)
Driver.maximize_window()

Driver.switch_to.frame(0)
image = 'C://Users/ranje/Downloads/sel.png'
Driver.find_element_by_id('RESULT_FileUpload-10').send_keys(image)

    # try:
    #     wait = WebDriverWait(Driver,10)
    #     time.sleep(10)
    #     element = wait.until(EC.element_to_be_clickable((By.ID,"RESULT_FileUpload-10")))
    #
    # except:
    #     print("Error from explicit wait")

time.sleep(10)


