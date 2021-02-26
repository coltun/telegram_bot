
Description Telegram Crypto Bot:
Bot for which you can set the time to send daily top 25 crypto coins that increased and decreased in price the most in the last 24h from the first page of coinmarketcap website. 

Environment configuration: 
In .env file:
1. Set the Telegram API_KEY in API_KEY = ""
2. Provide the CHAT_ID(chat that you want to receive messages from the bot) in CHAT_ID = ""
3. Provide the time in EXECUTION_TIME = "hour:minutes" to set the daily time to receive the message from the bot. 

Running the script on MacOS with nohup:
1. "`chmod +x bot.py`" -> set the permissions of the file to allow execution
2. "`nohup ./bot.py &`" -> running the script in the background with nohup


