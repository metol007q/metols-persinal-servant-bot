#Bot by metol007

import discord
from discord.ext import commands
from discord.ext.commands import bot
import os

bot = commands.Bot(command_prefix="")

@bot.event
async def on_ready():
	print ("Ready for your commands master")
	print ("I am running on"+bot.user.name)
	print ("With the ID:"+bot.user.id)
	
@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("pong")
	
chat_filter = ["fuck"]
bypass_list = [445064818412617729]

@bot.command(pass_context=True)
async def on_message(message):
	contents = message.content.split("")
	for word in contents:
		if word.upper() in chat_filter:
			if not message.author.id in bypass_list:
				try:
					await client.delete_message (messae)
					await client.send_message(message.channel, "you cant say fuck anymore"

bot.run(os.environ["TOKEN"])
