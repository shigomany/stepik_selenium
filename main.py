from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Edge(executable_path=r'msedgedriver.exe')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
try:
    browser.get(link)
    but = browser.find_element(By.ID, 'book')
    cost = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    but.click()

    x = browser.find_element(By.ID, 'input_value')

    field = browser.find_element(By.ID, 'answer')
    field.send_keys(calc(x.text))

    but = browser.find_element(By.ID, 'solve')
    but.click()


finally:
    time.sleep(10)
    browser.quit()
