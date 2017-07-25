import requests
from bs4 import BeautifulSoup

url = 'http://photo.poco.cn/lastphoto-htx-id-5748659-p-0.xhtml#'

wb_data = requests.get(url)

soup = BeautifulSoup(wb_data.text,'lxml')
imgs = soup.select('div.img-item > div.img-box.photo')
print(imgs)