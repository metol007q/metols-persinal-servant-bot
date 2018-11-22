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
	
@bot.command(pass_context=True)
async def fuck(ctx):
	await bot.say("Ill fuck you anytime")

@bot.command(pass_context=True)
async def tits(ctx):
	await bot.say("(.Y.)")
	
@bot.command(pass_context=True)
async def tit(ctx):
	await bot.say("(.)")
	
@bot.command(pass_context=True)
async def ass(ctx):
	await bot.say("(‿ˠ‿)")
	
@bot.command(pass_context=True)
async def show me everything(ctx):
	await bot.say("_____Sexy?Sex
____?Sexy?Sexy
___y?Sexy?Sexy?
___?Sexy?Sexy?S
___?Sexy?Sexy?S
__?Sexy?Sexy?Se
_?Sexy?Sexy?Se
_?Sexy?Sexy?Se
_?Sexy?Sexy?Sexy?
?Sexy?Sexy?Sexy?Sexy
?Sexy?Sexy?Sexy?Sexy?Se
?Sexy?Sexy?Sexy?Sexy?Sex
_?Sexy?__?Sexy?Sexy?Sex
___?Sex____?Sexy?Sexy?
___?Sex_____?Sexy?Sexy
___?Sex_____?Sexy?Sexy
____?Sex____?Sexy?Sexy
_____?Se____?Sexy?Sex
______?Se__?Sexy?Sexy
_______?Sexy?Sexy?Sex
________?Sexy?Sexy?sex
_______?Sexy?Sexy?Sexy?Se
_______?Sexy?Sexy?Sexy?Sexy?
_______?Sexy?Sexy?Sexy?Sexy?Sexy
_______?Sexy?Sexy?Sexy?Sexy?Sexy?S
________?Sexy?Sexy____?Sexy?Sexy?se
_________?Sexy?Se_______?Sexy?Sexy?
_________?Sexy?Se_____?Sexy?Sexy?
_________?Sexy?S____?Sexy?Sexy
_________?Sexy?S_?Sexy?Sexy
________?Sexy?Sexy?Sexy
________?Sexy?Sexy?S
________?Sexy?Sexy
_______?Sexy?Se
_______?Sexy?
______?Sexy?
______?Sexy?
______?Sexy?
______?Sexy
______?Sexy
_______?Sex
_______?Sex
_______?Sex
______?Sexy
______?Sexy
_______Sexy
_______ Sexy?
________SexY")

bot.run(os.environ["TOKEN"])
