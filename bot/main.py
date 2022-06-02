import discord
from discord.ext import commands, tasks
import os
import time

bot = commands.Bot('$')
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="if you're drinking water")) 

target_channel_id = 860564834553692162, 938487387804286999

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#embed(s):
@tasks.loop(hours=3)
async def called_every_three_hours():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("Tomen agua porfa <3")

#Cron task reminder every 3 hours loop console print
@called_every_three_hours.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_every_three_hours.start()


#Funcion para enviar mensaje con el comando

@client.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().strip().startswith('$agua'):
        await message.channel.send('Tomen aguita cabros <3')
      time.sleep(2)
       await message.delete()

    if message.content.lower().strip().startswith('$benji'):
        await message.channel.send('the CLI works for us both now. finally done.*')
      time.sleep(2)
       await message.delete()


client.run(os.getenv("DISCORD_TOKEN"))
