import time

from selenium import webdriver


def test_open_vwologin():
    driver  = webdriver.Chrome()
    # Code -> HTTP REQUEST - POST
    # POST request | Create the Session
    # Session is created - Unique ID - 16 digit ID
    # session id - 283dbd4b8dfdb64de1aecb090d35bfbf

    # driver  = webdriver.Edge()
    # driver  = webdriver.firefox()


    print(driver.session_id)
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"

    time.sleep(10)    #Python Int - to stop for the 10 seconds




