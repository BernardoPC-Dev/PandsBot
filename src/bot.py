import discord
from discord.ext import commands
from random import randint

client = commands.Bot(command_prefix = '/')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round{client.latency * 1000}}ms')

@client.command()
async def roll(ctx, *, n):
    number = randint() * n
    await ctx.send(f'Eu rolei {n} e caiu o número {number}!')

@client.command()
async def clear(ctx, msgs=1):
    await ctx.channel.parge(limit-msgs)

@client.command()
async def prefix(ctx):
    await ctx.send(f'Meu prefixo é {client}')

@clientt.command()
async def say(ctx, arg):
    await ctx.send(f'{arg}')

client.run('NzY0NjU1OTExNjMzMDI3MDky.X4JbTw._nFs91rqmWBnzEi8tDgIr94LyQc')
