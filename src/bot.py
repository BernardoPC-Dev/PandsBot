import discord
from discord.ext import commands
from random import randint

client = commands.Bot(command_prefix = '/')

# Ping Command

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency * 1000}ms')

# Roll Command

@client.command()
async def roll(ctx, *, n):
    number = randint() * n
    await ctx.send(f'Eu rolei {n} e caiu o número {number}!')

# Clear Command

@client.command()
async def clear(ctx, msgs=1):
    await ctx.channel.parge(limit-msgs)

# Prefix Command

@client.command()
async def prefix(ctx):
    await ctx.send(f'Meu prefixo é {client}')

# Say Command

@client.command()
async def say(ctx, arg):
    await ctx.send(f'{arg}')

# Kick Command

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"O usuário foi expulso por `{reason}`!")

# Ban Command

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"O usuário foi banido por `{reason}`!")

# Unban Command

@client.command()
async def unban(ctx, member : discord.Member):
    await member.unban()
    await ctx.send("O banimento do usuário foi retirado!")

# Run Bot

client.run('Token que eu não vou revelar uwu')
