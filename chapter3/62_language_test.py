import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urls = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('url', urls)
def test_correct_answer(browser, url):
    link = url
    browser.get(link)

    answer = str(math.log(int(time.time())))

    # textarea = browser.find_element_by_css_selector("textarea[required]")
    textarea = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[required]"))
    )
    textarea.send_keys(answer)

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    # wait for the page to render new element
    banner = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "pre"))
    )
    result = banner.text

    assert "Correct!" == result, "Result is not as expected"
