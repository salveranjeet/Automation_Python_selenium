import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import mysql.connector

# serv_obj = Service("E:\\browser_drivers\\chromedriver_win32\\chromedriver.exe")
# driver=webdriver.Chrome(service = serv_obj)

driver_path = 'E:\\browser_drivers\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(10)

try:
    con= mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="testdb")
    curs= con.cursor()
    curs.execute("select * from caldata;")

    for row in curs:
        #reading data from db and storing it in variables
        principalAmount = row[0]
        rateOfInterest = row[1]
        period1 = row[2]
        period2 = row[3]
        frequency = row[4]
        exp_mvalue = row[5]

        #passing data to the application
        driver.find_element(By.ID,"principal").send_keys(principalAmount)
        driver.find_element(By.ID,"interest").send_keys(rateOfInterest)
        driver.find_element(By.ID,"tenure").send_keys(period1)

        #period drop down
        PeriodDrpDwn= Select(driver.find_element(By.ID,"tenurePeriod"))
        PeriodDrpDwn.select_by_visible_text(period2)

        #frequency drop down
        FreqDrpDwn= Select(driver.find_element(By.ID,"frequency"))
        FreqDrpDwn.select_by_visible_text(frequency)

        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()

        act_mvalue= driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

        #validation of m-value
        if float(exp_mvalue) == float(act_mvalue):
            print("Test Passed")
        else:
            print("Test Failed")

        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(3)

    con.close()

except:
    print("Connection unsuccessful")

driver.close()



