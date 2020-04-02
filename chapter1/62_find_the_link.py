from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"
# 224592
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link_element = browser.find_element_by_link_text(link_text)

    link_element.click()

    first_name = browser.find_element_by_tag_name("input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_name("last_name")
    last_name.send_keys("Petrov")
    city = browser.find_element_by_class_name("city")
    city.send_keys("Smolensk")
    country = browser.find_element_by_id("country")
    country.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла