import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='@')

@bot.event

async def on_ready():
    print(">>BOT Is Online!!<<")


@bot.event
async def on_member_join(member):
    
    channel = bot.get_channel(736886903588257796)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    
    channel = bot.get_channel(736886903588257796)
    await channel.send(f'{member} leave!')


bot.run('NzM2ODkwNjUwODM4MDQwNTg2.Xx1Y5Q.UmK_A4zALOiL2DDFXIAC1rMjlLA')
