#!/usr/bin/python3.8

from telegram.ext import *
import requests
import logging
import json
 
#updater
updater = Updater(token='', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
		level=logging.INFO)

#start function
def start(updater, context):
	context.bot.send_message(chat_id=updater.effective_chat.id, text='this is start')
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#covid function
def covid(updater, context):
	#covid api
	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
	querystring = {"country":"Iran"}
	headers = {
	    'x-rapidapi-key': "7a61b9e1e4mshbd28c587d1a254dp136a20jsn0007c28f0d43",
	    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
	    }
	response = requests.request("GET", url, headers=headers, params=querystring)
	jsn = json.loads(response.text)
	#jon = str(json.dumps(jsn, indent=8))
	recovered = str(jsn["data"]["recovered"])
	deaths = str(jsn["data"]["deaths"])
	confirmed = str(jsn["data"]["confirmed"])
	lastChecked = str(jsn["data"]["lastChecked"])
	lastReported = str(jsn["data"]["lastReported"])
	
	#print(json.dumps(jsn, indent=4))
	#print(response.text)
	#bot
	context.bot.send_message(chat_id=updater.effective_chat.id, text="recoverd: " + recovered +  "\ndeaths: " + deaths + "\ncofirmed: " + confirmed + "\nlastChecked: " + lastChecked + "\nlastReported: " + lastReported)
covid_handler = CommandHandler('covid', covid)
dispatcher.add_handler(covid_handler)

updater.start_polling()
