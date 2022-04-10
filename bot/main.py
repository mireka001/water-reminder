import discord
import os
import time

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="baby chicks <3")) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #embed:
    if message.content.lower().strip().startswith('.dinfo'):
       embed_m = discord.Embed(colour=0xfbf2b4)
       embed_m.add_field(name="",
                         value='\n\nplease be kind <a:hartlemon:957115698327482428>\n\nwe love u here, no need to worry <a:hartlemon:957115698327482428>')
       embed_m.set_image(url="https://cdn.discordapp.com/attachments/957102779334270986/962568895812751410/outside_.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    #commands:
    elif message.content.lower().strip().startswith('command prefix'):
       await message.channel.send('body')
       time.sleep(2)
       await message.delete()

client.run(os.getenv("DISCORD_TOKEN"))
