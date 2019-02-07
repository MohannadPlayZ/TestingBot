import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'A New Wild Member Appeared')
    print('Sent message to ' + member.name)
    await client.change_presence(game=Game(name='Playing Hi'))
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello,I Hope You Will like Our Server')
    print('Sent message to ' + member.name)
    await client.change_presence(game=Game(name='Playing Fortnite'))
    await client.change_presence(game=Game(name='fortnite'))
    print('Ready') 

@client.event
async def on_message(message):
    if ('heck') in message.content:
       await client.delete_message(message)
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('tf') in message.content:
       await client.delete_message(message)
   
bot.run('NTQzMTE4MzUyNDExNzg3MzE0.Dz357Q.spcGoern0vZQszFOQYgxo5KPHN8')