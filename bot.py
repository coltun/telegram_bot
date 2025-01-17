#!/usr/bin/env python3

import os
import requests
import schedule
import time
import scrape
import dotenv
import tabletext

dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')
EXECUTION_TIME = os.getenv('EXECUTION_TIME')

def bot_message():
	max_data, min_data = scrape.get_max_min_coins()
	min_data_text = tabletext.to_text(min_data)
	max_data_text = tabletext.to_text(max_data)

	message = "Top losers: \n" + min_data_text + "\n" + "Top gainers: \n" + max_data_text
	url = 'https://api.telegram.org/bot' + API_KEY + '/sendMessage?chat_id=' + CHAT_ID + '&text=' + message
	requests.get(url)

schedule.every().day.at(EXECUTION_TIME).do(bot_message)
bot_message()
while True:
    schedule.run_pending()
    time.sleep(1)

