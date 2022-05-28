import discord
from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_ready():
    print(f"rodando no bot {bot.user}")
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("OTgwMTY5NTEzNDYwOTY5NTQz.G-C-71.zTP6ILLBMLQIr6u3GC3J_OcrhrrnDdV8I9NOMA")

