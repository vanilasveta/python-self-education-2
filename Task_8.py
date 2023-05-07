import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер и переходим на страницу
driver_path = r'C:\Program Files\Google\Chrome\Application'  # пропишите путь к драйверу
from selenium.webdriver.chrome.service import Service

driver_path = r'C:\Python\chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://www.random.org/dice/')

time.sleep(2)

button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Roll Dice"]')))
button.click()
time.sleep(2)

print('Кнопка нажата')

time.sleep(3)
driver.quit()