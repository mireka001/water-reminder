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

#Men I Trust Embed:
    if message.content.lower().strip().startswith('.information'):
       embed_m = discord.Embed(colour=0xFF0000)
       embed_m.add_field(name="<a:burst2:934223774759399514> Server Information <a:burst2:934223774759399514>",
                         value="-\n\n<a:burst5:934223774788759592> **No discrimination, harrassment, or bullying.**\n\n<a:burst5:934223774788759592> **No attacking members based on race, sexuality, gender identity, etc.**\n\n<a:burst5:934223774788759592> **Be respectful & kind.**\n\n<a:burst5:934223774788759592> **Insulting Emma Proulx, Dragos Chiriac, and Jessy Caron is permitted. This is punishable by ban**.\n\n<a:burst5:934223774788759592> **Roles within the server;**\n\n<@&924340565347299369> - **Owner**\n\n<@&924206476149538828> - **Co-Owner**\n\n<@&924156949401047061> - **Band Members**\n\n<@&749401066428170298> - **Boosters**\n\n<@&933175183861219399> - **Given Role.**")
       embed_m.set_thumbnail(url="https://images.squarespace-cdn.com/content/v1/54e1b4c1e4b0ef0a3e407bd1/1586767283721-Y9HQUO82LJC594XQA562/daisies_white_footer.gif")
       await message.channel.send(embed=embed_m)



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
       await message.channel.send('Oncle Jazz Commands: \n\n<a:burst5:934223774788759592> .m emma \n\n<a:burst5:934223774788759592> .m proulx hairflip \n\n<a:burst5:934223774788759592> .m jammin \n\n<a:burst5:934223774788759592> .reddit \n\n<a:burst5:934223774788759592> .tumblr \n\n<a:burst5:934223774788759592> .youtube \n\n<a:burst5:934223774788759592> .youtube music \n\n<a:burst5:934223774788759592> .spotify \n\n<a:burst5:934223774788759592> .apple music \n\n<a:burst5:934223774788759592> .iheartradio \n\n<a:burst5:934223774788759592> .pandora \n\n<a:burst5:934223774788759592> .ad \n\n<a:burst5:934223774788759592> .m message to meme \n\n<a:burst5:934223774788759592> .m meme \n\n<a:burst5:934223774788759592> .ian \n\n<a:burst5:934223774788759592> .benji') 



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


