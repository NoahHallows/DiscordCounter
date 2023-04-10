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
    print(number_up_to)
    print(len(number_up_to))
    try:
        number_up_to = int(number_up_to)
        number_up_to = number_up_to + 1
        number_up_to = str(number_up_to)
        keyboard.write(number_up_to)
        keyboard.press_and_release("enter")
    except:
        await message.channel.send("Error")
    print("done")
    #await message.channel.send(number_up_to)
 
client.run('MTA5NDc2NDk3NzM4ODI2MTQxOA.GA51K_.nnYqd8aoSLaA3Y9fnjVbGb2KY2C6kOi1hEEEmw')
