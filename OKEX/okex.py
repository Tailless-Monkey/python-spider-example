import cfscrape,json

url="https://www.okex.com/v2/spot/markets/kline?size=300&symbol=eos_usdt&type=1min"
scraper = cfscrape.create_scraper()
cnt = scraper.get(url).content
jdata=json.loads(cnt)['data']
#jdata is the 300 data points
print len(jdata)
print jdata[0]

ddddddddddimport requests
from lxml import etree

url = ''
r = requests.get(url).text

s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/text()')

import pandas as pd
df = pd.DataFrame(file)
df.to_excel('pinglun.xlsx')