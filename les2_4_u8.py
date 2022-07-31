from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    WebDriverWait(browser, 7).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text.strip())
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(math.log(abs(12 * math.sin(x))))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

