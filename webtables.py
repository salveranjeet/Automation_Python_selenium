import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def webtable():
    Driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    application_url = 'https://www.dezlearn.com/webtable-example/'
    Driver.get(application_url)
    Driver.maximize_window()
    Driver.implicitly_wait(10)

#### Finding number of rows and colums in table
    rows = len(Driver.find_elements(By.XPATH, "//tbody//tr"))
    cols = len(Driver.find_elements(By.XPATH, "//tbody//tr//th"))

    for r in range(2,rows+1):
        name= Driver.find_element(By.XPATH,"//tbody//tr[" + str(r) + "]//td[1]").text
        if name == "John White":
            standard = Driver.find_element(By.XPATH,"//tbody//tr//td[3]//input[@type='checkbox']").click()
            premium = Driver.find_element(By.XPATH,"//tbody//tr//td[4]//input[@type='checkbox']").click()
            # print(email)
            time.sleep(5)
    return Driver

webtable()





