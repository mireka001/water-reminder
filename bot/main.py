import discord
import os
import time

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="baby chicks <3")) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #embed:
    if message.content.lower().strip().startswith('.dhinfo'):
       embed_m = discord.Embed(colour=0xfbf2b4)
       embed_m.add_field(name="\n",
                         value='\n\nplease be kind <a:hartlemon:957115698327482428>\n\nwe love u here, no need to worry <a:hartlemon:957115698327482428>')
       embed_m.set_image(url="https://cdn.discordapp.com/attachments/957102779334270986/962568895812751410/outside_.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    #commands:
    elif message.content.lower().strip().startswith('.dhembed'):
       await message.channel.send('<a:hartlemon:957115698327482428> <@&957540747538751519>\n\n<a:hartorange:957115698415542322> <@&957540790689755256>\n\n<a:hartlime:957115698352619610> <@&957540772398395392>\n\n<a:hartraspberry:957115698323259452> <@&957540812877611048>\n\n<:dhrknife:959494964943912990>  <@&957540922671923271>\n\n~\n\n<a:hartcherry:957115698231013407> <@&957542213905182760>\n\n<a:hartstrawberry:957115698491060255> <@&957542256456396820>')
       time.sleep(2)
       await message.delete()

client.run(os.getenv("DISCORD_TOKEN"))
