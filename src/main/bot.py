import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print("Eu estou pronta!")

client.run('NzY0NjU1OTExNjMzMDI3MDky.X4JbTw._nFs91rqmWBnzEi8tDgIr94LyQc')
