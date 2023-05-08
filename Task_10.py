from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

random = random.randint(10, 100000)
driver = webdriver.Chrome()
driver.get("https://rozetka.com.ua/")

driver.find_element(By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[2]').click()
#registerUserName
name = driver.find_element(By.CSS_SELECTOR, '#registerUserName')
name.send_keys('Светлана')
time.sleep(2)
#registerUserSurname
last_name = driver.find_element(By.CSS_SELECTOR, '#registerUserSurname')
last_name.send_keys('Тест')
time.sleep(2)
#registerUserPhone
number = driver.find_element(By.CSS_SELECTOR, '#registerUserPhone')
number.send_keys('0930000000')
#registerUserEmail
email = driver.find_element(By.CSS_SELECTOR, '#registerUserEmail')
email.send_keys('sveta12345@gmail.com')
#registerUserPassword
password = driver.find_element(By.CSS_SELECTOR, '#registerUserPassword')
password.send_keys('Sv123456')
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-register/div/form/fieldset/div[8]/button[1]').click()

time.sleep(2)
driver.quit()