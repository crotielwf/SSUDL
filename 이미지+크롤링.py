
import os
os.chdir('C:/Users/Kim/animal/cow')
print(os.getcwd())


import urllib.request
import codecs
import csv
import requests
from bs4 import BeautifulSoup

# 사이트 url 따기
url ='https://www.google.com/search?biw=746&bih=740&tbm=isch&sa=1&ei=FNpXW9rOHIyM8wXdz6-ABw&q=%EC%86%8C&oq=%EC%86%8C&gs_l=img.3..0l10.2193.2896.0.3105.2.2.0.0.0.0.119.222.0j2.2.0....0...1c.4.64.img..0.2.221....0.TH7G6RlM8Rk'

# image url 따기
image_url =[]

# 사이트 파싱
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
url2= soup.select('img')
#url2 = soup.select('a.item_slider.product_link > img')

#for m in url2:
#    url.append(m.get('src'))
#ZN2TfZlM_AaT6M\3a
#html
#//*[@id="5JBMQ2DwDzPGEM:"]
# image url만 긁어서 리스트에 넣기
for m in url2:
    image_url.append(m.get('src'))

# 리스트에 들어가있는 image url로 사진 다운로드
for i in range(1,len(image_url)):   
    name = str(i) + '.jpg'
    urllib.request.urlretrieve(image_url[i],name)       
    print(i)

