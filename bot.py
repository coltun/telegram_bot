#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import requests
import schedule
import time
from scrape import get_max_min_coins
from tabletext import to_text

load_dotenv()
API_KEY = os.getenv('API_KEY')
CHAT_ID = os.getenv('CHAT_ID')
TIME_EXECUTION  = os.getenv('TIME_EXECUTION')


def bot_message():
	max_data, min_data = get_max_min_coins()
	min_data_text = to_text(min_data)
	max_data_text = to_text(max_data)

	message = "Top losers: \n" + min_data_text + "\n" + "Top gainers: \n" + max_data_text
	url = 'https://api.telegram.org/bot' + API_KEY + '/sendMessage?chat_id=' + CHAT_ID + '&text=' + message
	requests.get(url)

#bot_message()

schedule.every().day.at(TIME_EXECUTION).do(bot_message)

while True:
    schedule.run_pending()
    time.sleep(1)

