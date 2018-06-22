import cfscrape,json

url="https://www.okex.com/v2/spot/markets/kline?size=300&symbol=eos_usdt&type=1min"
scraper = cfscrape.create_scraper()
cnt = scraper.get(url).content
jdata=json.loads(cnt)['data']
#jdata is the 300 data points
print (len(jdata))
print (jdata[0])