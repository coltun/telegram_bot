import requests
import json
from tabletext import to_text

url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all"

def get_max_min_coins(amount=20):
	r = requests.get(url)
	data = (r.json())
	coins = data['data']['cryptoCurrencyList']

	symbol_list_positive = []
	symbol_list_negative = []

	for coin in coins:
		if coin['quotes'][0]['percentChange24h'] < 0:
			symbol_list_negative.append([coin['symbol'], coin['quotes'][0]['percentChange24h']])
		else:
			symbol_list_positive.append([coin['symbol'], coin['quotes'][0]['percentChange24h']])
			
	symbol_list_positive = sorted(symbol_list_positive, key=lambda x:(-x[1],x[0]))
	symbol_list_negative = sorted(symbol_list_negative, key=lambda x:(-x[1],x[0]), reverse=True)

	symbol_list_positive.insert(0, ['Coin Symbol', "Percentage Increase 24h"])
	symbol_list_negative.insert(0, ['Coin Symbol', "Percentage Decrease 24h"])
	return symbol_list_positive[:amount], symbol_list_negative[:amount]





	



