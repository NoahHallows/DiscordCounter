import discord
import keyboard
 
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
 
client.run('MTA5NDc2NDk3NzM4ODI2MTQxOA.GrcYwy.SxlSM9bNx7rITBvAq23locVSIDux9yqB6Dim24')