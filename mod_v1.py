import discord
from dotenv import load_dotenv
import os
import re

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # Define the word that should be present in the nickname
    required_word = "muffin"
    # Print the list of servers that the bot is a member of
    print("List of servers:")
    for index, guild in enumerate(client.guilds):
        print(f"{index}: {guild.name}")
    
    # Get the server object by name
    guild_name = "Darthmuffin's test server"  # Replace with the name of the desired server
    guild = discord.utils.get(client.guilds, name=guild_name)

    # Loop through all members in the server
    for member in guild.members:
        # Get the current nickname of the member
        current_nick = member.nick
        print(current_nick)
        if current_nick is not None:
            # Check if the required word is not present in the nickname
            if required_word not in current_nick.lower():
                # Update the nickname to include the required word
                new_nick = f"{required_word} {current_nick}" if current_nick else required_word
                await member.edit(nick=new_nick)
        else:
            print("Current member doesn't have a nickname")

    
    
client.run(TOKEN)