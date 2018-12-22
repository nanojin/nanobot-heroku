import discord
from discord.ext import commands
import os
import json
import asyncio

# Authentication
TOKEN = 'MjY4OTQ3ODc3NTU0ODE0OTg2.Dv_vgQ.eqi8NTGOj5wtvlWcELATt4RLlqU'


# Configuration Setup
bot = commands.Bot(command_prefix = '.')
client = discord.Client()

@bot.event
async def on_ready():
	print('nanobot online.')

@bot.event
async def on_message(message):
	author = message.author
	body = message.content
	with open('messages.txt', 'a+') as f:
		log = author + body
		f.write(message.content)

bot.run(TOKEN)
