import discord
from discord.ext import commands
TOKEN = 'your_token_here'
client = discord.Client()

@client.event
async def on_ready():
    print("I am a vipul bot")

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if(message.author==client.user):
        return
    elif(message.content.startswith("hello") and ('kanak' in message.content or 'bot' in message.content)):
        await message.channel.send("Hello, I am Kanak bot. I am a noob gamer")
    elif("who are you" in message.content or ("who is" in message.content and "kanak" in message.content)):
        await message.channel.send("I am son of " + str(message.author)[:-5])
@client.event
async def on_message_delete(message):
    await message.channel.send("Koi ni beta " + str(message.author)[:-5] + " karle message delete")

client.run(TOKEN)
