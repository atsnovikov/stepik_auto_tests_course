'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(str(y))
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    browser.execute_script('window.scrollBy(0, 50);')
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

import time
import math
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait

try:
    for line in open('tttt.txt'): print(line, end='')

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price100 = WebDriverWait(browser, 25).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element(By.ID, "book").click()
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(str(y))
    button = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    '''
    new_win = browser.window_handles[1]
    browser.switch_to.window(new_win)
    #confirm.accept()
    browser.find_element(By.ID, 'answer').send_keys(calc(int(browser.find_element(By.ID, 'input_value').text)))
    browser.find_element(By.TAG_NAME, 'button').click()'''


finally:
    time.sleep(2)
    browser.quit()