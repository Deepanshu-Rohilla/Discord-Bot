import discord
from discord.ext import commands
TOKEN = 'YOUR TOKEN HERE'
client = commands.Bot(command_prefix = 'vipul')

@client.event
async def on_ready():
    print("I am a vipul bot")
client.run(TOKEN)
