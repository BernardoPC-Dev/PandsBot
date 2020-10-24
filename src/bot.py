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
@commands.has_permission(manage_messages=True)
async def clear(ctx, msgs=1):
    await ctx.channel.parge(limit-msgs)

# Prefix Command

@client.command()
@commands.has_permission(manage_server=True)
async def setprefix(ctx, nvprefixo):
    client = commands.Bot(command_prefix = nvprefixo)
    await ctx.send(f'Prefixo alterado para: {nv-prefixo} com sucesso!')

# Say Command

@client.command()
@commands.has_permission(manage_messages=True)
async def say(ctx, arg):
    await ctx.send(f'Comando em manutenção!')

# Kick Command

@client.command()
@commands.has_permission(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"O usuário foi expulso por `{reason}`!")

# Ban Command

@client.command()
@commands.has_permission(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"O usuário foi banido por `{reason}`!")

# Unban Command

@client.command()
@commands.has_permission(ban_members=True)
async def unban(ctx, member : discord.Member):
    await member.unban()
    await ctx.send("O banimento do usuário foi retirado!")

# CreateChannel Command

@client.command()
@commands.has_permission(manage_channels=True)
async def createchannel(ctx, channel):
    await guild.create_text_channel(channel)
    await ctx.send("Canal criado!")

# Nickname Command

@client.command()
@commands.has_permission(change_nickname=True)
async def nickname(ctx, nickname):
    await member.edit(nickname)
    await ctx.send("O apelido foi alterado!")

# ClearReactions

@client.command()
@commands.has_permission(manage_messages=True)
async def clearreactions(ctx, message)
    await message.clear_reactions()
    await ctx.send("As reações da mensagem foram apagadas!")

# Softsay Command

@client.command()
@commands.has_permission(manage_messages=True)
async def softsay(ctx, channel, *, msg):
    await ctx.channel.send(f'{msg}')
    await ctx.send(f'Mensagem enviada em {channel}!')

# Star Secret-Command

@client.command()
async def star(ctx):
    await ctx.send('Você é uma estrela! :star:!')
    await ctx.add_reaction(':star:')

# 8ball Command

@client.command()
async def 8ball(ctx, question):
    resp = (':+1:', ':-1:', 'Talvez', 'Provavelmente Sim', 'Provavelmente Não', 'Não sei'.)
    rdm = randint(0, 5)
    await ctx.send(f'{resp[rdm]}')

# Invite Command

@client.command()
async def invite(ctx):
    await ctx.send('Para me convidar para seu servidor, clique no link abaixo e leia o README.md dela.\n\n https://github.com/bernardopc-dev/PandsBot')

# Pin Command

@client.command()
@commands.has_permission(manage_messages=True)
async def pin(ctx, id):
    await message.pin(id)
    await ctx.send('Mensagem fixada!')

# Unpin Command

@client.command()
@commands.has_permission(manage_messages=True)
async def unpin(ctx, msg):
    await message.unpin(msg)
    await ctx.send('Mensagem desfixada!')

# Coinflip Command

@client.command()
async def coinflip(ctx):
    coin = randint(0, 1)
    lados = ["Cara", "Coroa"]
    await ctx.send(f':coin: {lados[coin]}!')
# Run Bot

client.run('Token que eu não vou revelar uwu')
