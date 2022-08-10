from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def working_with_web_tables():
    Driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    application_url = 'https://www.techlistic.com/p/demo-selenium-practice.html'
    Driver.get(application_url)
    Driver.implicitly_wait(10)


#### Finding number of rows and colums in table
    rows = len(Driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr")) ### will give number of rows in web table
    print(rows)

    cols = len(Driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr[1]/th"))   ### will give number of columns
    print(cols)

####  Extracting value from table
    print("company"+"    "+"Contact"+"    "+"Country")

    for r in range(2,rows+1):
        for c in range(1,cols+1):
            value = Driver.find_element(By.XPATH,"//*[@id='countries']/tbody/tr[2]/td[2]").text  #will extract value from 2nd row 2nd column
            # value = Driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text  # will extract all values
            print(value,end='         ')
        print()
    return Driver

working_with_web_tables()

