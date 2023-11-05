from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Firefox profilinizin dizin yolunu ve profil ad1n1 belirtin
profile_path = "/root/.mozilla/firefox/dlr2maa5.default-release"

# Firefox profilini olu_turun
firefox_profile = webdriver.FirefoxProfile(profile_path)

# WebDriver'1 ba_lat1rken profilinizi kullan1n
options = webdriver.FirefoxOptions()
options.profile = firefox_profile

# 0lk ve ikinci Firefox taray1c1y1 aç1n
driver1 = webdriver.Firefox(options=options)
driver2 = webdriver.Firefox(options=options)
driver3 = webdriver.Firefox(options=options)
driver4 = webdriver.Firefox(options=options)
driver5 = webdriver.Firefox(options=options)

# YouTube kanal1na gidin ve sayfan1n yüklenmesini bekleyin (Her iki taray1c1 için)
driver1.get("https://www.youtube.com/@mahperest/videos")
driver3.get("https://www.youtube.com/@mahperest/videos")
driver4.get("https://www.youtube.com/@mahperest/videos")
driver5.get("https://www.youtube.com/@mahperest/videos")

# Bekleme süresi
wait_time = 20

# Sayfan1n yüklenmesini bekleyin
time.sleep(wait_time)

# Ayn1 liste üzerinden belirli bir videoyu bulup aç1n ve sonra 0 endeksini silin (her iki taray1c1 için)
video_elements = driver1.find_elements(By.XPATH, "//a[contains(@title, 'WOW')]")
if len(video_elements) > 0:
    video_elements[0].click()
    time.sleep(wait_time)

driver2.get("https://www.youtube.com/@mahperest/videos")
time.sleep(wait_time)
video_elements = driver2.find_elements(By.XPATH, "//a[contains(@title, 'WOW')]")
if len(video_elements) > 0:
    video_elements[1].click()
    time.sleep(wait_time)

driver3.get("https://www.youtube.com/@mahperest/videos")
time.sleep(wait_time)
video_elements = driver3.find_elements(By.XPATH, "//a[contains(@title, 'WOW')]")
if len(video_elements) > 0:
    video_elements[2].click()
    time.sleep(wait_time)

driver4.get("https://www.youtube.com/@mahperest/videos")
time.sleep(wait_time)
video_elements = driver4.find_elements(By.XPATH, "//a[contains(@title, 'WOW')]")
if len(video_elements) > 0:
    video_elements[3].click()
    time.sleep(wait_time)

driver5.get("https://www.youtube.com/@mahperest/videos")
time.sleep(wait_time)
video_elements = driver5.find_elements(By.XPATH, "//a[contains(@title, 'WOW')]")
if len(video_elements) > 0:
    video_elements[4].click()
    time.sleep(wait_time)

# Daha fazla i_lem yapmak için gerektii gibi kodu geni_letebilirsiniz

