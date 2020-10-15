import discord
from discord.ext import commands
import bot

@client.event()
async def on_member_join(ctx):
   await ctx.channel.send(f'{msg}')
