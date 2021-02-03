from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url ="http://github.com"
driver.maximize_window()
driver.get(url)
# search_input = driver.find_element_by_name("q")
search_input = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]")
time.sleep(1)
search_input.send_keys("html") # arama bölümüne html yazar
time.sleep(2)
search_input.send_keys(Keys.ENTER) # enter tuşuna basar
time.sleep(2)
# result = driver.page_source
# print(result)
result = driver.find_elements_by_css_selector(".repo-list-item a")
for element in result:
    print(element.text)
time.sleep(2)
driver.close()