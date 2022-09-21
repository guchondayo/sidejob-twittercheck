# coding:utf-8
# 修正 8:52

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# webdriverのバージョン管理 webdriverマネージャー及びByのインストール　1
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


import time
import requests
import chromedriver_binary       
from selenium.webdriver.common.keys import Keys as keys
import random

id="session08"
password="session09"
search_keys=["一つ目","二つ目","検索ワード三つ目","・・・"] #検索ワードを入力してください


options = webdriver.ChromeOptions()
# options.add_argument('--headless')    # ヘッドレスモードに
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("-window-size=1920,1080")
options.add_argument('--lang=ja-JP')
options.add_argument("--start-maximized")
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)'

options.add_argument('--user-agent=' + UA)
#driver = webdriver.Chrome('chromedriver')

# webdriverマネージャーのインストール
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()

url = "https://twitter.com/i/flow/login"

#id入力
driver.get(url)
# a = driver.find_elements_by_name("text")
a = driver.find_elements(By.NAME,"text")
a[0].send_keys(id)
a[0].send_keys(keys.ENTER)

#password入力
# a = driver.find_elements_by_name("password")
a = driver.find_elements(By.NAME,"password")
a[0].send_keys(password)
a[0].send_keys(keys.ENTER)
time.sleep(5)

# PATH
search_PATH = "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]"
texBox_PATH = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input"
latest_tag_PATH = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a"

#検索ボタンクリック
# a = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]")

a = driver.find_element(By.XPATH,search_PATH)


a.click()

time.sleep(4)

for j in range(len(search_keys)):
    if j!=0:
        driver.get("https://twitter.com/explore")


    search_key=search_keys[j]
    print(search_key)
    print(driver.current_url)

    #search_keyで検索
    # a = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
    a = driver.find_element(By.XPATH,texBox_PATH)  
    
    
    # if len(a)==0:
    #     a = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
    a.clear()
    time.sleep(2)
    a.send_keys(search_key)
    a.send_keys(keys.ENTER)

    time.sleep(4)

    #最新ツイートボタン押す
    # a = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a")
    a = driver.find_element(By.XPATH,latest_tag_PATH)
    a.click()

    time.sleep(4)




    count=0

    while True:
        #ツイートを取得
        # a = driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div")
        a = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div")
        if len(a)==0:
            print("ツイートなし")
            break

        for i in range(1,len(a)+1):
            x_path = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/section/div/div/div["+str(i)+"]/div/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div"
            # detail_button = driver.find_elements_by_xpath(x_path)
            detail_button = driver.find_elements(By.XPATH,x_path)
            if len(detail_button)==0:
                continue
            driver.execute_script("arguments[0].click();",detail_button[0])
            time.sleep(1)

            block_button = driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div")
            if len(block_button)==3:#ブロックしている時
                continue
            elif len(block_button)==5:
                print(block_button[2])
                block_button[2].click()
            else:
                continue
            time.sleep(1)

            block = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]")
            block.click()
            count=count+1
            print(str(count)+"回ブロックしました")
            time.sleep(1)
        
        # search_input = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        search_input = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
        search_input.send_keys(keys.ENTER)


