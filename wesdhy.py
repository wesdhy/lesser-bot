import discord
import random
from discord.ext import commands
import time
from datetime import datetime, timedelta
client = commands.Bot(command_prefix = '@') 


@client.event
async def on_ready():
    #awaitj client.change_presence(status=discord.Status.online, activity=discord.Game('Test bot'))
    print("lesser  start")
#봇이 켜지면, 봇의 상태메시지를 TestBot으로 바꾼 후, 콘솔에 로그를 찍습니다.

@client.command()
async def super113355(ctx, amount=99):
	time2 = datetime.now()
	await ctx.channel.purge(limit = amount)
	print("100",time2)
time.sleep(10)

@client.command()
async def clear10(ctx, amount=10):
	time2 = datetime.now()
	await ctx.channel.purge(limit = amount)
	print("10",time2)
time.sleep(10)

@client.command()
async def clear(ctx, amount=1):
	await ctx.channel.purge(limit = amount)
time.sleep(10)
    
    
client.run('')



