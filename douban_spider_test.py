import requests
from bs4 import BeautifulSoup
import pandas

f = requests.get('https://book.douban.com/subject/1084336/comments/')
f.text
f.encoding='utf-8'

soup = BeautifulSoup(f.text,'lxml')
pattern = soup.find_all('p','comment-content')
for item in pattern:
    print(item.string)

comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
df.to_csv('comments.csv')
