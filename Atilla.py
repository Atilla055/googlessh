from selenium import webdriver
from selenium.webdriver.common.by import By

# Firefox profilinizin dizin yolunu ve profil adını belirtin
profile_path = "/root/.mozilla/firefox/dlr2maa5.default-release"

# Firefox profilini oluşturun
firefox_profile = webdriver.FirefoxProfile(profile_path)

# WebDriver'ı başlatırken profilinizi kullanın
options = webdriver.FirefoxOptions()
options.profile = firefox_profile
driver = webdriver.Firefox(options=options)

# İlk sayfaya gidin
driver.get("https://addons.mozilla.org/en-US/firefox/addon/webgl-fingerprint-defender/")

# Sayfanın yüklenmesini beklemek için gerekli bir bekleme süresi ekleyin
driver.implicitly_wait(10)  # Örnekte 10 saniye bekleme süresi kullanıldı, gerektiği gibi ayarlayabilirsiniz.

# "Add to Firefox" düğmesine tıklayın
add_to_firefox_button = driver.find_element(By.ID, "addon-add-button")
add_to_firefox_button.click()

# Sayfanın yüklenmesini beklemek için gerekli bir bekleme süresi ekleyin
driver.implicitly_wait(10)  # Örnekte 10 saniye bekleme süresi kullanıldı, gerektiği gibi ayarlayabilirsiniz.

# WebDriver'ı kapatın
