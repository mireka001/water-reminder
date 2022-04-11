import discord
import os
import time

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="ducklings")) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #embed:
    if message.content.lower().strip().startswith('.dhinfo'):
       embed_m = discord.Embed(colour=0xEA8D35)
       embed_m.add_field(name="~",
                         value='\n\n<:dhrduckheart:960366979657650176> please be kind\n\n<:dhrduckheart:960366979657650176> we love u here, no need to worry')
       embed_m.set_image(url="https://media.discordapp.net/attachments/917513455395831818/962904025689387018/mr._duckie_-3.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()
        
    if message.content.lower().strip().startswith('.dhembed1'):
       embed_m = discord.Embed(colour=0x336a94)
       embed_m.add_field(name="~",
                         value='\n\n<a:hartlemon:957115698327482428> <@&957540747538751519>\n\n<a:hartorange:957115698415542322> <@&957540790689755256>\n\n<a:hartlime:957115698352619610> <@&957540772398395392>\n\n<a:hartraspberry:957115698323259452> <@&957540812877611048>\n\n<:dhrknife:959494964943912990>  <@&957540922671923271>\n\n~\n\n<a:hartcherry:957115698231013407> <@&957542213905182760>\n\n<a:hartstrawberry:957115698491060255> <@&957542256456396820>')
       embed_m.set_image(url="https://media.discordapp.net/attachments/917513455395831818/962905226166296596/mr._duckie_-1_re-revised.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    if message.content.lower().strip().startswith('.dhembed2'):
       embed_m = discord.Embed(colour=0xa40e26)
       embed_m.add_field(name="~",
                         value='\n\n<:dhoc:959584599841849344> <@&959587688086917233>\n\n<:dhasia:959584599728603187> <@&959577150393057290>\n\n<:dheu:959584599644700723> <@&959577017072881714>\n\n<:dhna:959584599229472839> <@&959576872717541387>\n\n<:dhsa:959584599355301988> <@&959576971455643708>')
       embed_m.set_image(url="https://images-ext-2.discordapp.net/external/GnOPCL-Zjc2w94-Vi6JuXy1sd0ajHgYXQLnPAsFqrwk/https/media.discordapp.net/attachments/917513455395831818/962895880963362816/mr._duckie_-_2.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    #commands:
    elif message.content.lower().strip().startswith('commandhere'):
       await message.channel.send('bodytexthere')
       time.sleep(2)
       await message.delete()

client.run(os.getenv("DISCORD_TOKEN"))
