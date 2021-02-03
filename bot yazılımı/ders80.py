from selenium import webdriver
import time

driver = webdriver.Chrome()
url ="https://www.github.com"
driver.get(url) # sayfayı açar

time.sleep(1)
driver.maximize_window() # pencereyi tam ekran yapar
driver.save_screenshot("github.com - homepage.png") # sayfanın ekran görüntüsü alır

url_1 = "https://www.github.com/sadikturan"
driver.get(url_1)
print(driver.title) # sayfanın başlıgını yazar

if "sadikturan" in driver.title:
    driver.save_screenshot("github - sadikturan.png")

time.sleep(1)
driver.back() # bir önceki sayfaya döner
# driver.forward() bir sonraki sayfaya geçer
time.sleep(1)
driver.close() # tarayyıcıyı kapatır