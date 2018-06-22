import requests
f = requests.get('http://www.baidu.com/')
print(f)
f.text
f.encoding='utf-8'
print(f.text)