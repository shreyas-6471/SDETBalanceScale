from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time
counter=1
def setup_driver():
    """Sets up the Selenium WebDriver."""
    driver = webdriver.Firefox()
    driver.get("http://sdetchallenge.fetch.com/")
    return driver

def fill_board(driver, side, values):
    """Fills the specified side of the board with given values."""
    xpath = f"(//div[contains(@class, 'board-row')])[{side}]//input"
    inputs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )
    for i, value in enumerate(values):
        inputs[i].send_keys(str(value))
        
def weigh_bars(driver, left_values, right_values):
    """Performs the weighing of bars and returns the result."""
    driver.find_element(By.XPATH, "//button[text()='Reset']").click()
    fill_board(driver, 1, left_values)
    fill_board(driver, 4, right_values)
    driver.find_element(By.XPATH, "//button[text()='Weigh']").click()
    global counter
    WebDriverWait(driver, 20).until(
        lambda d: len(d.find_elements(By.XPATH, "//li")) >= (counter)
    )
    counter=counter+1
    last_li_element = driver.find_elements(By.XPATH, "//li")[-1]
    return last_li_element.text

def perform_search(driver, start, end):
    """Recursively searches for the counterfeit bar and returns its number."""
    if start == end:
        select_fake_bar(driver, start)
        return start

    num_bars = end - start + 1
    third = num_bars // 3
    result = weigh_bars(driver, list(range(start, start + third)),
                        list(range(start + third, start + 2 * third)))
    print("Result is",result)

    if "=" in result:
        return perform_search(driver, start + 2 * third, end)
    elif "<" in result:
        return perform_search(driver, start, start + third - 1)
    else:
        return perform_search(driver, start + third, start + 2 * third - 1)


def select_fake_bar(driver, bar_number):
    """Selects the fake bar and asserts if the correct alert is present."""
    button_xpath = f"//button[text()='{bar_number}']"
    time.sleep(10)
    driver.find_element(By.XPATH, button_xpath).click()
    time.sleep(10)
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        assert "Yay! You find it!" in alert_text, "Alert text does not match expected text."
        print("Correct alert found and assertion passed.")
        alert.accept()
    except NoAlertPresentException:
        assert False, "No alert was present."

def main():
    """Main function to execute the counterfeit bar finding process."""
    driver = setup_driver()
    fake_bar_number = perform_search(driver, 0, 8)
    print(f"Fake bar is number: {fake_bar_number}")
    driver.quit()

if __name__ == "__main__":
    main()
