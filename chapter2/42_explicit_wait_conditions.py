from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    browser = webdriver.Chrome()
    browser.get(link)

    book_button = browser.find_element_by_id("book")
    # wait for price to drop to 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book_button.click()

    message = browser.find_element_by_id("simple_text")
    assert "Math is real magic!" in message.text

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