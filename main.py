import discord
import os
import random
from random import choice
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix="!", help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"i am the best bot"))
    
print("Bot Is Online")

@client.command()
async def help(ctx):
  e = discord.Embed(
  title="Commands For Me!",
  description="howgay, simprate, pp, coinflip, randomnumber"),
  color=0xFF0000
  await ctx.send(embed=e)
  
  @client.command()
async def howgay(ctx):
    x = random.randint(0,100)
    e = discord.Embed(
  title="Gay Rate",
  description=f"{x}% Gay",
    color=0xFF0000
    await ctx.send(embed=e)
      
@client.command()
async def simprate(ctx):
    x = random.randint(0,100)
    e = discord.Embed(
  title="Simp Rate",
  description=f"{x}% Simp",
    color=0xFF0000
    await ctx.send(embed=e)
      
@client.command()
async def pp(ctx):
    x = random.randint(1,10)
    e = discord.Embed(
  title="Calculated PP",
  description=f"8{'='*random.randint(1, 10)}D",
    color=0xFF0000
    )
    await ctx.send(embed=e)

determine_flip = [1, 0]

@client.command()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!", color=0xFF0000)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!", color=0xFF0000)
        await ctx.send(embed=embed)

@client.command()
async def randomnumber(ctx):
    x = random.randint(1,100)
    e = discord.Embed(
  title="Random Number Is",
  description=f"{x}%",
    color=0xFF0000
    await ctx.send(embed=e)
      
client.run("TOKEN")
