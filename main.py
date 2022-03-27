from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os
# import unittest
# import pytest
from itertools import combinations, permutations

# k = list(permutations([1, 2, 3, 4, 5, 6, 7, 8], 2))
# print(k)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

print(calc('650'))
#
# browser = webdriver.Edge()
#
#
# class TestRegistration:
#     def test_registration_page_1(self):
#         link = "http://suninjuly.github.io/registration1.html"
#         browser.get(link)
#         elements = browser.find_elements(By.TAG_NAME, "input")
#         for element in elements:
#             element.send_keys("Привет, мир")
#         button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#         button.click()
#         time.sleep(1)
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         welcome_text = welcome_text_elt.text
#
#         assert "Congratulations! You have successfully registered!" == welcome_text, "Should be absolute"
#
#     def test_registration_page_2(self):
#         link = "http://suninjuly.github.io/registration2.html"
#         browser.get(link)
#         first_block_first = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
#         first_block_first.send_keys("Test first name")
#         first_block_second = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
#         first_block_second.send_keys("Test last name")
#         first_block_third = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
#         first_block_third.send_keys("Test email")
#         button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#         time.sleep(1)
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         welcome_text = welcome_text_elt.text
#
#         assert "Congratulations! You have successfully registered!" == welcome_text, "Should be absolute"


# if __name__ == "__main__":
#     TestRegistration.main()