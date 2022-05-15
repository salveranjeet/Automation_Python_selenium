from selenium import webdriver

def capture_screenshots():

    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = "https://opensource-demo.orangehrmlive.com/"
    Driver.get(application_url)
    Driver.implicitly_wait(10)

    # Driver.save_screenshot("E:\screenshots\homepage.png")

    Driver.get_screenshot_as_file("E:\screenshots\homepage1.png")


    return Driver

capture_screenshots()
