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

    if message.content.lower().strip().startswith('$testingembed'):
        await message.channel.send('this command *should* delete')
        time.sleep(2)
        await message.delete()

    if message.content.lower().strip().startswith('$pride'):
        await message.channel.send('happy pride month from Water Reminder to you. I hope you have a enjoyable; and **refreshing** pride month.')
        time.sleep(2)
        await message.delete()


    if message.content.lower().strip().startswith('circuit1'):
       embed_m = discord.Embed(colour=0xa3dab5)
       embed_m.add_field(name="~",
                         value='This server is a friend based server. The following channels are designed for bot use; <#984622238311522364>, <#938487387804287001>, <#958956207941488680>, <#977347893386162186>. Some channels have more than one bot infused within itself; so be aware of it\'s designated channel. ')
       embed_m.set_image(url="https://data.whicdn.com/images/356922579/original.gif")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete() 

client.run(os.getenv("DISCORD_TOKEN"))
