import discord
import os
import time

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="𝐝𝐮𝐜𝐤𝐥𝐢𝐧𝐠𝐬")) 


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
        
    if message.content.lower().strip().startswith('.dhembedrr1'):
       embed_m = discord.Embed(colour=0x336a94)
       embed_m.add_field(name="~",
                         value='\n\n<a:dhrribbonblue:962889749255839784> <@&957540747538751519>\n\n<a:dhrribbonblue:962889749255839784> <@&957540790689755256>\n\n<a:dhrribbonblue:962889749255839784> <@&957540772398395392>\n\n<a:dhrribbonblue:962889749255839784> <@&957540812877611048>\n\n<a:dhrribbonblue:962889749255839784> <@&957540851901403166>\n\n<a:dhrribbonblue:962889749255839784>  <@&957540922671923271>\n\n~\n\n<a:dhrribbonblue:962889749255839784> <@&957542213905182760>\n\n<a:dhrribbonblue:962889749255839784> <@&957542256456396820>')
       embed_m.set_image(url="https://media.discordapp.net/attachments/917513455395831818/962905226166296596/mr._duckie_-1_re-revised.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    if message.content.lower().strip().startswith('.dhembedrr2'):
       embed_m = discord.Embed(colour=0xa40e26)
       embed_m.add_field(name="~",
                         value='\n\n<:dhoc:959584599841849344> <@&959587688086917233>\n\n<:dhasia:959584599728603187> <@&959577150393057290>\n\n<:dheu:959584599644700723> <@&959577017072881714>\n\n<:dhna:959584599229472839> <@&959576872717541387>\n\n<:dhsa:959584599355301988> <@&959576971455643708>')
       embed_m.set_image(url="https://images-ext-2.discordapp.net/external/GnOPCL-Zjc2w94-Vi6JuXy1sd0ajHgYXQLnPAsFqrwk/https/media.discordapp.net/attachments/917513455395831818/962895880963362816/mr._duckie_-_2.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    if message.content.lower().strip().startswith('.dhembedrr3'):
       embed_m = discord.Embed(colour=0xEA8D35)
       embed_m.add_field(name="~",
                         value='\n\n<:dhrflower:959494929262968903> <@&963378319389261825>\n\n<:dhrflower:959494929262968903> <@&963378529536475176>\n\n<:dhrflower:959494929262968903>  <@&963378531994337360>\n\n<:dhrflower:959494929262968903> <@&963378533391024150>\n\n<:dhrflower:959494929262968903> <@&963378534364119080>\n\n<:dhrflower:959494929262968903> <@&963378535123275796>\n\n<:dhrflower:959494929262968903> <@&963378537304301568>\n\n<:dhrflower:959494929262968903> <@&963378537946026004>\n\n<:dhrflower:959494929262968903> <@&963378539246268417>\n\n<:dhrflower:959494929262968903> <@&963379237425926144>')
       embed_m.set_image(url="https://cdn.discordapp.com/attachments/957102779334270986/963385766728323142/135-1356350_hue-y-duck-pixel-duck-hd-png-download-removebg-preview3.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    #commands:
    elif message.content.lower().strip().startswith('commandhere'):
       await message.channel.send('bodytexthere')
       time.sleep(2)
       await message.delete()

client.run(os.getenv("DISCORD_TOKEN"))
