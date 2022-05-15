import XLUtils
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = 'E:\\browser_drivers\\chromedriver_win32\\chromedriver.exe'
Driver = webdriver.Chrome(executable_path=driver_path)
application_url = "https://demo.guru99.com/test/newtours/"

Driver.get(application_url)
# Driver.maximize_window()
Driver.implicitly_wait(10)

print(Driver.current_url)

excel_file_path = 'C:\\Users\\ranje\\Downloads\\login1.xlsx'

rows = XLUtils.getRowCount(excel_file_path,"Sheet1")

for r in range(2,rows+1):
    userName = XLUtils.readData(excel_file_path,"Sheet1",r,1)  ###captured username and password from excel
    passWord = XLUtils.readData(excel_file_path,"Sheet1",r,2)

    Driver.find_element_by_name('userName').send_keys(userName)  ### sent username and password to the application
    Driver.find_element_by_name('password').send_keys(passWord)

    Driver.find_element_by_name('submit').click()

    if Driver.title == "Login: Mercury Tours":  ### verifying title
        print("TC Passed")
        XLUtils.writeData(excel_file_path,"Sheet1",r,3,"TC Passed")

    # elif Driver.title == 'Welcome: Mercury Tours':
    #     print("TC Failed")
    #     XLUtils.writeData(excel_file_path,"Sheet1",r,3,"TC Failed")

    else:
        print("TC Failed")
        XLUtils.writeData(excel_file_path, "Sheet1", r, 3, "TC Failed")

    # ActionChains(Driver).move_to_element(Driver.find_element_by_id('welcome')).click().perform()
    # ActionChains(Driver).move_to_element(Driver.find_element_by_link_text('Logout')).click().perform()

    # Driver.find_element_by_link_text("Home").click()
    Driver.back()
    Driver.find_element_by_name('userName').clear()
    

