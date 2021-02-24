#!/usr/bin/env python3

import requests
import schedule
import time
from scrape import get_max_min_coins
from tabletext import to_text

API_KEY ="1668423663:AAG1A0HuGSZ1tv1AvLRus3ZDnHyFXCzSNdA"
chat_id = '667939696'



def bot_message():
	max_data, min_data = get_max_min_coins()
	min_data_text = to_text(min_data)
	max_data_text = to_text(max_data)

	message = "Top losers: \n" + min_data_text + "\n" + "Top gainers: \n" + max_data_text
	
	pre_url = 'https://api.telegram.org/bot1668423663:AAG1A0HuGSZ1tv1AvLRus3ZDnHyFXCzSNdA/sendMessage?chat_id=667939696&text='
	url = pre_url + message
	requests.get(url)

# bot_message()

schedule.every().day.at("19:49").do(bot_message)

while True:
    schedule.run_pending()
    time.sleep(1)

