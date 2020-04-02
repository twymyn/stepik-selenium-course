from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def sum(x, y):
  return int(x) + int(y)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # getting X Y value
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    value = str(sum(x, y))

    # select the answer
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(value)

    # submit answer
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print("Test passed")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()