import os
import dotenv
import requests
import json

dotenv.load_dotenv()
COINMARKETCAP_URL_API = os.getenv('COINMARKETCAP_URL_API')

def get_max_min_coins(amount=20):
	r = requests.get(COINMARKETCAP_URL_API)
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





	



