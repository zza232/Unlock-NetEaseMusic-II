# coding: utf-8

import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from retrying import retry

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s %(message)s')

@retry(wait_random_min=5000, wait_random_max=10000, stop_max_attempt_number=3)
def enter_iframe(browser):
    logging.info("Enter login iframe")
    target = browser.find_element(By.XPATH, "//*[starts-with(@id,'x-URS-iframe')]")
    browser.switch_to.frame(target)
    return browser

@retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=5)
def extension_login(email, password):
    chrome_options = webdriver.ChromeOptions()

    logging.info("Load Chrome extension NetEaseMusicWorldPlus")
    chrome_options.add_extension('NetEaseMusicWorldPlus.crx')

    logging.info("Initializing Chrome WebDriver")
    service = Service(ChromeDriverManager().install())  # Auto-download correct chromedriver
    browser = webdriver.Chrome(service=service, options=chrome_options)

    # Set global implicit wait
    browser.implicitly_wait(20)

    browser.get('https://music.163.com')

    # Find and click login button
    logging.info("Click login button")
    login_button = browser.find_element(By.XPATH, "//a[text()='登录']")
    browser.execute_script('arguments[0].scrollIntoView(true);', login_button)
    time.sleep(2)
    login_button.click()

    # Select login method
    logging.info("Select login method")
    time.sleep(2)
    browser.find_element(By.XPATH, "//a[text()='选择其他登录模式']").click()

    # Agree to terms
    logging.info("Agree to terms")
    browser.find_element(By.ID, 'j-official-terms').click()

    # Choose email login
    logging.info("Select email login")
    browser.find_element(By.XPATH, "//a[text()='网易邮箱帐号登录']").click()

    # Enter login iframe
    time.sleep(5)
    browser = enter_iframe(browser)

    # Enter email and password
    logging.info("Enter credentials")
    browser.find_element(By.CSS_SELECTOR, "input.j-inputtext[name='email']").send_keys(email)
    browser.find_element(By.NAME, 'password').send_keys(password)

    time.sleep(2)

    # Click login button
    logging.info("Submit login")
    browser.find_element(By.ID, 'dologin').click()

    time.sleep(2)

    # Refresh to confirm login
    browser.refresh()
    logging.info("Unlock finished")

    time.sleep(10)
    browser.quit()


if __name__ == '__main__':
    try:
        email = os.environ['EMAIL']
        password = os.environ['PASSWORD']
    except KeyError:
        logging.error('Failed to read email and password.')
    else:
        extension_login(email, password)
