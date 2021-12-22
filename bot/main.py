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

    if message.content.startswith('hello'):
        await message.channel.send('hi hi!')


    if message.author == client.user:
        return

    if message.content.startswith('i love you'):
        await message.channel.send('bitch, im a bot :(')

    if message.author == client.user:
        return

    if message.content.startswith('pls hug'):
        await message.channel.send('https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif')
    
     
    if message.content.startswith('pls kissy'):
        await message.channel.send('https://media.giphy.com/media/iJDthUh1cvaF2/giphy.gif')
   
    if message.content.startswith('pls codenames'):
        await message.channel.send('https://codenames.game/')  

    if message.content.startswith('pls gartic phone'):
        await message.channel.send('https://garticphone.com/') 

    if message.content.startswith('pls secret hitler '):
        await message.channel.send('https://secrethitler.io/')

    if message.content.startswith('pls uno'):
        await message.channel.send('https://www.letsplayuno.com/')           
    if message.content.startswith('pls scrabble'):
        await message.channel.send('https://www.pogo.com/games/scrabble/play') 

    if message.content.startswith('pls skribbl'):
        await message.channel.send('https://skribbl.io/')  
    
    if message.content.startswith('pls heart'):
        await message.channel.send('https://tenor.com/bNJH7.gif')   
client.run(os.getenv("DISCORD_TOKEN"))
