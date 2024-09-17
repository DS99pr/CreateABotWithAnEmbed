# i must admit that I literally copied this code from the previous repository, and modified it (named "CreateAnAvatarBot")

import discord # "pip install discord" or "conda install discord"
from discord.ext import commands

intents = discord.Intents.default() # setting the intents the bot will be able to use, check it in the Discord Developers Portal so that the bot can send messages, etc.
intents.message_content = True # allowing the bot to send messages

bot = commands.Bot(
  command_prefix="?", # the "command_prefix" parameter is the prefix of our commands
  intents=intents # assign intents to the bot
) # creating a bot instance, it is responsible for the application

@bot.event # decorator "@bot.event" allows you to listen for events
async def on_ready(): # we use an asynchronous "on_ready" function, it is executed when the bot is ready
   print("bot is ready") # sending a log, you can do anything else here, but if you want to do something related to the Discord API, use "await" before the command

embed = discord.Embed(
  title="Title of my embed", # set the title of the embed
  description="Description of my embed", # set the description of the embed
  color=discord.Colour.red() # set a color of embed, you can also give "blue" or "green", and other colors, or just use hex
) # creating an Embed instance

@bot.command(name="embed") # creating a command called "embed", it will be called like this: "?embed"
async def embedCommand(ctx: commands.Context): # for the explanation of "commands.Context" check the documentation discord.py, or go to my repository called "CreateAPrefixCommandBot"
   await ctx.send(embed=embed) # sending embed to channel
   # after executing the "?embed" command, the bot responds with that embed, if it has "message_content" intentions assigned.

@bot.run("token") # replace the "token" with your token from the "Bot" tab in the Discord Developers Portal, and give it here (as a string), remember not to share it with ANYONE
