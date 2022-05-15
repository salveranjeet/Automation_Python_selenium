import time

from selenium import webdriver

def handling_windows():
    driver_path = "C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe"
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = 'http://demo.automationtesting.in/Windows.html'
    Driver.get(application_url)
    Driver.implicitly_wait(10)
    Driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

    print(Driver.current_window_handle)   #### value of parent window

    handles = Driver.window_handles  ### values of each and every window open on browser
    for h in handles:
        Driver.switch_to.window(h)    ### switch to currently opened window
        print(Driver.title)

        if Driver.title == 'Frames & windows':
            Driver.close() ### close parent window

    time.sleep(10)
    return Driver


handling_windows()


