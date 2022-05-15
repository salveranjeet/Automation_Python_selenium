from selenium import webdriver

def working_with_web_tables():
    driver_path = 'C:\\Users\\ranje\\Downloads\\chromedriver_win32\\chromedriver.exe'
    Driver = webdriver.Chrome(executable_path=driver_path)
    application_url = 'https://www.techlistic.com/p/demo-selenium-practice.html'
    Driver.get(application_url)
    Driver.implicitly_wait(10)


#### Finding number of rows and colums in table
    rows = len(Driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr")) ### will give number of rows in web table
    print(rows)

    cols = len(Driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))   ### will give number of columns
    print(cols)

####  Extracting value from table
    print("company"+"    "+"Contact"+"    "+"Country")

    for r in range(2,rows+1):
        for c in range(1,cols+1):
            # Driver.find_element_by_xpath("//*[@id='countries']/tbody/tr[2]/td[2]").text  #will extract value from 2nd row 2nd column
            value = Driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text  # will extract all values
            print(value,end='    ')
        print()
    return Driver

working_with_web_tables()

