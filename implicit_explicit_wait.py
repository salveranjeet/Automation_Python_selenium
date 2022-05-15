from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait


def implicit_explicit_wait():

    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = 'http://automationpractice.com/index.php'
    Driver.get(application_url)
    assert "My Store" in Driver.title    # verifying title

    Driver.implicitly_wait(10)  # implicitly waits for 10 second (is applicable for all the elements on the page)

    # Driver.maximize_window()
    # dashboardPage = implicit_explicit_wait()
    # ActionChains(Driver).move_to_element(Driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[1]/a')).click().perform()

    ######## explicit wait condition  #######

    try:
        wait = WebDriverWait(Driver,10)
        time.sleep(10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='block_top_menu']/ul/li[1]/a")))
        element.click()
    except:
        print("Error from explicit wait")

    return Driver

implicit_explicit_wait()
time.sleep(20)

