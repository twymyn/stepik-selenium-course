from selenium import webdriver
import time
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    # element = browser.find_element_by_css_selector("input[type=file]")
    # element.send_keys(file_path)

    # get x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # scroll the view
    answer = browser.find_element_by_id("answer")
    checkbox = browser.find_element_by_id("robotCheckbox")
    radio_label = browser.find_element_by_css_selector("#robotsRule")
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("arguments[0].scrollIntoView(true);", answer)

    # fill the field
    answer.send_keys(y)

    # checkbox
    checkbox.click()

    # radio button
    radio_label.click()

    # submit answer
    button.click()

    print("Test passed")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()