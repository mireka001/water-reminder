import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().strip().startswith('.m hello'):
        await message.channel.send('hi hi! https://tenor.com/7MVe.gif')


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
   
    if message.content.lower().strip().startswith('.m codenames'):
        await message.channel.send('https://codenames.game/')  

    if message.content.lower().strip().startswith('.m gartic phone'):
        await message.channel.send('https://garticphone.com/') 

    if message.content.lower().strip().startswith('.m secret hitler'):
        await message.channel.send('https://secrethitler.io/')

    if message.content.lower().strip().startswith('.m uno'):
        await message.channel.send('https://www.letsplayuno.com/')           
    if message.content.lower().strip().startswith('.m scrabble'):
        await message.channel.send('https://www.pogo.com/games/scrabble/play') 

    if message.content.lower().strip().startswith('.m skribbl'):
        await message.channel.send('https://skribbl.io/')  
    
    if message.content.lower().strip().startswith('.m heart'):
        await message.channel.send('https://tenor.com/view/moti-hearts-gif-20367288') 
        
    if message.content.lower().strip().startswith('.m narwhale'):
        await message.channel.send('http://narwhale.io/')
       
    
    if message.content.lower().strip().startswith('.m somebody love me, for fucks sake why does nobody love me!'):
        await message.channel.send('sorry meme :( we all love you here!!! <3') 
        
    if message.content.lower().strip().startswith('.m meme'):
        await message.channel.send('we all love you here meme!!! <3')     
        
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

    if message.content.lower().strip().startswith('.apple music'):
       await message.channel.send('https://music.apple.com/login')
    
    if message.content.lower().strip().startswith('.m i hate you'):
       await message.channel.send('https://tenor.com/9eCN.gif') 

    if message.content.lower().strip().startswith('.m sad'):
       await message.channel.send('https://tenor.com/btf9K.gif')   

    if message.content.lower().strip().startswith('.m lmao'):
       await message.channel.send('https://tenor.com/bh5zk.gif')    

    if message.content.lower().strip().startswith('.m ew'):
       await message.channel.send('https://tenor.com/4lKJ.gif')    

    if message.content.lower().strip().startswith('.m water reminder'):
       await message.channel.send('plz drink some water <3 <@&906298179476135936> https://tenor.com/bnNG6.gif')    
    if message.content.lower().strip().startswith('.m food reminder'):
       await message.channel.send('plz eat some food <3 <@&906298179476135936> https://tenor.com/bLtpk.gif') 

    if message.content.lower().strip().startswith('.m babies reminder <3'):
       await message.channel.send('plz remember to drink some water <3 you deserve it.  <@901321594763350097> https://tenor.com/bnNG6.gif')    
    if message.content.lower().strip().startswith('.m snacko reminder <3 '):
       await message.channel.send('plz remember to eat some food <3 you need it. <@901321594763350097> https://tenor.com/bLtpk.gif') 
    
    if message.content.lower().strip().startswith('.m cockroach calisthenics'):
       await message.channel.send('https://youtu.be/KqNrAOrReNg')

    if message.content.lower().strip().startswith('.m roach'):
       await message.channel.send('https://tenor.com/992S.gif')  

    if message.content.lower().strip().startswith('.m happy wheels'):
       await message.channel.send('https://totaljerkface.com/')    
    if message.content.lower().strip().startswith('.m checkers'):
       await message.channel.send('https://www.247checkers.com/')    
    if message.content.lower().strip().startswith('.m chess'):
       await message.channel.send('https://lichess.org/')    
    if message.content.lower().strip().startswith('.m geoguessr'):
       await message.channel.send('https://www.geoguessr.com/')    
    if message.content.lower().strip().startswith('.m spotify'):
       await message.channel.send('https://accounts.spotify.com/en/status')    
    if message.content.lower().strip().startswith('.m twitter'):
       await message.channel.send('https://twitter.com/login?lang=en')    
    if message.content.lower().strip().startswith('.m reddit'):
       await message.channel.send('https://www.reddit.com/login/')    
    if message.content.lower().strip().startswith('.m instagram'):
       await message.channel.send('https://www.instagram.com/accounts/login/')    
    if message.content.lower().strip().startswith('.m whatsapp web'):
       await message.channel.send('https://web.whatsapp.com/')    
    if message.content.lower().strip().startswith('.m amazon'):
       await message.channel.send('https://www.google.com/aclk?sa=L&ai=DChcSEwiSwO3c1Pb0AhUIRYYKHRT6BLUYABAAGgJ2dQ&ae=2&sig=AOD64_3IB-j8Votf2GHeK8-xdoel4umm-A&q&adurl&ved=2ahUKEwjjxOTc1Pb0AhW9SDABHbFGC7YQ0Qx6BAgDEAE')    
    if message.content.lower().strip().startswith('.m cashapp'):
       await message.channel.send('https://cash.app/')    
    if message.content.lower().strip().startswith('.m facebook'):
       await message.channel.send('https://www.facebook.com/')    
    if message.content.lower().strip().startswith('.m life360'):
       await message.channel.send('https://app.life360.com/login?utm_source=GAds&utm_medium=paidsearch&utm_campaign=Web_GADS_Brand_Beta&utm_adgroup=null&utm_content=null&utm_term=null')    
    if message.content.lower().strip().startswith('.m google'):
       await message.channel.send('https://www.google.com/')    
    if message.content.lower().strip().startswith('.m discord'):
       await message.channel.send('https://discord.com/login')    
    if message.content.lower().strip().startswith('.m discord developer'):
       await message.channel.send('https://discord.com/login?redirect_to=%2Fdevelopers')    
    if message.content.lower().strip().startswith('.m help'):
       await message.channel.send('Vocal response commands; \n\n.m hello \n.m hugs \n.m i love you \n.m kissy \n.m handshake \n.m wave\n.m ick \n.m i hate you\n.m hugs \n.m loser\n.m wow \n.m shocked \n.m lmao\n.m sad \n.m water reminder \n.m food reminder\n.m cockroach calisthenics\n.m cockroach\n\nGame commands;\n.m codenames\n.m gartic phone \n.m secret hitler\n.m uno\n.m scrabble\n.m skribbl \n.m narwhale\n.m happy wheels \n.m checkers\n.m chess\n.m geoguessr\n\nPlatform commands;\n.m youtube\n.m spotify \n.m apple music\n.m twitter\n.m reddit\n.m instagram\n.m WhatsApp web \n.m amazon\n.m cashapp \n.m facebook\n.m life360 \n.m google\n.m discord developer\n.m discord\n\nBot commands;\n.m help')
client.run(os.getenv("DISCORD_TOKEN"))
