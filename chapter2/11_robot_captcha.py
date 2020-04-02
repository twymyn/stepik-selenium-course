from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # getting X value
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # fill the field
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # checkbox
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    # radio button
    radio_label = browser.find_element_by_css_selector("[for=robotsRule]")
    radio_label.click()

    # submit answer
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    print("Test passed")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()