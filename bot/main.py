import discord
import os
import time

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="my lovelies <3")) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

#embed(s):


    if message.content.lower().strip().startswith('command'):
       embed_m = discord.Embed(colour=0x000000)
       embed_m.add_field(name="<3",
                         value='')
       embed_m.set_image(url="")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

client.run(os.getenv("DISCORD_TOKEN"))
