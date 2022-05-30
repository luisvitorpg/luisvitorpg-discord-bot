import discord
from discord.ext import commands

client = commands.Bot("!")

@client.event
async def on_ready():
  print(f"Estou pronto! rodando no bot {bot.user}")

@client.command(name="ping")
async def ping(ctx):
  await ctx.send("Pong!")

@client.command(name="twitch")
async def twitch(ctx):
  await ctx.send("minha twitch: https://twitch.tv/thetannereel")

@client.command(name="rickroll")
async def rickroll(ctx):
  await ctx.send("Rick Roll! https://bit.ly/39NAz2s")
@client.command()
async def RJ(ctx):
  await ctx.send("a capital de RJ e Rio de Janeiro")
@client.command()
async def SP(ctx):
  await ctx.send("a capital de SP e Sao Paulo")
@client.command()
async def GO(ctx):
  await ctx.send("a capital de GO e Goiania")

client.run('OTgwMTY5NTEzNDYwOTY5NTQz.GY6boi.Xqjc-jQICqF5eUE3wvQP7dMewTa9MmToGHR0Lg')
