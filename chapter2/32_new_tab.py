from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # first tab handler
    first_window = browser.window_handles[0]
    # browser.switch_to.window(first_window)

    # troll button
    troll_button = browser.find_element_by_tag_name("button")
    troll_button.click()

    # second tab handler
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    # getting X value
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # fill the field
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    # submit answer
    submit_button = browser.find_element_by_id("solve")
    submit_button.click()

    print("Test passed")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()