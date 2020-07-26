import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf8') as jFile:
    jdata = json.load(jFile)

bot=commands.Bot(command_prefix='@')
@bot.event

async def on_ready():
    print(">>BOT Is Online!!<<")

@bot.event
async def on_member_join(member):
    
    channel = bot.get_channel(int(jdata['welcome_channel']))
    await channel.send(f'{member} join!')
@bot.event
async def on_member_remove(member):
    
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')





@bot.command()
#async def ping(ctx):
# await ctx.send(F'{round(bot.latency*1000)} (ms)')
async   def 圖片(ctx):
    random_pic= random.choice(jdata['pic1'])
    pic= discord.File(random_pic)
    await ctx.send(file=pic)

    #pic = discord.File(jdata['pic1'])
    #await ctx.send(file= pic)

@bot.command()
async   def YY(ctx):
    random_youtube= random.choice(jdata['url_youtube'])
    await ctx.send(random_youtube)

bot.run(jdata['token'])
