import discord
from dotenv import load_dotenv
import os
import re

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

trigger_text_with_space = 'this is the way '
trigger_text_without_space = 'this is the way'
reply_text = 'This is the way'
# Define a regular expression pattern to match the message content
pattern = r"\bthis\s+is\s+the\s+way[\!\?\.]*\b" 
# Compile the pattern
regex = re.compile(pattern, flags=re.IGNORECASE)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global trigger_text, reply_text
    if message.author == client.user:
        return
    # Check if the message content matches the pattern
    if regex.search(message.content):
        await message.channel.send(reply_text)
    
client.run(TOKEN)