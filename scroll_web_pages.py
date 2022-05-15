import time

from selenium import webdriver

def scroll_web_pages():

    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = "https://www.countries-ofthe-world.com/flags-of-the-world.html"
    Driver.get(application_url)
    Driver.implicitly_wait(10)
    Driver.maximize_window()

    ### 1. Scroll down page by pixel
    # Driver.execute_script("window.scrollBy(0,1000)","")

    ### 2. Scroll down the page by element
    # flag = Driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[72]/td[1]/img")
    # Driver.execute_script("arguments[0].scrollIntoView();",flag)

    ### 3. Scroll down till end of the page
    Driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    
    time.sleep(5)
    return Driver

scroll_web_pages()
