from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def send_weeklymail():
    s=Service(ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")
    # options.add_argument("--user-data-dir=C:\\Users\\ckgou\\AppData\\Local\\Google\\Chrome\\User Data")
    # options.add_argument("--profile-directory=Default")
    driver = webdriver.Chrome(service=s,chrome_options=options)

    driver.get('https://mail.storeapps.org:2096/cpsess5803118817/3rdparty/roundcube/')

    current_url = driver.current_url

    driver.find_element(By.NAME, 'user').send_keys('chandan.gouda@storeapps.org')
    driver.find_element(By.NAME, 'pass').send_keys('CHA2021@6%ST12&MA')
    driver.find_element(By.NAME, 'pass').submit()

    WebDriverWait(driver, 15).until(EC.url_changes(current_url))
    current_url = driver.current_url

    # Switch to the new window and open the email template
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(current_url + ".Sent&_uid=57&_action=show")
    driver.find_element(By.XPATH, '//*[@id="messagemenulink"]').click()
    driver.find_element(By.XPATH, '//*[@id="rcmbtn125"]').click()