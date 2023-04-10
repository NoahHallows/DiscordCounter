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
    if message.author == client.user:
        return
    print(message.content)
    print(len(message.content))
    if message.content.isdigit():
        #await message.channel.send("is int")
        count = int(message.content)
        next_count_str = str(count + 1)
        keyboard.write(next_count_str)
        keyboard.press_and_release("enter")
    else:
        await message.channel.send("Please refrain from using this channel for things other than counting or you will be terminated")
    print("done")
print(TOKEN) 
client.run(TOKEN)