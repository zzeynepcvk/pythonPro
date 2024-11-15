import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('fotolar'))
    with open(f'fotolar/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

bot.run()

#klasör içinden rastgele foto gönderen bot
