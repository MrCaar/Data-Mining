from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
url = "https://www.kizlarsoruyor.com/"
driver.get(url)

try:
    button = driver.find_element(By.ID,"scp_share_btn")
    button.click()
    print("Basariyla butona tiklandi")
except Exception as e:
    print("Hata oldu: {e}")

time.sleep(5)
driver.quit()