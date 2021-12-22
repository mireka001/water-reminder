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

    if message.content.startswith('.m hello'):
        await message.channel.send('hi hi!')


    if message.author == client.user:
        return

    if message.content.startswith('.m i love you'):
        await message.channel.send('bitch, im a bot :(')

    if message.author == client.user:
        return

    if message.content.startswith('.m hug'):
        await message.channel.send('https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif')
    
     
    if message.content.startswith('.m kissy'):
        await message.channel.send('https://media.giphy.com/media/iJDthUh1cvaF2/giphy.gif')
   
    if message.content.startswith('.m codenames'):
        await message.channel.send('https://codenames.game/')  

    if message.content.startswith('.m gartic phone'):
        await message.channel.send('https://garticphone.com/') 

    if message.content.startswith('.m secret hitler'):
        await message.channel.send('https://secrethitler.io/')

    if message.content.startswith('.m uno'):
        await message.channel.send('https://www.letsplayuno.com/')           
    if message.content.startswith('.m scrabble'):
        await message.channel.send('https://www.pogo.com/games/scrabble/play') 

    if message.content.startswith('.m skribbl'):
        await message.channel.send('https://skribbl.io/')  
    
    if message.content.startswith('.m heart'):
        await message.channel.send('https://tenor.com/view/moti-hearts-gif-20367288') 
        
    if message.content.startswith('.m narwhale'):
        await message.channel.send('http://narwhale.io/')
       
    
    if message.content.startswith('.m somebody love me, for fucks sake why does nobody love me!'):
        await message.channel.send('sorry meme :( we all love you here!!! <3') 
        
    if message.content.startswith('.m meme'):
        await message.channel.send('we all love you here meme!!! <3')     
        
    if message.content.startswith('.m wink'):
        await message.channel.send('https://tenor.com/bNyLU.gif') 
        
    if message.content.startswith('.m youtube'):
       await message.channel.send('https://www.youtube.com/')
    
client.run(os.getenv("DISCORD_TOKEN"))
