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
    browser.add_cookie({"name": "MUSIC_U", "value": "00E37EAD61C158D8CD0A632BBFBBDC8402DDE5CCB032A5C4AEDB922E00EC6BA5847B448E093B56F3F91D473FE0A58EB0F2AFE66E1EDFB1754F9581C816C0B05317E851E6E9DECF25DBA3AE11AB78E341F4ACE4D4913533ED9B5D808E91254643713D4F5B7D344D79FB0D8344DFEA691E5A426C55CE702484BAEE5249C7B1F96086AA5C1B38400318CC76AB358176A0F78882E055771750EBDEF9CEE43608F0EC6FF76BE5FB0324EEDE3753B879E8061AEA2EDF9E15D44A6899EEBB1196EA4E41CE367F8BF1B88AA083BF887A0AFCA8BB28A0B4B0D3C65F2E082D524B358564B76445286BEBF51D2B2E3C9E2E4BC09100AB0FA2C5D0BAD29F8B96CDC23BFFBD877F929479AE351948FF002B5C7E5A0F2066B3D9C5D24ED3DBD0A1134C1D68DD6D54667AB7ED2DF00C0EC9ECB416FED2983F4BC99B69D2FB3354EA587BF4FA7857778B814AEED2C793EF42D7478AC27994CDD32C61915E689F4D076F3DE1E38214AC"})
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
