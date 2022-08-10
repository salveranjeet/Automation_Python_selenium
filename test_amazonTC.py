from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select





def test_amazon():

    url = "https://www.amazon.in/"
    drpdwn_select_category_xpath = "//select[@id='searchDropdownBox']"
    textbox_id = "twotabsearchtextbox"
    search_icon_id = "nav-search-submit-button"


    driver_path = 'E:\\browser_drivers\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)

    Wait = WebDriverWait(driver, 20)
    driver.get(url)
    # driver.maximize_window()
    driver.implicitly_wait(10)

    Wait.until(EC.element_to_be_clickable((By.XPATH,drpdwn_select_category_xpath)))
    drpdwn = Select(driver.find_element(By.XPATH,drpdwn_select_category_xpath))
    drpdwn.select_by_value("search-alias=electronics")

    driver.find_element(By.ID,textbox_id).send_keys("Samsung LED TV")
    driver.find_element(By.ID,search_icon_id).click()

    return driver

test_amazon()









