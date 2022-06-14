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


    if message.content.lower().strip().startswith('$circuit1'):
       embed_m = discord.Embed(colour=0xa3dab5)
       embed_m.add_field(name="Server Information:",
                         value='-\n\nThis server is a private, friend based community.\n\n Please be respectful of that, and refrain from "spreading" the server.\n\nOur server rules consist of;\n\n**Be respectful.**\n\n**Be kind.**\n\nPlease keep all NSFW content in it\'s **proper channel.**\n\nAny questions, or concerns please reach out to <@961462461763031070>.')
       embed_m.set_thumbnail(url="https://thumbs.gfycat.com/WhoppingPassionateGalapagospenguin-max-1mb.gif")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete() 

    if message.content.lower().strip().startswith('$circuit2'):
       embed_m = discord.Embed(colour=0xa3dab5)
       embed_m.add_field(name="Server Roles:",
                         value='-\n\nThe roles provided, are Pronouns, and Age roles.\n\n*Please be aware that more may be added if needed.*\n\n<@&957540747538751519>\n\n<@&957540790689755256>\n\n<@&957540772398395392>\n\n<@&957540812877611048>\n\n<@&957540851901403166>\n\n<@&957542213905182760>\n\n<@&957542256456396820>')
       embed_m.set_thumbnail(url="https://media.discordapp.net/attachments/984628727021461504/984632547558436904/ezgif-1-6968916f5b.gif")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete() 


    if message.content.lower().strip().startswith('$circuit3'):
       embed_m = discord.Embed(colour=0xa3dab5)
       embed_m.add_field(name="<3",
                         value='-\n\nbeep boop...\n\n<@&957053492906831945> i hope you all are doing well! please make sure to take care of yourselves. <:circuitgreenheart:984392506013806632>')
       embed_m.set_thumbnail(url="https://cdn.discordapp.com/emojis/963450818147778570.gif?size=240&quality=lossless")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete() 

client.run(os.getenv("DISCORD_TOKEN"))
