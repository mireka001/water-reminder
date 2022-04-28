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


    if message.content.lower().strip().startswith(';roles1'):
       embed_m = discord.Embed(colour=0x000000)
       embed_m.add_field(name="<3",
                         value='<a:blackarrow:969162216307818556> <@&957540747538751519>\n\n<a:blackarrow:969162216307818556> <@&957540790689755256>\n\n<a:blackarrow:969162216307818556> <@&957540851901403166>\n\n<a:blackarrow:969162216307818556> <@&957542213905182760>\n\n<a:blackarrow:969162216307818556> <@&957542256456396820>')
       embed_m.set_image(url="https://images-ext-1.discordapp.net/external/SqDgswiJyElYFa64YXiy7hXmbQghrJbs4SF5Ll4udOk/https/images-ext-2.discordapp.net/external/Mn4vIHHMLfOa-yPuL5gXZ6PgmW3nvHnTVJZJXLDqDaw/%253Fauto%253Dcompress%2526cs%253Dtinysrgb%2526dpr%253D1%2526w%253D500/https/images.pexels.com/photos/3048527/pexels-photo-3048527.png")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()


       
    if message.content.lower().strip().startswith(';roles2'):
       embed_m = discord.Embed(colour=0x000000)
       embed_m.add_field(name="<3",
                         value='<a:blackarrow:969162216307818556> <@&959577017072881714>\n\n<a:blackarrow:969162216307818556> <@&959587688086917233>\n\n<a:blackarrow:969162216307818556> <@&959576872717541387>\n\n<a:blackarrow:969162216307818556> <@&959576971455643708>\n\n<a:blackarrow:969162216307818556> <@&959577150393057290>')
       embed_m.set_image(url="https://images-ext-2.discordapp.net/external/1zEYKNy-K9hDQsZpsosSOxGJRwIfzNJqjExHU0LQnfA/%3Fwidth%3D798%26height%3D1197/https/images-ext-1.discordapp.net/external/Qb_x2mHQhIhwP6JDWWKGhwLh2yGIUUPyrHOG_ihM2jw/%253Fixlib%253Drb-1.2.1%2526ixid%253DMnwxMjA3fDB8MHxzZWFyY2h8MXx8YmxhY2slMjBhbmQlMjB3aGl0ZSUyMHBob3RvZ3JhcGh5fGVufDB8fDB8fA%25253D%25253D%2526w%253D1000%2526q%253D80/https/images.unsplash.com/photo-1597871040916-4b4c20ba08dd")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)



       await message.delete()
    if message.content.lower().strip().startswith(';roles3'):
       embed_m = discord.Embed(colour=0x000000)
       embed_m.add_field(name="<3",
                         value='')
       embed_m.set_image(url="")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()



    if message.content.lower().strip().startswith('blank'):
       embed_m = discord.Embed(colour=0x000000)
       embed_m.add_field(name="<3",
                         value='')
       embed_m.set_image(url="")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()



    if message.content.lower().strip().startswith('blank'):
       embed_m = discord.Embed(colour=0x000000)
       embed_m.add_field(name="<3",
                         value='')
       embed_m.set_image(url="")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()


client.run(os.getenv("DISCORD_TOKEN"))
