from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time
import os

driver = uc.Chrome()
url = "https://www.tripadvisor.com/Hotel_Review-g297977-d12282029-Reviews-Movenpick_Bursa_Hotel_and_Thermal_Spa-Bursa.html"
driver.get(url)
foldername = "MovenpickBursaHotelandTermalSpaBursa"

try:
    button = driver.find_element(By.CLASS_NAME, "UikNM _G B- _S _W _T c G_ wSSLS wnNQG")
    button.click()
    print("Başarıyla butona tıklandı")
except Exception as e:
    print(f"Hata oldu: {e}")

time.sleep(5)

def yorumaltadv():
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    divs = soup.find_all("div", {"data-automation": "tab"})

    dosya_yolu = f"/home/mrcaar/Documents/Data Mining/Tripadvisor/{foldername}.txt"
    with open(dosya_yolu, "a", encoding="utf-8") as file:
        for div in divs:
            try:
                # kullanici adini bul
                kullaniciad_div = div.find("div", {"class": "zpDvc Zb"})
                kullaniciad = kullaniciad_div.text.strip() if kullaniciad_div else "Kullanıcı Adı Bulunamadı"

                # gonderi tarihi
                tarih_div = div.find("div", {"class": "biGQs _P pZUbB ncFvv osNWb"})
                tarih = tarih_div.text.strip() if tarih_div else "Tarih Bulunamadı"

                # puani
                score_div = div.find("title", {"id": ":lithium-rb8:"})
                score = score_div.text.strip() if score_div else "Score Bulunamadı"

                # yorum basligi
                yorumbasligi_div = div.find("span", {"class": "yCeTE"})
                yorumbasligi = yorumbasligi_div.text.strip() if yorumbasligi_div else "Yorum Başlığı Bulunamadı"

                # yorum kismi
                yorum_div = div.find("span", {"class": "JguWG"})
                yorum = yorum_div.text.strip() if yorum_div else "Yorum Bulunamadı"

                # dosyaya yazma kısmı
                file.write(f"Kullanıcı Adı: {kullaniciad}\nTarih: {tarih}\nPuanı: {score}\nYorum Basligi: {yorumbasligi}\nYorum: {yorum}\n\n")
                print(f"Kullanıcı Adı: {kullaniciad}\nTarih: {tarih}\nPuanı: {score}\nYorum Basligi: {yorumbasligi}\nYorum: {yorum}\n\n")
            except Exception as e:
                print(f"Hata oluştu: {e}")

yorumaltadv()

while True:
    try:
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Next page']"))
        )
        button.click()
        print("Başarıyla Butona Tıklandı")
        time.sleep(2.5)
        yorumaltadv()
    except Exception as e:
        print(f"Hata oldu veya sayfa bitti: {e}")
        break

driver.quit()