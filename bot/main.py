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
    if message.content.lower().strip().startswith(',09yx'):
       embed_m = discord.Embed(colour=0xFF0000)
       embed_m.add_field(name="<a:bubblerf:935756938661232690> Server Information; <a:bubblerf:935756938661232690>",
                         value=":burst1: 𝙉𝙤 𝙙𝙞𝙨𝙘𝙧𝙞𝙢𝙞𝙣𝙖𝙩𝙞𝙤𝙣 / 𝙝𝙖𝙧𝙖𝙨𝙨𝙢𝙚𝙣𝙩 / 𝙗𝙪𝙡𝙡𝙮𝙞𝙣𝙜.\n\n:burst1: 𝘼𝙩𝙩𝙖𝙘𝙠𝙞𝙣𝙜 𝙤𝙧 𝙙𝙞𝙨𝙘𝙧𝙞𝙢𝙞𝙣𝙖𝙩𝙞𝙣𝙜 𝙖𝙣𝙤𝙩𝙝𝙚𝙧 𝙢𝙚𝙢𝙗𝙚𝙧 𝙗𝙖𝙨𝙚𝙙 𝙤𝙣 𝙩𝙝𝙚𝙞𝙧 𝙧𝙖𝙘𝙚, 𝙨𝙚𝙭𝙪𝙖𝙡 𝙤𝙧𝙞𝙚𝙣𝙩𝙖𝙩𝙞𝙤𝙣, 𝙣𝙖𝙩𝙞𝙤𝙣𝙖𝙡𝙞𝙩𝙮, 𝙜𝙚𝙣𝙙𝙚𝙧, 𝙚𝙩𝙘 𝙞𝙨 𝙣𝙤𝙩 𝙖𝙡𝙡𝙤𝙬𝙚𝙙.\n\n:burst1:𝙏𝙖𝙨𝙩𝙚𝙡𝙚𝙨𝙨 𝙤𝙧 𝙪𝙣𝙣𝙚𝙘𝙚𝙨𝙨𝙖𝙧𝙞𝙡𝙮 𝙣𝙚𝙜𝙖𝙩𝙞𝙫𝙚 𝙗𝙚𝙝𝙖𝙫𝙞𝙤𝙧 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙥𝙪𝙣𝙞𝙨𝙝𝙚𝙙.\n\n:burst1: 𝙄𝙣𝙨𝙪𝙡𝙩𝙞𝙣𝙜/𝙩𝙖𝙡𝙠𝙞𝙣𝙜 𝙖𝙗𝙤𝙪𝙩 𝙀𝙢𝙢𝙖 𝙋𝙧𝙤𝙪𝙡𝙭, 𝘿𝙧𝙖𝙜𝙤𝙨 𝘾𝙝𝙞𝙧𝙞𝙖𝙘, 𝙖𝙣𝙙 𝙅𝙚𝙨𝙨𝙮 𝘾𝙖𝙧𝙤𝙣 𝙞𝙣 𝙖𝙣 𝙞𝙣𝙖𝙥𝙥𝙧𝙤𝙥𝙧𝙞𝙖𝙩𝙚 𝙢𝙖𝙣𝙣𝙚𝙧 𝙞𝙨 𝙣𝙤𝙩 𝙖𝙡𝙡𝙤𝙬𝙚𝙙 𝙖𝙣𝙙 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙥𝙪𝙣𝙞𝙨𝙝𝙚𝙙 𝙗𝙮 𝙗𝙖𝙣.\n\n- 𝘔𝘦𝘯 𝘐 𝘛𝘳𝘶𝘴𝘵 𝘚𝘦𝘳𝘷𝘦𝘳 𝘙𝘰𝘭𝘦𝘴\n\n:burst4: <@&924152053150920764> - 𝙊𝙬𝙣𝙚𝙧\n\n/n:burst4: <@&931682984568979537> - 𝘾𝙤-𝙊𝙬𝙣𝙚𝙧\n\n:burst4: <@&924156949401047061> - 𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝙈𝙚𝙣 𝙄 𝙏𝙧𝙪𝙨𝙩 𝘽𝙖𝙣𝙙 𝙈𝙚𝙢𝙗𝙚𝙧𝙨\n\n:burst4: <@&749401066428170298> - 𝘽𝙤𝙤𝙨𝙩𝙚𝙧𝙨 𝙬𝙞𝙩𝙝𝙞𝙣 𝙩𝙝𝙚 𝙨𝙚𝙧𝙫𝙚𝙧\n\n:burst4: <@&933175183861219399> - 𝙂𝙞𝙫𝙚𝙣 𝙧𝙤𝙡𝙚 𝙩𝙤 𝙖𝙡𝙡 𝙫𝙚𝙧𝙞𝙛𝙞𝙚𝙙 𝙪𝙨𝙚𝙧𝙨\n\n/n- 𝘊𝘰𝘭𝘰𝘶𝘳 𝘳𝘰𝘭𝘦𝘴 𝘪𝘯𝘧𝘰𝘳𝘮𝘢𝘵𝘪𝘰𝘯\n\n:burst3: 𝙞𝙛 𝙖𝙣𝙮 𝙤𝙛 𝙮𝙤𝙪 𝙥𝙧𝙚𝙛𝙚𝙧 𝙖 𝙘𝙤𝙡𝙤𝙪𝙧 𝙩𝙝𝙖𝙩 𝙞𝙨𝙣'𝙩 𝙘𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝙖𝙫𝙖𝙞𝙡𝙖𝙗𝙡𝙚; 𝙥𝙡𝙚𝙖𝙨𝙚 𝙛𝙚𝙚𝙡 𝙛𝙧𝙚𝙚 𝙩𝙤 𝙧𝙚𝙖𝙘𝙝 𝙤𝙪𝙩. 𝙞 𝙖𝙢 𝙢𝙤𝙧𝙚 𝙩𝙝𝙖𝙣 𝙝𝙖𝙥𝙥𝙮 𝙩𝙤 𝙜𝙞𝙫𝙚 𝙖𝙣𝙮 𝙤𝙛 𝙮𝙤𝙪 𝙮𝙤𝙪𝙧 '𝙤𝙬𝙣' 𝙘𝙤𝙡𝙤𝙪𝙧(𝙨).\n\n:burst3: 𝙩𝙞𝙥: 𝙧𝙚𝙜𝙖𝙧𝙙𝙞𝙣𝙜 𝙘𝙤𝙡𝙤𝙪𝙧 𝙧𝙚𝙖𝙘𝙩𝙞𝙤𝙣 𝙧𝙤𝙡𝙚𝙨; 𝙥𝙡𝙚𝙖𝙨𝙚 𝙢𝙖𝙠𝙚 𝙨𝙪𝙧𝙚 𝙩𝙤 𝙪𝙣𝙨𝙚𝙡𝙚𝙘𝙩 𝙮𝙤𝙪𝙧 𝙥𝙧𝙚𝙫𝙞𝙤𝙪𝙨 𝙘𝙤𝙡𝙤𝙪𝙧 𝙩𝙤 𝙚𝙣𝙨𝙪𝙧𝙚 𝙩𝙝𝙚 𝙣𝙚𝙬𝙡𝙮 𝙨𝙚𝙡𝙚𝙘𝙩𝙚𝙙 𝙤𝙣𝙚 𝙞𝙨 𝙨𝙝𝙤𝙬𝙣.\n\n𝙮𝙤𝙪'𝙧𝙚 𝙡𝙤𝙫𝙚𝙙,\n\n~m :burst2: Thanks so much! ~ Oncle <a:heartwonclejazz:931061570920931368>")
       await message.channel.send(embed=embed_m)
       time.sleep(2)
       await message.delete()

    # Men I Trust Commands:
    elif message.content.lower().strip().startswith('.reminder'):
       await message.channel.send('Please keep the chat clean while talking inside <#748642406231965868>. Thanks so much! ~ Oncle <a:heartwonclejazz:931061570920931368>')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.m emma proulx'):
       await message.channel.send('https://tenor.com/bMe4t.gif')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.m proulx hairflip'):
       await message.channel.send('https://tenor.com/9POk.gif')
       time.sleep(2)
       await message.delete()
  
    elif message.content.lower().strip().startswith('.m jammin'):
       await message.channel.send('https://tenor.com/9POs.gif')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.reddit'):
       await message.channel.send('https://www.reddit.com/r/menitrust/')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.tumblr'):
       await message.channel.send('https://menitrust.tumblr.com/')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.ad'):
       await message.channel.send('The Men I Trust Discord is a server dedicated to the indie band "Men I Trust." \n\nWe have an extremely welcoming community, where **everyone** is welcome! \n\nCome check us out! We love you, A Lot. \n\nhttps://discord.gg/Yzg3mfPhPA \n\nhttps://i.redd.it/vm1zofojn9h81.gif')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.youtube'):
       await message.channel.send('https://www.youtube.com/channel/UCOzZL8Sd8V8yFGWqOHnVqFA')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.youtube music'):
       await message.channel.send('https://music.youtube.com/channel/UCaPOa_Tg0TThuYSVtUEXb8g')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.spotify'):
       await message.channel.send('https://open.spotify.com/artist/3zmfs9cQwzJl575W1ZYXeT?autoplay=true')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.apple music'):
       await message.channel.send('https://music.apple.com/us/artist/men-i-trust/886240553')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.iheartradio'):
       await message.channel.send('https://www.iheart.com/artist/men-i-trust-30421840/?autoplay=true')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.pandora'):
       await message.channel.send('https://www.pandora.com/station/play/110003941483222834')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.oncle'):
       await message.channel.send('Oncle Jazz Commands: \n\n<a:burst5:934223774788759592> .m emma \n\n<a:burst5:934223774788759592> .m proulx hairflip \n\n<a:burst5:934223774788759592> .m jammin \n\n<a:burst5:934223774788759592> .reddit \n\n<a:burst5:934223774788759592> .tumblr \n\n<a:burst5:934223774788759592> .youtube \n\n<a:burst5:934223774788759592> .youtube music \n\n<a:burst5:934223774788759592> .spotify \n\n<a:burst5:934223774788759592> .apple music \n\n<a:burst5:934223774788759592> .iheartradio \n\n<a:burst5:934223774788759592> .pandora \n\n<a:burst5:934223774788759592> .ad \n\n<a:burst5:934223774788759592> .m message to meme \n\n<a:burst5:934223774788759592> .m meme \n\n<a:burst5:934223774788759592> .ian \n\n<a:burst5:934223774788759592> .benji')
       time.sleep(2)
       await message.delete()

    # Personal Server Commands:
    elif message.content.lower().strip().startswith('.m message to meme'):
       await message.channel.send('sorry <@324054566595198976> :( we all love you here!!! <3')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.m meme'):
       await message.channel.send('we all love you here <@324054566595198976>!!! <3')
       time.sleep(2)
       await message.delete()
  
    elif message.content.lower().strip().startswith('.ian'):
       await message.channel.send('check out <@429723963157905410>\'s stream! <3 https://twitch.tv/ianxian')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.benji'):
       await message.channel.send('check out <@695788578596192286>\'s stream! <3 https://twitch.tv/notbenja20')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith('.minecraft link'):
       await message.channel.send('MenITrust.aternos.me')
       time.sleep(2)
       await message.delete()

    elif message.content.lower().strip().startswith(',aert'):
       await message.channel.send('i love you guys too <a:heartwonclejazz:931061570920931368>')
       time.sleep(2)
       await message.delete()


client.run(os.getenv("DISCORD_TOKEN"))
