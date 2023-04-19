from time import sleep

import os
import discord
import keyboard
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') 

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: #or message.author == "Darthmuffin#5299":
        return
    print(message.author)
    print(message.content)
    #print(len(message.content))
    if message.content.isdigit():
        #await message.channel.send("is int")
        count = int(message.content)
        next_count = count + 1
        next_count_str = str(next_count)
        #keyboard.write(next_count_str)
        sleep(1)
        #keyboard.press_and_release("enter")
        await message.channel.send(next_count_str)
    else:
        await message.channel.send("Please refrain from using this channel for things other than counting or you will be terminated")
 
client.run(TOKEN)