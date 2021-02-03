from twitter_user_info import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class twitter:
    def __init__(self,usename,password):
        self.browser_profile = webdriver.ChromeOptions() # özellik eklemek için
        self.browser_profile.add_experimental_option("prefs", {"intl.accept_languages":"en,en_us"}) #ingilizce dili özelligi ekledik
        self.browser = webdriver.Chrome("chromedriver.exe", chrome_options = self.browser_profile) # ekledigimiz özelligi chromedriver.exe ye ekledik
        self.browser.maximize_window()
        self.username = username
        self.password = password
    
    def sing_in(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        username_input = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
        password_input = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        
        button_submit = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
        button_submit.click()
        time.sleep(2)

    def search(self,hastage):
        
        search_input = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        search_input.send_keys(hastage)
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        time.sleep(2)
        
        list = self.browser.find_elements_by_tag_name("//div[@data-testid='tweet']/div[1]/div[1]div/div/span")
        for item in list:
            print(item.text)

twttr = twitter(username,password)
twttr.sing_in()
twttr.search("python")