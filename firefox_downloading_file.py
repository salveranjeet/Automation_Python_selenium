import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def firefoxBrowser_download_file():

    #### changing location of download

    fp = webdriver.FirefoxProfile()

    fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf")   #mime type(text/plain--for text file) and
                                                                                                # application/pdf-- for pdf file
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir","E:\python_code")
    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("pdfjs.disabled",True)

    driver_path = "C:\\Users\\ranje\\Downloads\\geckodriver-v0.30.0-win32\\geckodriver.exe"

    Driver = webdriver.Firefox(executable_path=driver_path,firefox_profile=fp)   ####initiating the object we created fp


    application_url = "http://demo.automationtesting.in/FileDownload.html"
    Driver.get(application_url)
    Driver.maximize_window()
    Driver.implicitly_wait(10)

    #### 1. Downloading text file

    Driver.find_element_by_id("textbox").send_keys("Hi, I am Ranjeet")
    Driver.find_element_by_id("createTxt").click()   ### generate file button
    Driver.find_element_by_id("link-to-download").click()   ### download link

    #### 2. Downloading PDF file
    Driver.find_element_by_id("pdfbox").send_keys("Hi, I am Sonu")
    Driver.find_element_by_id("createPdf").click()  ### generate file button
    Driver.find_element_by_id("pdf-link-to-download").click()  ### download link

    time.sleep(10)
    return Driver

firefoxBrowser_download_file()
