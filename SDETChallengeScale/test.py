from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://sdetchallenge.fetch.com/")
counterfeit_bar = float('inf')
counter=1
def fill_board(side, values):
    time.sleep(5)
    xpath = "(//div[contains(@class, 'board-row')])[" + str(side) + "]" + "//input"
    inputs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )
    for i, value in enumerate(values):
        inputs[i].send_keys(str(value))
def weigh_bars(left_start, left_end, right_start, right_end):
    driver.find_element(By.XPATH, "//button[text()='Reset']").click()
    left_values = []
    right_values = []
    for i in range(left_start, left_end + 1):
        left_values.append(i)
    for i in range(right_start, right_end + 1):
        right_values.append(i)
    fill_board(1, left_values)
    fill_board(4, right_values)
    driver.find_element(By.XPATH,"//button[text()='Weigh']").click()
    global counter
    wait = WebDriverWait(driver, 20)
    elements = wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//li")) >= counter)
    time.sleep(5)
    last_li_element = driver.find_elements(By.XPATH, "//li")[-1]
    return last_li_element.text
def perform_search(start, end):
    global counterfeit_bar 
    time.sleep(5)
    if (start == end):
        buttonxpth="//button[text()='"+str(start)+"']"
        driver.find_element(By.XPATH,buttonxpth).click()
        counterfeit_bar = start  
        return start
    numBars = end - start + 1
    third = numBars // 3
    operatorexpression = weigh_bars(start, start + third - 1, start + third, start + 2 * third - 1)
    if "=" in operatorexpression:
        perform_search(start + 2 * third, end)
    elif "<" in operatorexpression:
        perform_search(start, start + third - 1)
    else:
        perform_search(start + third, start + 2 * third - 1)
perform_search(0, 8)
time.sleep(5)
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()
time.sleep(10)
driver.quit()