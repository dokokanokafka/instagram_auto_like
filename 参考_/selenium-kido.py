# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from time import sleep
# import chromedriver_binary

import urllib.parse
import time


# # ブラウザを開く。
# driver = webdriver.Chrome()
# # Googleの検索TOP画面を開く。
# driver.get("https://www.google.co.jp/")
# # 検索語として「京都プログラミング研究室」と入力し、Enterキーを押す。
# search = driver.find_element_by_name('q') 
# search.send_keys("京都プログラミング研究室")
# search.send_keys(Keys.ENTER)
# # タイトルに「京都プログラミング研究室」と一致するリンクをクリックする。
# driver.find_element_by_partial_link_text("京都プログラミング研究室").click()
# # 5秒間待機してみる。
# sleep(5)
# # ブラウザを終了する
# # driver.close()



# #Webdriver
# # browser = webdriver.Chrome()
# browser = webdriver.Chrome(executable_path='/Users/haruhikido/Desktop/chromedriver')

# #URL
# MAIN_URL = "https://www.instagram.com/"
# TAG_SEARCH_URL = MAIN_URL + "explore/tags/{}/?hl=ja"

# #selectors
# LOGIN_PATH = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
# LIKE_PATH = '//button[@class="wpO6b "]/*[name()="svg"][@aria-label="いいね！"]'
# LIKE_BUTTON_PATH = '//button[@class="wpO6b "]'

# MEDIA_SELECTOR = 'div._9AhH0' #表示されているメディアのwebelement
# NEXT_PAGE_SELECTOR = 'a.coreSpriteRightPaginationArrow' #次へボタン

# #USER INFO
# username = "jpn_kyoto_annaewon"
# password = "szdxfcgv8832"
# #params
# tagName = "[#해외여행]"
# likedCounter = 0
# likedMax = 100

# if __name__ == '__main__':

#     #login 
#     browser.get(MAIN_URL)
#     time.sleep(3)
#     browser.find_element_by_xpath(LOGIN_PATH).click()
#     time.sleep(3)
#     usernameField = browser.find_element_by_name('username')
#     usernameField.send_keys(username)
#     passwordField = browser.find_element_by_name('password')
#     passwordField.send_keys(password)
#     passwordField.send_keys(Keys.RETURN)

#     #tag search
#     time.sleep(3)
#     encodedTag = urllib.parse.quote(tagName) #普通にURLに日本語は入れられないので、エンコードする
#     encodedURL = TAG_SEARCH_URL.format(encodedTag)
#     print("encodedURL:{}".format(encodedURL))
#     browser.get(encodedURL)

#     #media click
#     time.sleep(3)
#     browser.implicitly_wait(10)
#     browser.find_element_by_css_selector(MEDIA_SELECTOR).click()

#     #次へボタンが表示されないか、いいねが一定数いくまで
#     while likedCounter < likedMax:
#         time.sleep(3)
#         try:
#             browser.find_element_by_xpath(LIKE_PATH)
#             browser.find_element_by_xpath(LIKE_BUTTON_PATH).click()
#             likedCounter += 1
#             print("liked {}".format(likedCounter))
#         except:
#             #読み込まれなかったり既にいいねしているならパス
#             print("pass")
#             pass

#         #次へ
#         try:
#             browser.find_element_by_css_selector(NEXT_PAGE_SELECTOR).click()
#         except:
#             break

#     print("You liked {} media".format(likedCounter))


# http://yoppyland.net/copypaste-python/

import urllib.parse
import time
import random
from time import sleep
import schedule


"""
instagramにアクセス
""" 

driver = webdriver.Chrome(executable_path='/Users/haruhikido/Desktop/chromedriver')
driver.get("https://www.instagram.com/accounts/login/")

#指定した時間だけ処理を遅延ランダムで
sleep(random.randint(1,3))

"""
ログイン
""" 

#ログインID入力
user = driver.find_element_by_class_name("_2hvTZ")
user.send_keys("dokokanokafkainsta")

#パスワード入力
password = driver.find_element_by_name('password')
password.send_keys("szdxfcgv8832")

##Enterキーを押下する
password.send_keys(Keys.ENTER)

#指定したドライバの要素が見つかるまでの待ち時間を設定する
driver.implicitly_wait(5)

#指定した時間だけ処理を遅延ランダムで
sleep(random.randint(1,3))


#ポップ画面の表示された場合　「後で」をクリックする
try:
  elem_search_word = driver.find_element_by_xpath("/html/body/div[*]/div/div/div[3]/button[2]")
  sleep(random.randint(1,3))
  elem_search_word = driver.find_element_by_xpath("/html/body/div[*]/div/div/div[3]/button[2]").click()
  driver.implicitly_wait(2)
  sleep(random.randint(1,3))

#検索タグのページに移動→初めの一枚目をクリック
except:
  pass 
driver.get("https://www.instagram.com/explore/tags/일본여행/")
driver.implicitly_wait(6)
driver.find_element_by_xpath("//article/div[1]/div[1]/div[1]/div[1]/div[1]/a").click()
# sleep(random.randint(1,3))


# """
# いいね
# """

def job():

    likecount = 0
    #いいね回数指定デフォルトでは、20回になってます
    while (likecount < 20):
       try:
           #いいね判定
        #    sleep(random.randint(1,3))
           driver.find_element_by_css_selector("[aria-label=「いいね！」を取り消す]")
        #    sleep(random.randint(1,3))
           #いいねされていたら次に
        #    print("いいね済み、パス")
           driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()
        #    sleep(random.randint(1,3))
       except:
           #いいねする
           driver.find_element_by_xpath("/html/body/div[*]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
           likecount += 1
        #    sleep(random.randint(1,3))
           print(likecount)
           print("いいね！")
           driver.find_element_by_css_selector("a.coreSpriteRightPaginationArrow").click()
        #    sleep(random.randint(1,3))
           pass

    print(likecount)
    print("いいねしました！")



def main():
    # 60分ごと
    schedule.every(60).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

main();

