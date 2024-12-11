from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os

driver = webdriver.Chrome()
url = "https://www.booking.com/hotel/it/agriturismo-podere-coldifico.html?label=gog235jc-1DCAEoggI46AdIM1gDaOQBiAEBmAExuAEZyAEM2AED6AEB-AECiAIBqAIDuALUjdu6BsACAdICJDRjZmVlNDFhLWNhMGEtNDhkNi1hNDY2LTE3YzY2ZmNjZjk2ZtgCBOACAQ&aid=397594&ucfs=1&arphpl=1&dest_id=104&dest_type=country&group_adults=1&req_adults=1&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=ccce4a00244b002b&srepoch=1733740336&from_sustainable_property_sr=1&from=searchresults"
driver.get(url)
foldername = "AgriturismoPodereColdifico"

# Sayfa başlatıldıktan sonra 'Reviews' sekmesine tıklayın
try:
    button = driver.find_element(By.ID, "reviews-tab-trigger")
    button.click()
    print("Başarıyla butona tıklandı")
except Exception as e:
    print(f"Hata oldu: {e}")

time.sleep(5)

# Yorumları çekmeye başla
# Yorumları çekme fonksiyonu
def get_reviews():
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    divs = soup.find_all("div", {"data-testid": "review-card"})  # Yorumları kapsayan div'ler

    dosya_yolu = f"/home/mrcaar/Documents/Data Mining/Booking/{foldername}.txt"
    with open(dosya_yolu, "a", encoding="utf-8") as file:
        for div in divs:
            try:
                # Kullanıcı adını bul
                kullaniciad_div = div.find("div", {"data-testid": "review-avatar"})  # Kullanıcı avatar kısmı
                kullaniciad = kullaniciad_div.text.strip() if kullaniciad_div else "Kullanıcı adı bulunamadı"

                # Tarihi bul
                tarih_div = div.find("span", {"data-testid": "review-date"})  # Tarihi kapsayan div
                tarih = tarih_div.text.strip() if tarih_div else "Tarih bulunamadı"

                # Score bul
                score_div = div.find("div", {"data-testid": "review-score"}) #Score bulunan yer
                score = score_div.text.strip() if score_div else "Score bulunamadı"

                # Yorum basligi kısmını bul
                yorumbasligi_div = div.find("h3", {"data-testid": "review-title"})  # Yorum başlığı
                yorumbasligi = yorumbasligi_div.text.strip() if yorumbasligi_div else "Yorum basligi bulunamadı"

                # Yorum (olumlu) kısmını bul
                yorumpositive_div = div.find("div", {"data-testid": "review-positive-text"}) # Yorum (olumlu) kısmı
                yorumpositive = yorumpositive_div.text.strip() if yorumpositive_div else "Olumlu Yorum Bulunamadı"

                # Yorum (olumsuz) kısmını bul
                yorumnegative_div = div.find("div", {"data-testid": "review-negative-text"}) # Yorum (olumsuz) kısmı
                yorumnegative = yorumnegative_div.text.strip() if yorumnegative_div else "Olumsuz Yorum Bulunamadı"

                # Verileri dosyaya yaz
                file.write(f"Kullanıcı Adı: {kullaniciad}\nTarih: {tarih}\nScore: {score}\nYorum Basligi: {yorumbasligi}\nOlumlu Yorum: {yorumpositive}\nOlumsuz Yorum: {yorumnegative}\n\n")
                print(f"Kullanıcı Adı: {kullaniciad}\nTarih: {tarih}\nScore: {score}\nYorum Basligi: {yorumbasligi}\nOlumlu Yorum: {yorumpositive}\nOlumsuz Yorum: {yorumnegative}\n\n")
            except Exception as e:
                print(f"Hata oluştu: {e}")

# İlk sayfayı çek
get_reviews()

# Sayfa geçişini gerçekleştirmek için
while True:
    try:
        # WebDriverWait ile 'Next page' butonunun tıklanabilir olmasını bekle
        button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Next page']"))
        )
        button.click()
        print("Başarıyla butona tıklandı")
        time.sleep(2.5)  # Sayfa geçişini bekleyin
        get_reviews()  # Yeni sayfadan yorumları çekin
    except Exception as e:
        print(f"Hata oldu veya sayfa bitti: {e}")
        break  # Eğer geçiş butonu yoksa veya başka bir hata varsa döngüyü kır

driver.quit()
