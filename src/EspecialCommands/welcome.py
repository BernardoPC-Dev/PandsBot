import discord
from discord.ext import commands
import bot

@client.command()
@commands.has_permissons(manage_server=True)
async def setwelcome(ctx, channel, msg):
   
   @client.event()
   async def on_member_join(ctx):
      await ctx.channel.send(f'{msg}')
