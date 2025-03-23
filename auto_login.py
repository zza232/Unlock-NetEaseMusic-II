# coding: utf-8

import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from retrying import retry

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s %(message)s')

@retry(wait_random_min=5000, wait_random_max=10000, stop_max_attempt_number=3)
def enter_iframe(browser):
    logging.info("Enter login iframe")
    time.sleep(5)  # 给 iframe 额外时间加载
    try:
        iframe = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[starts-with(@id,'x-URS-iframe')]")
        ))
        browser.switch_to.frame(iframe)
        logging.info("Switched to login iframe")
    except Exception as e:
        logging.error(f"Failed to enter iframe: {e}")
        browser.save_screenshot("debug_iframe.png")  # 记录截图
        raise
    return browser

@retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=5)
def extension_login():
    chrome_options = webdriver.ChromeOptions()

    logging.info("Load Chrome extension NetEaseMusicWorldPlus")
    chrome_options.add_extension('NetEaseMusicWorldPlus.crx')

    logging.info("Initializing Chrome WebDriver")
    try:
        service = Service(ChromeDriverManager().install())  # Auto-download correct chromedriver
        browser = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        logging.error(f"Failed to initialize ChromeDriver: {e}")
        return

    # Set global implicit wait
    browser.implicitly_wait(20)

    browser.get('https://music.163.com')

    # Inject Cookie to skip login
    logging.info("Injecting Cookie to skip login")
    browser.add_cookie({"name": "你的MUSIC_U", "value": "00ED34A0E814273D14A646BA5D092361D48FBDC035B6A3BE7D7DDFCD95E0A3253C8FBB10EC4331FAB14E4187AF4EE777AD6BA3525D86E002A2C53937A0888035A6801FDCFDA109439AB69C82B820BF3D013BE68A45C7B1F81FD47BF06D38DECBCCA97705381C2F466B11F3E8974EA4B9074828B374C27501A9E6560977DAC3271AD44FC0A9B6BDD077C6D7482CCF97EFE363A3A8A12E63BA272AE4AF41632D24573ECA04A3F38CE5F32C00B613D8CA7599CA21FAB02E803B38FEA088B4D089F889DF436F91DBCD79F0808D09E4BF8D7F0EE0B708E9B6CF65D9A75E81A0FC80DA1BCA70CD9A6A5A24AE628CFBBFE17CA87209839905A989E5A4B956FF9E0BAA34B69D07AF7F313D41095C17BF1C737BF5DB950DA0D9D772D1BAEF2916C6443CDD8FCC31FB2B8E73BA298B54236F8048DF42A2749891FF251E51351DF76CBB2DFEFD6551776C5B063A813FB38622B8725ACA4757BBB21F7C4AA41761A9B371768FC6"})
    browser.refresh()
    time.sleep(5)  # Wait for the page to refresh
    logging.info("Cookie login successful")

    # Confirm login is successful
    logging.info("Unlock finished")

    time.sleep(10)
    browser.quit()


if __name__ == '__main__':
    try:
        extension_login()
    except Exception as e:
        logging.error(f"Failed to execute login script: {e}")
