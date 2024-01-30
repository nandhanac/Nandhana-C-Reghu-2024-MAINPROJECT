from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        budora=driver.find_element(By.CSS_SELECTOR,'.px-lg-3')
        budora.click()
        time.sleep(2)
        budora=driver.find_element(By.CSS_SELECTOR,'#cust')
        budora.click()
        time.sleep(2)
        budora=driver.find_element(By.CSS_SELECTOR,'#id_username')
        budora.send_keys("user@13")
        time.sleep(2)
        budora=driver.find_element(By.CSS_SELECTOR,'#id_password')
        budora.send_keys("Nandhana@25")
        time.sleep(2)
        budora=driver.find_element(By.CSS_SELECTOR,'.btn-primary')
        budora.click()
        time.sleep(2)
      