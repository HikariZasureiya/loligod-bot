import os
import discord
from dotenv import load_dotenv
import random
import requests
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='./', description="This is a test bot",intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='convert')
async def convert(ctx, *args):
    print("works" , args)
    s=' nigga '.join(args)
    await ctx.send(s)

@bot.command(name='test')
async def test(ctx, channel:discord.TextChannel, title, *, message):
    print("yay", ctx.author)
    await channel.send(f'**{title}**\n{message}')

@bot.command(name="spam")
async def spam(ctx,*args):
    if args!=():
        s=' '.join(args)
        for i in range(20):
            await ctx.send(s)


@bot.command(name='toss')
async def toss(ctx):
    try:
        chance=['heads','tails']
        found = random.choice(chance)
        await ctx.reply(f"It's {found}")
    except Exception as e:
        print("Exception: ", e)
        await ctx.send("Invalid command")


@bot.command(name = 'chat')
async def chat(ctx,message):
    url = 'https://loligod-bot.onrender.com/geminichat'
    data = {'prompt': message}

    # Send the POST request
    response = requests.post(url, json=data)

    # Check the response
    if response.status_code == 200:
        print("Response from API:", response.json())
        await ctx.reply(response.json())
    else:
        print("Failed to get a valid response. Status code:", response.status_code)
    
bot.run(TOKEN)
