import discord
import os
import time

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name="Oncle Jazz")) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Men I Trust Embed:
    if message.content.lower().strip().startswith('.channel'):
       embed_m = discord.Embed(colour=0xFF0000)
       embed_m.add_field(name="**Server Information;**",
                         value='-\n\n**Rules;**\n\nNo discrimination, Bullying, etc.\n\nAttacking any members based on sexuality, race, gender identity, etc is punishable by **ban.**\n\nNSFW is **not permitted** within the server, due to the fact that we are minor friendly.\n\n- \n\n**Server Roles;**\n\n<@&924152053150920764> - Owners <@713677600572047401>, <@304995404917768193>\n\n<@&937601501201833984> - Staff Members \n\n<@&924156949401047061> - Official Band Members\n\n<@&749401066428170298> - Boosters within the server\n\nThanks so much! ~ Men I Trust Staff <:hartpinky:931246593527644190>')
       embed_m.set_thumbnail(url="https://cdn.discordapp.com/emojis/931246593527644190.webp?size=240&quality=lossless")                
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    # Men I Trust Commands:
    elif message.content.lower().strip().startswith('.reminder'):
       await message.channel.send('Please keep the chat clean while talking inside <#748642406231965868>. Thanks so much! ~ Oncle <a:heartwonclejazz:931061570920931368>')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',m emma proulx'):
       await message.channel.send('https://tenor.com/bMe4t.gif')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',m proulx hairflip'):
       await message.channel.send('https://tenor.com/9POk.gif')
       time.sleep(2)
       await message.delete()
  
    elif message.content.lower().strip().startswith(',m jammin'):
       await message.channel.send('https://tenor.com/9POs.gif')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',reddit'):
       await message.channel.send('https://www.reddit.com/r/menitrust/')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',tumblr'):
       await message.channel.send('https://menitrust.tumblr.com/')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',ad'):
       await message.channel.send('The Men I Trust Discord is a server dedicated to the indie band "Men I Trust." \n\nWe have an extremely welcoming community, where **everyone** is welcome! \n\nCome check us out! We love you, A Lot. \n\nhttps://discord.io/menitrust\n\nhttps://i.redd.it/vm1zofojn9h81.gif')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',youtube'):
       await message.channel.send('https://www.youtube.com/channel/UCOzZL8Sd8V8yFGWqOHnVqFA')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',youtube music'):
       await message.channel.send('https://music.youtube.com/channel/UCaPOa_Tg0TThuYSVtUEXb8g')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',spotify'):
       await message.channel.send('https://open.spotify.com/artist/3zmfs9cQwzJl575W1ZYXeT?autoplay=true')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',apple music'):
       await message.channel.send('https://music.apple.com/us/artist/men-i-trust/886240553')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',iheartradio'):
       await message.channel.send('https://www.iheart.com/artist/men-i-trust-30421840/?autoplay=true')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',pandora'):
       await message.channel.send('https://www.pandora.com/station/play/110003941483222834')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',oncle'):
       await message.channel.send('Oncle Jazz Commands: \n\n<a:burst5:934223774788759592> .m emma \n\n<a:burst5:934223774788759592> .m proulx hairflip \n\n<a:burst5:934223774788759592> .m jammin \n\n<a:burst5:934223774788759592> .reddit \n\n<a:burst5:934223774788759592> .tumblr \n\n<a:burst5:934223774788759592> .youtube \n\n<a:burst5:934223774788759592> .youtube music \n\n<a:burst5:934223774788759592> .spotify \n\n<a:burst5:934223774788759592> .apple music \n\n<a:burst5:934223774788759592> .iheartradio \n\n<a:burst5:934223774788759592> .pandora \n\n<a:burst5:934223774788759592> .ad \n\n<a:burst5:934223774788759592> .m message to meme \n\n<a:burst5:934223774788759592> .m meme \n\n<a:burst5:934223774788759592> .ian \n\n<a:burst5:934223774788759592> .benji')
       time.sleep(2)
       await message.delete()

    # Personal Server Commands:
    elif message.content.lower().strip().startswith(',m message to meme'):
       await message.channel.send('sorry <@324054566595198976> :( we all love you here!!! <3')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',m meme'):
       await message.channel.send('we all love you here <@324054566595198976>!!! <3')
       time.sleep(2)
       await message.delete()
  
    elif message.content.lower().strip().startswith(',ian'):
       await message.channel.send('check out <@429723963157905410>\'s stream! <3 https://twitch.tv/ianxian')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',benji'):
       await message.channel.send('check out <@695788578596192286>\'s stream! <3 https://twitch.tv/notbenja20')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',minecraft link'):
       await message.channel.send('MenITrust.aternos.me')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',aert'):
       await message.channel.send('i love you guys too <a:heartwonclejazz:931061570920931368>')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',ama'):
       await message.channel.send('oh, you fokah')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',meme'):
       await message.channel.send('meme, even at your lowest in life. i want you to know that you matter. you matter not only to me; but to us all. you have been such a bright person in my life. and i can\'t ask for a better person to do so. you make this world so much brighter in these hard times. i know you\'ve had your own struggles but i want you to know that i am so proud of you for getting past them, and moving fowards. you\'re so brave. i love you so much love.')
       time.sleep(2)
       await message.delete()

client.run(os.getenv("DISCORD_TOKEN"))
