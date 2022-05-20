import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from ddt_using_excel import XLUtils

# serv_obj = Service("E:\\browser_drivers\\chromedriver_win32\\chromedriver.exe")
# driver=webdriver.Chrome(service = serv_obj)

driver_path = 'E:\\browser_drivers\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(10)

file = "E:\python_code\Automation_Python_selenium\TestData\caldata.xlsx"

rows = XLUtils.getRowCount(file,"Sheet1")
for r in range(2,rows+1):
    principalAmount = XLUtils.readData(file,"Sheet1",r,1)
    rateOfInterest = XLUtils.readData(file,"Sheet1",r,2)
    period1 = XLUtils.readData(file, "Sheet1", r, 3)
    period2 = XLUtils.readData(file, "Sheet1", r, 4)
    frequency = XLUtils.readData(file, "Sheet1", r, 5)
    exp_mvalue = XLUtils.readData(file, "Sheet1", r, 6)

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
        XLUtils.writeData(file,"Sheet1",r,8,"As Expected")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)

    else:
        print("Test Failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Not As Expected")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(3)

driver.close()










