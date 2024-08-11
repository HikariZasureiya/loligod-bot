import os
import discord
from dotenv import load_dotenv
import random

from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$', description="This is a test bot",intents=discord.Intents.all())


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
        for i in range(15):
            await ctx.send(args[0])


@bot.command(name='toss')
async def toss(ctx, *args ):
    try:
        chance=['heads','tails']
        found = random.choice(chance)
        if args[0]==found:   
            await ctx.send(f"K you win it's {found}")
        else: 
            await ctx.send("you lose L")
    except:
        await ctx.send("Invalid command")


bot.run(TOKEN)
