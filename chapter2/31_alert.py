from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # magic button
    magic_button = browser.find_element_by_tag_name("button")
    magic_button.click()

    # switch to alert
    alert = browser.switch_to.alert
    alert.accept()

    # getting X value
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # fill the field
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    # submit answer
    submit_button = browser.find_element_by_tag_name("button")
    submit_button.click()

    print("Test passed")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()