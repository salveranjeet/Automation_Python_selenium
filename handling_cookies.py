#### operation on cookies ####
# 1. capture all cookies from browser
# 2. count number of cookies
# 3. read cookie pair
# 4. adding new cookies
# 5. deleting specific cookie by using name of cookie
# 6. deleting all cookies
import time

from selenium import webdriver

def cookies_operations():

    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = "https://www.amazon.in/"
    Driver.get(application_url)
    Driver.implicitly_wait(10)

    ### 1. capture all cookies from browser

    cookies = Driver.get_cookies()
    print(len(cookies))
    print(cookies)

    ### 4. adding new cookies

    # cookie = {"name":"Mycookie","value":"123456"}
    # Driver.add_cookie(cookie)
    #
    # cookies = Driver.get_cookies()
    # print(len(cookies))
    # print(cookies)
    #
    # ### 5. deleting specific cookie by using name of cookie
    #
    # Driver.delete_cookie('Mycookie')
    # time.sleep(5)
    # cookies = Driver.get_cookies()
    # print(len(cookies))
    # print(cookies)

    ### 6. deleting all cookies

    # Driver.delete_all_cookies()
    # cookies = Driver.get_cookies()
    # print(len(cookies))
    # print(cookies)

    ### 3. read cookie pair



    return Driver

cookies_operations()

