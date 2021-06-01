# bot.py
import os
import random
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    guild = discord.utils.get(client.guilds, name=GUILD)

    if message.author == client.user:
        return

    if re.findall(r'\b(pik)\b', message.content, re.IGNORECASE):
        await message.channel.send("Pik?", reference=message.to_reference())
        return
    

    if message.content == "!valaan":
        ref = message.reference
        if ref is not None:
            await message.channel.send("Blaf blaf blaf! ```*struggle snuggle*```", reference=ref)
            return
        print("err: could not find ref", message.reference)

    y = random.randint(0, 4)
    if message.content == "!redpill":
        if y == 0:
            await message.channel.send("Zalig, dit. Lekker met koptelefoon op aan het luisteren. :pray::wink:  https://www.youtube.com/watch?v=YRNKjQg6y-c", reference=message.to_reference())     
        elif y == 1:
            await message.channel.send("Inspiratie voor het weekend. https://www.youtube.com/watch?v=vpp5EXZZrgA", reference=message.to_reference())     
        elif y == 2:
            await message.channel.send("De hele show. Alvast een zalig begin, de rest moet ik nog kijken. Dit zal zeker weer nieuwe stellingen en discussies opleveren. https://www.youtube.com/watch?v=mthj2Z7xqvM", reference=message.to_reference())   
        elif y == 3:
            await message.channel.send("In de #multimedia staat genoeg om jezelf een hart mee onder de riem te steken in je vrije (geïnformeerde?) keuze.", reference=message.to_reference())   
        else:            
            await message.channel.send("Veel plezier! :thumbsup::thumbsup:", file=discord.File(r'files/Industrial-Society-and-Its-Future-Theodore-Kaczynski.pdf'), reference=message.to_reference())    
        return

    y = random.randint(0, 2)
    print(message.guild.name, message.channel.name, i)
    if y == 0: #and message.guild.name == "TestServer":
        phrases = [
            "Interessant! Bedankt voor je bijdrage.",
            "Neem het met een korrel zout. Tegelijk: ik twijfel grondig aan deze stelling.",
            "Wat een zwendel.",
            "Lieve help.",
            "Ik heb wel zitten te genieten af en toe.",
            "Heel interessant.",
            "Ja, vreemd hoor! Dank voor het delen",
            "Best eng eigenlijk.",
            "Dit zal geen WO3 ontketenen.",
            "Over lessen leren uit het verleden gesproken... ",
            "Ja. Wel een beetje kort door de bocht",
        ]       
        response = random.choice(phrases) 
        print(">replied", message.guild.name, message.channel.name, response)
        await message.channel.send(response, reference=message.to_reference())
        return


client.run(TOKEN)
