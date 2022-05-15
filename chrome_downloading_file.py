import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def chromeBrowser_download_file():

    #### changing location of download

    chromeOptions = Options()
    chromeOptions.add_experimental_option("prefs",{"download.default_directory":"E:\python_code"})

    driver_path = "C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe"

    Driver = webdriver.Chrome(executable_path=driver_path,chrome_options=chromeOptions)   ###initiating the object we created

    application_url = "http://demo.automationtesting.in/FileDownload.html"
    Driver.get(application_url)
    Driver.maximize_window()
    Driver.implicitly_wait(10)

    #### 1. Downloading text file

    # Driver.find_element_by_id("textbox").send_keys("Hi, I am Ranjeet")
    # Driver.find_element_by_id("createTxt").click()   ### generate file button
    # Driver.find_element_by_id("link-to-download").click()   ### download link

    #### 2. Downloading PDF file
    Driver.find_element_by_id("pdfbox").send_keys("Hi, I am Sonu")
    Driver.find_element_by_id("createPdf").click()  ### generate file button
    Driver.find_element_by_id("pdf-link-to-download").click()  ### download link

    time.sleep(10)
    return Driver

chromeBrowser_download_file()


