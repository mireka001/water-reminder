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

    if message.content.lower().strip().startswith('.m hello'):
        await message.channel.send('hi hi! https://c.tenor.com/4pSNX9roPqEAAAAd/menitrust-norton-commander.gif')


    if message.author == client.user:
        return

    if message.content.lower().strip().startswith('.m welcome'):
        await message.channel.send('welcome! https://thumbs.gfycat.com/GrimyBetterAdder-max-1mb.gif')


    if message.author == client.user:
        return
     
    if message.content.lower().strip().startswith('.m i love you'):
        await message.channel.send('i love you too https://tenor.com/WeeS.gif')

    if message.author == client.user:
        return

    if message.content.lower().strip().startswith('.m hug'):
        await message.channel.send('https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif')
    
     
    if message.content.lower().strip().startswith('.m kissy'):
        await message.channel.send('https://media.giphy.com/media/iJDthUh1cvaF2/giphy.gif')

   
    if message.content.lower().strip().startswith('.m  somebody love me, for fucks sake why does nobody love me!'):
        await message.channel.send('sorry <@324054566595198976> :( we all love you here!!! <3') 

        
    if message.content.lower().strip().startswith('.m meme'):
        await message.channel.send('we all love you here <@324054566595198976>!!! <3')  
   
        
    if message.content.lower().strip().startswith('.m wink'):
        await message.channel.send('https://tenor.com/bNyLU.gif') 

        
    if message.content.lower().strip().startswith('.m youtube'):
       await message.channel.send('https://www.youtube.com/')


    if message.content.lower().strip().startswith('.m emma'):
       await message.channel.send('https://tenor.com/bMe4t.gif')


    if message.content.lower().strip().startswith('.m wave'):
       await message.channel.send('https://tenor.com/blP4l.gif')

    
    if message.content.lower().strip().startswith('.m handshake'):
       await message.channel.send('https://tenor.com/blLXy.gif')

           
    if message.content.lower().strip().startswith('.m ick'):
       await message.channel.send('https://tenor.com/7w1S.gif') 

   
    if message.content.lower().strip().startswith('.m loser'):
       await message.channel.send('https://tenor.com/bgdt3.gif') 


    if message.content.lower().strip().startswith('.shocked'):
       await message.channel.send('https://media.giphy.com/media/3o7TKFq4jy3JeWyn8A/giphy.gif')


    if message.content.lower().strip().startswith('.wow'):
       await message.channel.send('https://media.giphy.com/media/1Zt3z4uEBPZQY/giphy.gif')

    
    if message.content.lower().strip().startswith('.m i hate you'):
       await message.channel.send('https://tenor.com/9eCN.gif') 

    if message.content.lower().strip().startswith('.m sad'):
       await message.channel.send('https://tenor.com/btf9K.gif')   


    if message.content.lower().strip().startswith('.m lmao'):
       await message.channel.send('https://tenor.com/bh5zk.gif')    


    if message.content.lower().strip().startswith('.m ew'):
       await message.channel.send('https://tenor.com/4lKJ.gif')    


    if message.content.lower().strip().startswith('.m roach'):
       await message.channel.send('https://tenor.com/992S.gif')  


    if message.content.lower().strip().startswith('.ian'):
       await message.channel.send('check out <@429723963157905410>\'s stream! https://twitch.tv/ianxian') 


    if message.content.lower().strip().startswith('.ad'):
       await message.channel.send('*The Men I Trust Discord*' 
      'Our community is the largest supporting discord in regards to the Indie Band "Men I Trust." We have an extremely welcoming community, where **everyone** is welcome! Come check us out! We love you, A Lot. https://discord.gg/menitrust https://tinyurl.com/2fska59c') 


client.run(os.getenv("DISCORD_TOKEN"))
