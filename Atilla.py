from selenium import webdriver

# Firefox profilinizin dizin yolunu ve profil adını belirtin
profile_path = "/root/.mozilla/firefox/dlr2maa5.default-release"

# Firefox profilini oluşturun
firefox_profile = webdriver.FirefoxProfile(profile_path)

# WebDriver'ı başlatırken profilinizi kullanın
options = webdriver.FirefoxOptions()
options.profile = firefox_profile

# İlk sayfa için yeni bir WebDriver oluşturun
driver1 = webdriver.Firefox(options=options)

# İlk sayfaya gidin
driver1.get("https://addons.mozilla.org/en-US/firefox/addon/webgl-fingerprint-defender/")

# Sayfanın yüklenmesini beklemek için gerekli bir bekleme süresi ekleyin
driver1.implicitly_wait(10)

# İkinci sayfa için yeni bir WebDriver oluşturun
driver2 = webdriver.Firefox(options=options)

# İkinci sayfaya gidin
driver2.get("https://addons.mozilla.org/en-US/firefox/addon/canvas-fingerprint-defender/")

# Sayfanın yüklenmesini beklemek için gerekli bir bekleme süresi ekleyin
driver2.implicitly_wait(10)

# WebDriver'ları kapatı
