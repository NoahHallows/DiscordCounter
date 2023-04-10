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
    number_up_to = message.content
    number_up_to = int(number_up_to)
    number_up_to = number_up_to + 1
    number_up_to = str(number_up_to)
    keyboard.write(number_up_to)
    keyboard.press_and_release("enter")
    #await message.channel.send(number_up_to)
 
client.run('MTA5NDc2NDk3NzM4ODI2MTQxOA.GS_TcQ.JdVqwX7bsf5M9HlHhrdgwBvER9nbQy_pLOUgq4')
