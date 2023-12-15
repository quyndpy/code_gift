from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Mapotic_Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def load_mapotic(self, code):
            self.driver.get('https://khuyenmaiyogurt.thmilk.vn/')
            time.sleep(2)
            name_id = self.driver.find_element(By.XPATH, '//*[@id="main-name"]')
            name_id.send_keys("Dogo")
            phone_id = self.driver.find_element(By.XPATH, '//*[@id="main-phone"]')
            phone_id.send_keys("0986642301")
            code_id = self.driver.find_element(By.XPATH, '//*[@id="main-code"]')
            code_id.send_keys(code)
            dropdown = self.driver.find_element(By.XPATH, '//*[@id="main-province"]')
            select = Select(dropdown)
            select.select_by_value('01')
            checkmark = self.driver.find_element(By.CLASS_NAME, 'checkmark')
            checkmark.click()
            submit = self.driver.find_element(By.CLASS_NAME, 'submit-btn')
            submit.click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//*[@id="confirm-btn"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, '/html/body/div/div[6]/div/div/div/div[1]/div[3]/a').click()
    def remove_code_from_file(self, code):
        with open('chuoi3.txt', 'r') as file:
            lines = file.readlines()
        with open('chuoi3.txt', 'w') as file:
            for line in lines:
                if line.strip() != code:
                    file.write(line)


bot = Mapotic_Bot()
with open('chuoi3.txt', 'r') as file:
    codes = file.readlines()

for code in codes:
    code = code.strip()
    bot.load_mapotic("T23" + code)
    bot.remove_code_from_file(code)

