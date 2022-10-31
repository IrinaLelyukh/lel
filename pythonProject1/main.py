import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
s=Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
#Форма Паспорт от Лелюх
def write_field(name, value):
    driver.find_element(By.ID, name).send_keys(Keys.HOME)
    driver.find_element(By.ID, name).send_keys(value)
driver.get("https://qa.neapro.site/login")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("leluca_69@mail.ru")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(3)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '.form:nth-child(2) .document-tile:nth-child(1) > .document-name').click()
driver.find_element(By.ID, 'surname').send_keys('Петров')
driver.find_element(By.ID, 'name').send_keys('Пётр')
driver.find_element(By.ID, 'patronymic').send_keys('Петрович')
#driver.find_element(By.ID,'issued').click()
driver.find_element(By.ID,'code').clear()
driver.find_element(By.ID,'code').send_keys('777-777')
driver.find_element(By.ID,'issued').clear()
driver.find_element(By.ID,'issued').send_keys('УФМС РОССИИ Г КРАСНОЯРСКА')
time.sleep(1)
driver.find_element(By.ID,'cardId').clear()
driver.find_element(By.ID,'cardId').send_keys('777-777-777 77')
driver.find_element(By.XPATH, '//*[@id="birthday"]/div/input').send_keys('14.01.2000')
driver.find_element(By.XPATH, '//*[@id="dateOfIssue"]/div/input').send_keys('14.02.2014')
write_field('passportSeries', '1234')
write_field('passportNumber', '567890')
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.CONTROL+"a")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.DELETE)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Москва")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.DOWN)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.ENTER)
driver.find_element(By.ID,'phone').clear()
driver.find_element(By.ID,'phone').send_keys('(902)902-90 20')
time.sleep(1)
driver.find_element(By.ID, 'privacy').click()
time.sleep(4)
driver.find_element(By.ID, 'privacy').click()
filePath ='C:\\users\\lelyu\\Desktop\\1.jpeg'
driver.find_element(By.CSS_SELECTOR, '#__layout > div > div.content-wrapper > div > div > div.content-page > div > div > div.form.passport-form.document-form > div.body > div.upload-widget.upload-widget > input[type=file]').send_keys(filePath)
time.sleep(15)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(10)
#разлогин
"""driver.get("https://qa.neapro.site/cabinet/documents/")
driver.find_element(By.CSS_SELECTOR,"menu-header").click()
driver.find_element(By.CSS_SELECTOR,"logout").click()"""
