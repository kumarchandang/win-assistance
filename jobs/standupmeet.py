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
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-plugins-discovery")
    # options.add_argument("--user-data-dir=C:\\Users\\ckgou\\AppData\\Local\\Google\\Chrome\\User Data")
    # options.add_argument("--profile-directory=Default")
    driver = webdriver.Chrome(service=s,chrome_options=options)

    driver.get(r'https://meet.google.com/landing?authuser=1')
    timeout = 20
    email = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, "identifier")))
    email.send_keys("kumarchandang801@gmail.com")
    password = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.NAME, "Kumar@801")))
    password.send_keys("pwd")
    login_button = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, "login")))
    login_button.click()