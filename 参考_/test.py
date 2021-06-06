"""
*
*
*
*
*seleniumの使い方は自分で勉強してください。
*macOS Python3.5で動作確認済みです。
*
*
*
*
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


driver = webdriver.Chrome(executable_path='/Users/haruhikido/Desktop/chromedriver')
driver.get("https://www.instagram.com/accounts/login/")

"""
*
*
*
*
*インスタグラムのログイン窓のHTMLの構造を調べて、
*ログイン窓のユーザーネームとパスワードのHTMLを取得して
*ユーザーidをパスワードを入力してログインします。
*
*
"""
#ログインID入力
user = driver.find_element_by_class_name("_2hvTZ")
user.send_keys("jpn_kyoto_annaewon")

#パスワード入力
password = driver.find_element_by_name('password')
password.send_keys("szdxfcgv8832")

##Enterキーを押下する
password.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
driver.find_element_by_css_selector(".aOOlW.HoLwm").click()

"""
*
*
*
*
*ログインすると、新しい要素が出現するまで若干待ちます。
*
*
*
*
"""

"""
*
*
*
*最新の投稿にループを回してイイねします。
*すでにイイねしてた場合は、except Exception as e:でエラー処理に回して、
*イイねしてない記事までループを続行します。
*
*
*
"""
count = 0
while (count < 9):
  try:
    print ('The count is:', count)
    myDynamicElement = driver.find_element_by_class_name("glyphsSpriteHeart__outline__24__grey_9")
    myDynamicElement.click()
    count = count + 1
  except Exception as e:
   print("You alredy LIKES " + str(e))

print ("Done!")