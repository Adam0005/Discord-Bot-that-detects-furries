import discord

token = "PUT YOUR DISCORD BOT TOKEN HERE"
client = discord.Client()

@client.event
async def on_message(message):
    if "furries" in message.content.lower():
        await message.channel.send("Ohh NAHH BRUH :skull:  another furry.")
        await message.reply("Where did your dad go? :sob: ")

client.run(token) 
