# python3 -m pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("/Users/vasiliykirnos/skillfactory/python_selenium_sf/chromedriver")
driver.get("https://google.com")
driver.find_element(By.XPATH, "//input[@title=\"Поиск\"]").send_keys('Skillfactory' + Keys.RETURN)
sleep(2)
driver.save_screenshot('sf.png')
driver.quit()
