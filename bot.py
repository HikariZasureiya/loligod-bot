import os
import discord
from dotenv import load_dotenv
import random
import requests
from discord.ext import commands
from discord import default_permissions

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='./', description="This is a test bot",intents=discord.Intents.all())
# slash_bot = discord.Bot(intents=discord.Intents.all())
# confess = discord.SlashCommandGroup("greetings", "make a confession")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


''' made this to make myself a moderator. worth it '''
# @bot.command(name='test')
# async def test(ctx):
#     print("here")
#     member = ctx.author
#     guild = ctx.guild
#     role = guild.get_role(729892169841770527)
#     await member.add_roles(role)
# 771233498619052033

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
        print("yes",ctx.guild.id)
        await ctx.reply(f"It's {found}")
    except Exception as e:
        print("Exception: ", e)
        await ctx.send("Invalid command")



@bot.command(name = 'chat')
async def chat(ctx,*,message):
    url = 'https://loligod-bot.onrender.com/geminichat'

    # url = 'http://localhost:8000/geminichat'
    data = {'server_id':ctx.guild.id , 'prompt': message}

    # Send the POST request
    response = requests.post(url, json=data)

    print(response)

    # Check the response
    if response.json() and response.status_code == 200:
        # print("Response from API:", response.json())
        await ctx.reply(response.json())
    else:
        requests.get('https://loligod-bot.onrender.com/deletechat',params={"server_id": ctx.guild.id})
        # print("deleting")
        # requests.get('http://localhost:8000/deletechat',params={"server_id": ctx.guild.id})
        response = requests.post(url, json=data)
        if response.json():
           
            await ctx.reply(response.json())
        else:
            await ctx.reply("i ain't replying to that try harder")

@bot.slash_command(name = "confess")
@commands.has_permissions()
async def confess(ctx,title ,confession):
    # url = "http://localhost:8000/confess"
    url = "https://loligod-bot.onrender.com/confess"
    data = {"server_id": ctx.guild.id , "title": title , "message":confession}
    response = requests.post(url , data)
    print(response.json())
    decorated_confession = f'# __Anonymous Confession No.{response.json()}__ \n## {title}\n{confession}'
    await ctx.send(decorated_confession)
    await ctx.response.send_message("confession sent", ephemeral=True)



bot.run(TOKEN)
