from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
url = "https://www.kuveytturk.com.tr/finans-portali"
driver.get(url)

time.sleep(3)

html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")

divs = soup.find_all("div", {"class": "finance-market-box"})

with open("kuveytguncelveri.txt", "w", encoding="utf-8") as file:
    for div in divs:
        title = div.find("div", {"class": "title"}).text.strip()
        buy_value = div.find("div", {"class": "value"}).text.strip()

        file.write(f"{title}, Alis: {buy_value}\n")
        print(f"{title}, Alis: {buy_value}")

driver.quit()