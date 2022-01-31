import discord
import os

client = discord.Client()

@client.event
async def on_ready():
 await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name="Oncle Jazz")) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return


 
#Men I Trust Commands:

    if message.content.lower().strip().startswith('.m emma proulx'):
       await message.channel.send('https://tenor.com/bMe4t.gif')

    if message.content.lower().strip().startswith('.m proulx hairflip'):
       await message.channel.send('https://tenor.com/9POk.gif')
  
    if message.content.lower().strip().startswith('.m jammin'):
       await message.channel.send('https://tenor.com/9POs.gif')

    if message.content.lower().strip().startswith('.reddit'):
       await message.channel.send('https://www.reddit.com/r/menitrust/') 

    if message.content.lower().strip().startswith('.tumblr'):
       await message.channel.send('https://menitrust.tumblr.com/') 

    if message.content.lower().strip().startswith('.ad'):
       await message.channel.send('The Men I Trust Discord is a server dedicated to the indie band "Men I Trust." \n\nWe have an extremely welcoming community, where **everyone** is welcome! \n\nCome check us out! We love you, A Lot. \n\nhttps://discord.gg/menitrust \n\nhttps://tinyurl.com/2fska59c')

    if message.content.lower().strip().startswith('.youtube'):
       await message.channel.send('https://www.youtube.com/channel/UCOzZL8Sd8V8yFGWqOHnVqFA') 


    if message.content.lower().strip().startswith('.youtube music'):
       await message.channel.send('https://music.youtube.com/channel/UCaPOa_Tg0TThuYSVtUEXb8g') 


    if message.content.lower().strip().startswith('.spotify'):
       await message.channel.send('https://open.spotify.com/artist/3zmfs9cQwzJl575W1ZYXeT?autoplay=true') 


    if message.content.lower().strip().startswith('.apple music'):
       await message.channel.send('https://music.apple.com/us/artist/men-i-trust/886240553') 


    if message.content.lower().strip().startswith('.iheartradio'):
       await message.channel.send('https://www.iheart.com/artist/men-i-trust-30421840/?autoplay=true') 


    if message.content.lower().strip().startswith('.pandora'):
       await message.channel.send('https://www.pandora.com/station/play/110003941483222834') 

    if message.content.lower().strip().startswith('.oncle'):
       await message.channel.send('.m emma \n\n.m proulx hairflip \n\n.m jammin \n\n.reddit \n\n.tumblr \n\n.youtube \n\n.youtube music \n\n.spotify \n\n.apple music \n\n.iheartradio \n\n.pandora \n\n.ad \n\n.m message to meme \n\n.m meme \n\n.ian \n\n.benji') 



 #Personal Server Commands:
  
    if message.content.lower().strip().startswith('.m message to meme'):
        await message.channel.send('sorry <@324054566595198976> :( we all love you here!!! <3') 

        
    if message.content.lower().strip().startswith('.m meme'):
        await message.channel.send('we all love you here <@324054566595198976>!!! <3') 
  
    if message.content.lower().strip().startswith('.ian'):
       await message.channel.send('check out <@429723963157905410>\'s stream! <3 https://twitch.tv/ianxian') 

    if message.content.lower().strip().startswith('.benji'):
       await message.channel.send('check out <@695788578596192286>\'s stream! <3 https://twitch.tv/notbenja20') 




client.run(os.getenv("DISCORD_TOKEN"))
