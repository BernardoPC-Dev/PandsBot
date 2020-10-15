import discord
from discord.ext import commands

@client.event()
async def on_member_join(ctx):
   await ctx.send(msg)
