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
# Add Perm
@client.command()
async def clear(ctx, msgs=1):
    await ctx.channel.parge(limit-msgs)

# Prefix Command

@client.command()
async def setprefix(ctx, nv-prefixo):
    client = commands.Bot(command_prefix = nv-prefixo)
    await ctx.send(f'Prefixo alterado para: {nv-prefixo} com sucesso!')
# Say Command
# Add Perm
@client.command()
async def say(ctx, arg):
    await ctx.send(f'{arg}')

# Kick Command
# Add Perm
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"O usuário foi expulso por `{reason}`!")

# Ban Command
# Add Perm
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"O usuário foi banido por `{reason}`!")

# Unban Command
# Add Perm
@client.command()
async def unban(ctx, member : discord.Member):
    await member.unban()
    await ctx.send("O banimento do usuário foi retirado!")

# Create-Channel Command
# Add Perm
@client.command()
async def create-channel(ctx, channel):
    await guild.create_text_channel(channel)
    await ctx.send("Canal criado!")

# Nickname Command
# Add Perm
@client.command()
async def nickname(ctx, nickname):
    await member.edit(nickname)
    await ctx.send("O apelido foi alterado!")

# Clear-Reactions
# Add Perm
@client.command()
async def clear-reactions(ctx, message)
    await message.clear_reactions()
    await ctx.send("As reações da mensagem foram apagadas!")

# Softsay Command
# Add Perm
@client.command()
async def softsay(ctx, channel, *, msg):
    await ctx.channel.send(f'{msg}')
    await ctx.send(f'Mensagem enviada em {channel}!')

# Star Secret-Command

@client.command()
async def star(ctx):
    await ctx.send('Você é uma estrela! :star:!')
    await ctx.add_reaction(':star:')

# Ask Command

@client.command()
async def ask(ctx, question):
    resp = (':+1:', ':-1:')
    rdm = randint(1, 2)
    await ctx.send(f'Você perguntou: {question}, e a resposta é: {resp[rdm]}!')

# Run Bot

client.run('Token que eu não vou revelar uwu')
