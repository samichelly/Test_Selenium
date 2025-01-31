import os
import time
import random
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


# Load .env
load_dotenv()

# Get IDs
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Options to simulate real user
chrome_options = Options()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--enable-javascript")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Run chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Use JS
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Reach website
driver.get("https://www.totalenergies.fr/clients/connexion")
action = ActionChains(driver)
time.sleep(random.uniform(3, 7))

title = driver.title
print(title)


# Username
action = ActionChains(driver)
time.sleep(random.uniform(3, 7))

text_box = driver.find_element(by=By.NAME, value="tx_demmauth_authentification[authentificationForm][login]")
time.sleep(random.uniform(3, 7))
action.move_to_element(text_box).click().perform()
time.sleep(random.uniform(1, 3))

text_box.send_keys(USERNAME)
time.sleep(random.uniform(0.5, 2))

# Password
action = ActionChains(driver)
time.sleep(random.uniform(3, 7))

password_ = driver.find_element(by=By.NAME, value="tx_demmauth_authentification[authentificationForm][password]")
time.sleep(random.uniform(3, 7))
action.move_to_element(password_).click().perform()
time.sleep(random.uniform(1, 3))

password_.send_keys(PASSWORD)
time.sleep(random.uniform(0.5, 2))


# Click to connect
time.sleep(random.uniform(1, 3))
login_button = driver.find_element(By.ID, "js--btn-validation")
login_button.click()

input("Waiting...")


driver.quit()
