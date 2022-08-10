import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def tables():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.goibibo.com/")

    driver.switch_to.alert.dismiss()
    driver.find_element(By.CLASS_NAME,"sc-GEbAx kenSRj").click()

    departure_city = driver.find_element(By.CLASS_NAME, "sc-iJKOTD iipKRx fswWidgetPlaceholder")
    for ele in departure_city:
        if ele.text == "New Delhi":
            ele.click()
            break

    destination_city = driver.find_element(By.CLASS_NAME, "sc-iJKOTD iipKRx fswWidgetPlaceholder")
    for ele in destination_city:
        if ele.text == "Mumbai":
            ele.click()
            break

    driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div/div[1]/div[3]").click()
    driver.switch_to.frame("//div[@class='sc-jgrJph gAiyey']")
    driver.find_element(By.XPATH,"//div[@aria-label='Tue Aug 16 2022']").click()
    driver.find_element(By.XPATH, "//div[@aria-label='Thu Sep 29 2022']").click()
    driver.find_element(By.CLASS_NAME, "fswTrvl__done").click()
    driver.find_element(By.CLASS_NAME, "sc-dtMgUX daltrV").click()
    driver.find_element(By.XPATH, "//span[@class='sc-fHeRUh jHgPBA']").click()
    return driver

tables()
























