from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver_path = Service("E:\\browser_drivers\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(driver_path)

driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
driver.implicitly_wait(10)
driver.find_element(By.ID,"tags").send_keys("S")

autocompletelist = driver.find_element(By.XPATH,"//ul[@id='ui-id-1']//li")
for ele in autocompletelist:
    if ele.text == "Selenium":
        ele.click()
        break


