import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--start-maximized")  # Maximiser la fenêtre
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Contourner la détection
chrome_options.add_argument("--enable-javascript")  # Assurer que JS est activé
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("prefs", {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "plugins.always_open_pdf_externally": True
})

# 🔹 Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Use JS
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


driver.get("http://latetedanslesmots.free.fr/")
action = ActionChains(driver)
time.sleep(5)

# input("Loading page")
search_box = driver.find_element(By.NAME, "Mot")
search_box.send_keys("Poisson")
time.sleep(5)

search_button = driver.find_element(By.NAME, "Rechercher")
search_button.click()
time.sleep(5)

story_link = driver.find_element(By.XPATH, "//ul[@class='listetitre']/li/a")
print(story_link.get_attribute("href")) 

print(story_link)
story_link.click()

pdf_link = driver.find_element(By.XPATH, "//a[contains(@href, '.pdf')]")
pdf_url = pdf_link.get_attribute("href")
time.sleep(10)
driver.get(pdf_url)
time.sleep(10)

input("Waiting...")
driver.quit()
