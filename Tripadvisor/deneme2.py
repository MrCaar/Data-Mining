from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Tarayıcıyı başlat
driver = webdriver.Chrome()
driver.get("https://www.tripadvisor.com/Hotel_Review-g293974-d294663-Reviews-Four_Seasons_Hotel_Istanbul_At_Sultanahmet-Istanbul.html")  # Yerine hedef URL'yi koyun

# Çerezleri kabul et
try:
    # Çerez kabul butonunu bul ve tıkla
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Kabul Et")]'))  # XPath'i kontrol edin
    )
    cookie_button.click()
    print("Çerezler kabul edildi.")
except Exception as e:
    print("Çerez kabul butonu bulunamadı:", e)

# Sayfaların kaçına kadar yorum çekmek istiyorsunuz?
max_pages = 3
current_page = 1

all_reviews = []

while current_page <= max_pages:
    try:
        # Yorumların tamamen yüklenmesi için sayfayı aşağı kaydır
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(15)

        # Yorumları çek
        reviews = driver.find_elements(By.CSS_SELECTOR, 'span.orRIx.Ci._a.C')
        for review in reviews:
            all_reviews.append(review.text)

        # Sonraki sayfa butonuna tıkla
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "next")]'))  # XPath'i kontrol edin
        )
        next_button.click()

        # Sayfanın yüklenmesi için bekle
        time.sleep(15)
        current_page += 1

    except Exception as e:
        print(f"Hata: {e}")
        break

# Yorumları yazdır veya kaydet
for index, review in enumerate(all_reviews, start=1):
    print(f"{index}. Yorum: {review}")

# Tarayıcıyı kapat
driver.quit()