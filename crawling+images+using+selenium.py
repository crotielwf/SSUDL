#working directory 설정
import os

os.getcwd()
animal = ['dog','cat','cow','pig','rabbit']
os.chdir('C:\\Users\\Kim\\animal')
wd = 'C:\\Users\\Kim\\animal'

def changedir(aniname):
    if aniname == 'dog' : os.chdir(wd+'\\'+animal[0])
    elif aniname == 'cat' : os.chdir(wd+'\\'+animal[1])
    elif aniname == 'cow' : os.chdir(wd+'\\'+animal[2])
    elif aniname == 'pig' : os.chdir(wd+'\\'+animal[3])
    else : os.chdir(wd+'\\'+animal[4])

os.getcwd()



# 사이트 url 따기
import urllib.request
import codecs
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver= webdriver.Chrome('c:/Users/Kim/chrome/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(4)


## 여기 아래에다가 url주소 입력


#dog : 
#  https://www.google.co.kr/search?biw=767&bih=740&tbm=isch&sa=1&ei=i9RaW5SqMcTm-Abs-J6oDQ&q=강아지&oq=강아지&gs_l=img.3..35i39k1j0l9.54205.55215.0.55338.7.6.0.0.0.0.266.488.0j2j1.3.0....0...1c.1j4.64.img..4.3.487....0.9X1eZ1roBvA
#cat : 
#  https://www.google.co.kr/search?biw=767&bih=740&tbm=isch&sa=1&ei=TdRaW67REtbr-Qbky4zQDg&q=%EA%B3%A0%EC%96%91%EC%9D%B4&oq=%EA%B3%A0%EC%96%91%EC%9D%B4&gs_l=img.3...31789.33691.0.33834.13.10.2.0.0.0.184.748.0j6.6.0....0...1c.1j4.64.img..8.5.452.0..0.0.eNb2zIUfXxU
#cow :
#  https://www.google.co.kr/search?biw=767&bih=740&tbm=isch&sa=1&ei=b9RaW9bKOMODoATHrZuAAg&q=%EC%86%8C&oq=%EC%86%8C&gs_l=img.3..35i39k1j0l9.5934.6545.0.6667.2.2.0.0.0.0.117.224.0j2.2.0....0...1c.1j4.64.img..0.2.223....0.P8iqIKOaeBk
#pig : 
#  https://www.google.co.kr/search?biw=767&bih=740&tbm=isch&sa=1&ei=eNRaW-evDs3chwOGyJfoCQ&q=%EB%8F%BC%EC%A7%80&oq=%EB%8F%BC%EC%A7%80&gs_l=img.3..0l10.9591.10536.0.10628.5.5.0.0.0.0.129.236.0j2.2.0....0...1c.1j4.64.img..4.1.127....0.3CXQ-goDX3E
#rabbit : 
#  https://www.google.co.kr/search?biw=767&bih=740&tbm=isch&sa=1&ei=g9RaW7C6I8LchwOTp7OABg&q=%ED%86%A0%EB%81%BC&oq=%ED%86%A0%EB%81%BC&gs_l=img.3..35i39k1j0l9.5651.7048.0.7275.7.6.0.0.0.0.189.696.2j4.6.0....0...1c.1j4.64.img..1.6.695....0.rPWXKIl27fw

changedir('rabbit')

driver.get('https://www.google.co.kr/search?biw=767&bih=740&tbm=isch&sa=1&ei=g9RaW7C6I8LchwOTp7OABg&q=%ED%86%A0%EB%81%BC&oq=%ED%86%A0%EB%81%BC&gs_l=img.3..35i39k1j0l9.5651.7048.0.7275.7.6.0.0.0.0.189.696.2j4.6.0....0...1c.1j4.64.img..1.6.695....0.rPWXKIl27fw')

time.sleep(20) # 20초 기다리기
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
#soup = BeautifulSoup(html, 'html.parser')
url2 = soup.find_all("img")
#url2 = soup.select('a.item_slider.product_link > img')

url = []

for m in url2:
    url.append(m.get('src'))
    
#그림저장
    
for i in range(2,len(url)):   
    name = str(i) + '.jpg'
    urllib.request.urlretrieve(url[i],name)
    print(i)
    if i == 100: break
