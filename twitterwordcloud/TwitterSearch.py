from selenium import webdriver
from urllib.parse import quote
from bs4 import BeautifulSoup
import time


class TwitterSearch:
    def __init__(self,search_word):
        #ChrmoeDriverサーバーのパスを引数に指定しChromeを起動
        self.driver = webdriver.Chrome('/Users/fenganling/Downloads/chromedriver')
        #指定したURLに遷移する
        self.driver.get("https://twitter.com/search?src=typd&q={}&lang=ja".format(quote(search_word)))
        time.sleep(1)

    def search_start(self,amount=0):
        time.sleep(1)
        #指定した回数だけスクロール
        for _ in range(0,amount):
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #トップに戻る

        #ソースコードを取得
        html = self.driver.page_source
        bsObj = BeautifulSoup(html,"lxml")
        
        return_tweets=[]
        for tweet in bsObj.find_all("p"):
            return_tweets.append(tweet.get_text())
            #print(tweet.get_text())
        return return_tweets
    
    def __del__(self):
        self.driver.close()