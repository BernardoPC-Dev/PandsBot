import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print("Eu estou pronta!")

@client.event
async def on_member_join(member):
    print(f'{member} entrou no servidor! Divirta-se aqui!')

@client.event
async def on_member_remove(member):
    print(f'{member} saiu do servidor! Espero que ele volte logo...')

client.run('NzY0NjU1OTExNjMzMDI3MDky.X4JbTw._nFs91rqmWBnzEi8tDgIr94LyQc')
