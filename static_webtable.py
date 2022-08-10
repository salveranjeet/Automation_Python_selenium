from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

ser_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service= ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# tbody: represents the whole body of your table
# tr: each tr represents a table row
# th: table header available in 1st row
# td: table data(data in the table)
#(mostly we use customized XPaths)

             ### 1: Count no. of rows and columns

# xpath to capture all rows:  //table[@name='BookTable']/tbody/tr  or //table[@name='BookTable']//tr
rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# print(rows)

# xpath to capture all Cols: //table[@name='BookTable']//tr[1]//th
cols = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]//th"))
# print(cols)


           ### 2: Read specific row and column data

# slecting amod from 2nd columns and 6th row( by using row no. and table body no.
# value = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[6]/td[2]").text
# print(value)

           ### 3: Read all the rows and column data

# for r in range(2, rows+1):
#     for c in range(1, cols+1):
#         data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td["+str(c)+"]").text
#         print(data,end=' ')
#     print()  #jump to the next row


          ### 4: Read the data based on condition

for r in range(2, rows+1):
    subject = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]//td[3]").text
    if subject == "JAVA":
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]//td[1]").text
        print(bookname)








