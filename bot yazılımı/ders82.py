from user_info import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def sign_in(self):
        self.browser.get("https://github.com/login")
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").click() # butona basar
    
    def load_followers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray").text)

    def get_followers(self):
        self.browser.get("https://github.com/sadikturan?tab=followers")
        time.sleep(2)
        self.load_followers()
        while True:
            links = self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")
            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.load_followers()
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        self.load_followers()
                    else:
                        continue

github = Github(username, password)
github.sign_in()
github.get_followers()
print(len(github.followers))
print(github.followers)
# for followers in github.followers:
#     print(followers)