from selenium import webdriver
import time
import os 

file_name = "file.txt"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, file_name)

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # fill the fields
    elements = browser.find_elements_by_css_selector("input[type=text")
    for element in elements:
        element.send_keys("bla")

    # create file.txt

    with open(file_path, "w") as file:
        file.write("automation! with python and selenium!")
        file.close()

    # select file
    file_upload = browser.find_element_by_css_selector("input[type=file]")
    file_upload.send_keys(file_path)

    # submit answer
    button = browser.find_element_by_tag_name("button")
    button.click()

    print("Test passed")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()