# how many links present
# capture all the links in web page
# click on the links
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def working_with_links():
    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    # application_url = 'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'
    application_url = 'http://automationpractice.com/index.php'
    Driver.get(application_url)
    Driver.implicitly_wait(10)

    links = Driver.find_elements(By.TAG_NAME,"a")

    ### finding all the links in web page (a_href)
    print("Number of links: ",len(links)) # number of links present

    ### extracting each and every link in web-page
    for link in links:
        print(link.text)

    ### clicking on a particular link
    # Driver.find_element(By.LINK_TEXT,'Women').click()   # by LINK_TEXT

    Driver.find_element(By.PARTIAL_LINK_TEXT,'Con').click()  # by PARTIAL_LINK_TEXT


    return Driver

working_with_links()
time.sleep(10)
