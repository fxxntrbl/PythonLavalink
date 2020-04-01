import discord
import asyncio
from discord.ext import commands
from config import owners

def is_owner():
    async def predicate(ctx):
        return ctx.author.id in owners
    return commands.check(predicate)

class Owners (commands.Bot) :
   def __init__ (self, bot):
      self.bot = bot

   @commands.command ()
   @is_owner()
   async def load (self, ctx, module) :
      self.bot.load_extension(module)