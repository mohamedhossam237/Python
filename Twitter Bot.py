from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 

class TwitterBot:
    def __init__(self,username,Password):
        self.username =username
        self.Password =Password
        self.bot= webdriver.Chrome(ChromeDriverManager().install())
        
        
    def login (self):
        bot=self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email =bot.find_element_by_class_name('email-input')
        password =bot.find_element_by_name('session[pass]')
        email.clear()
        password.clear()
        email.send.keys(self.username)
        password.send_keys(self.Password)
        password.send_keys(self.RETURN)
        time.sleep(3)

    def like_tweet(self,hashtag):
        bot =self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
          bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
          time.sleep(2)
          tweets = bot.find_elements_by_class_name('tweet')
          links =[elem.get_attribute('data-peralink-path')
                  for elem in tweets]
          for link in links:
              bot.get('https://twitter.com'+link)
              try:
                  bot.find_element_by_class_name('HeartAnimation').click()
                  time.sleep(10)
              except Exception as ex:
                  time.sleep(60)
          
          
ed=TwitterBot('story@yahoo.com','Duha259')
ed.login()
ed.like_tweet('webdevelopment')