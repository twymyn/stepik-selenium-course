from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/wait1.html"

try: 
    browser = webdriver.Chrome()
    # setup to lookup for elements for 5 sec in the worst case
    browser.implicitly_wait(5)
    browser.get(link)

    # click the button
    verify_button = browser.find_element_by_id("verify")
    verify_button.click()
    message = browser.find_element_by_id("verify_message")
    assert "successful" in message.text

    print("Test passed")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()