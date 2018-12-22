import dscord
from discord.ext import commands
import os
import json
import asyncio

# Configuration Setup
bot = commands.Bot(command_prefix = commands.when_mentioned_or('.'))
client = discord.Client()

@bot.event
async def on_ready():
	print('nanobot online.')

@bot.event
async def on_message(message):
	logname = (message.server.name + '[' + hash(message.server) + ']', 'DM_' + message.author, 'DM_' + message.author )[message.server != None]
	author = message.author
	body = message.content
	with open( logname + 'log.txt', 'a+') as f:
		log = author + body
		f.write(message.content)

bot.run(os.environ['NANOBOT_TOKEN'])
