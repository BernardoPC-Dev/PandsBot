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

@client.command()
async def say(ctx, arg):
    await ctx.send(f'{arg}')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send("O usuário foi expulso!")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send("O usuário foi banido!")

client.run('NzY0NjU1OTExNjMzMDI3MDky.X4JbTw._nFs91rqmWBnzEi8tDgIr94LyQc')
