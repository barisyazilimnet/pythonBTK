from instagram_user_info import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instagram:
    def __init__(self, username, password):
        # self.browser_profile = webdriver.ChromeOptions() # özellik eklemek için
        # self.browser_profile.add_experimental_option("prefs", {"intl.accept_languages":"en,en_us"}) #ingilizce dili özelligi ekledik
        self.browser = webdriver.Chrome() #("chromedriver.exe", chrome_options = self.browser_profile) # ekledigimiz özelligi chromedriver.exe ye ekledik
        self.username = username
        self.password = password

    def sing_in(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username_input = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        password_input = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)
    #{self.username}
    def get_followers(self):
        self.browser.get(f"https://www.instagram.com/deryabay87")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followers_count = len(dialog.find_elements_by_css_selector("li"))
        print(f"First count :{followers_count}")

        action = webdriver.ActionChains(self.browser) # tuş kombinasyonları için 

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_down(Keys.SPACE).perform()
            time.sleep(2)

            new_count = len(dialog.find_elements_by_css_selector("li"))     

            if followers_count != new_count:
                followers_count = new_count
                print(f"Updated count :{new_count}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")
        
        followers_list = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followers_list.append(link)
        
        with open("followers.txt", "w", encoding="UTF-8") as file:
            for item in followers_list:
                file.write(item + "\n")

    def follow_user(self,username):
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)

        follow_button = self.browser.find_element_by_tag_name("button")
        # print(follow_button.text)
        buttons = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]").find_elements_by_tag_name("button")
        # print(len(buttons))
        if len(buttons) == 2:
            follow_button.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")

    def unfollow_user(self,username):
        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)

        unfollow_button = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/div/span/span[1]/button")
        buttons = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]").find_elements_by_tag_name("button")
        if len(buttons) == 2:
            unfollow_button.click()
            time.sleep(2)
            self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]").click()
        else:
            print("Zaten takip etmiyorsunuz")


instgrm = instagram(username, password)
instgrm.sing_in()
instgrm.get_followers()
# instgrm.follow_user("deryabay87")
# instgrm.unfollow_user("deryabay87")

# list =["deryabay87","alitpc3221"]
# for user in list:
#     instgrm.follow_user(user)
#     time.sleep(3)