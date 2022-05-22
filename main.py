import discord
from discord.ext import commands
import random
bot = commands.Bot("!")

@bot.event
async def on_ready():
  print(f"Estou pronto! rodando no bot {bot.user}")

@bot.command(name="ping")
async def ping(ctx):
  await ctx.send("Pong!")

@bot.command(name="twitch")
async def twitch(ctx):
  await ctx.send("minha twitch: https://twitch.tv/thetannereel")

@bot.command(name="rickroll")
async def rickroll(ctx):
  await ctx.send("Rick Roll! https://bit.ly/39NAz2s")
bot.run('OTc3NTQ0NDU2MjI2MDkxMDM4.GQGNzi.w2ZzSQeIc1k2eErpg1dv3fVM7dZ5Jcj1z-akq4')
