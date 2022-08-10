from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))



driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.maximize_window()

recruitment_menu_xpath = "//a[@id='menu_recruitment_viewRecruitmentModule']"
candidates_menu_xpath = "//a[@id='menu_recruitment_viewCandidates']"
username_textbox_id = "txtUsername"
password_textbox_id = "txtPassword"
login_button_id = "btnLogin"

Wait = WebDriverWait(driver, 10)

driver.find_element(By.ID,username_textbox_id).send_keys("Admin")
driver.find_element(By.ID,password_textbox_id).send_keys("admin123")
driver.find_element(By.ID,login_button_id).click()

Wait.until(EC.presence_of_element_located((By.XPATH, recruitment_menu_xpath)))
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,recruitment_menu_xpath)) \
    .move_to_element(driver.find_element(By.XPATH,candidates_menu_xpath)).click().perform()
