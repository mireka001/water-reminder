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

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')
    
    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')  

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')
    
    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')

    if message.content.startswith(''):
        await message.channel.send('')           
client.run(('OTIyNzE5MjY0MzQxODk3Mjg3.YcFjRw.FMxK2nQ2G-uhrXWC_b7RKRff1Ds'))
