from selenium import webdriver
import time

def multiple_frames():
    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = "https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html"
    Driver.get(application_url)
    Driver.implicitly_wait(10)

    ### switching focus to 1st fram out of 3 frames
    Driver.switch_to.frame("packageListFrame")

    ### finding an element in 1st fram and clicking it
    Driver.find_element_by_link_text('org.openqa.selenium').click()
    time.sleep(5)

    ### switching back to default main page
    Driver.switch_to.default_content()
    time.sleep(5)

    ### 2nd frame
    Driver.switch_to.frame("packageFrame")
    Driver.find_element_by_link_text('WebDriver').click()
    time.sleep(5)
    Driver.switch_to.default_content()
    time.sleep(5)

    ### 3rd frame
    Driver.switch_to.frame("classFrame")
    Driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[1]/ul/li[6]').click()
    time.sleep(5)
    Driver.switch_to.default_content()
    time.sleep(5)

    return Driver

multiple_frames()
time.sleep(10)


