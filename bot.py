# bot.py
import os
import random
import re

import discord
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# Only used for debug atm
@client.event
async def on_ready():
    print(
        f'{client.user} is connected'
    )

@client.event
async def on_message(message):
    # Init
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    # Don't respond to self to avoid endless loops
    if message.author == client.user:
        return

    # ------------------------------- content-based ---------------------------------------------------
    # Pikkelikker
    if re.findall(r'\b(pik)\b', message.content, re.IGNORECASE):
        print(date_time, ">pik", message.guild.name, message.channel.name)
        await message.channel.send("Pik?", reference=message.to_reference())
        return

    # Respetto
    if message.content == "😂 😂":
        print(date_time, ">respetto", message.guild.name, message.channel.name)
        await message.channel.send("ik houd van humor maar ik houd nog meer van respect", reference=message.to_reference())
        return

    # gewoon joods
    mc = message.content
    if ("joods" in mc or "joden" in mc or "jood" in mc) and "gewoon" in mc:
        response = "Je kunt niet \"gewoon joods\" zijn, als je wil kunnen we doorpraten in #gamer-zone. Volgensmij is het antisemitisch om te denken dat er menselijke rassen zijn."
        print(date_time, ">joods", message.guild.name, message.channel.name)
        await message.channel.send(response, reference=message.to_reference())
        return
    
    # ------------------------------- commandos --------------------------------------------------------
    # Trucje
    if message.content == "!valaan":
        print(date_time, ">attack", message.guild.name, message.channel.name)
        ref = message.reference
        if ref is not None:
            await message.channel.send("Blaf blaf blaf! ```*struggle snuggle*```", reference=ref)
            return
        print("err: could not find ref", message.reference)

    # Ik heb alle rode pillen die je wilde krijgen
    y = random.randint(0, 4)
    if message.content == "!redpill":
        print(date_time, ">redpill", message.guild.name, message.channel.name, y)
        if y == 0:
            await message.channel.send("Zalig, dit. Lekker met koptelefoon op aan het luisteren. :pray::wink:  https://www.youtube.com/watch?v=YRNKjQg6y-c", reference=message.to_reference())     
        elif y == 1:
            await message.channel.send("Inspiratie voor het weekend. https://www.youtube.com/watch?v=vpp5EXZZrgA", reference=message.to_reference())     
        elif y == 2:
            await message.channel.send("De hele show. Alvast een zalig begin, de rest moet ik nog kijken. Dit zal zeker weer nieuwe stellingen en discussies opleveren. https://www.youtube.com/watch?v=mthj2Z7xqvM", reference=message.to_reference())   
        elif y == 3:
            await message.channel.send("In de #multimedia staat genoeg om jezelf een hart mee onder de riem te steken in je vrije (geïnformeerde?) keuze.", reference=message.to_reference())   
        elif y == 4:            
            await message.channel.send("Veel plezier! :thumbsup::thumbsup:", file=discord.File(r'files/Industrial-Society-and-Its-Future-Theodore-Kaczynski.pdf'), reference=message.to_reference())    
        return

    
    
    # ------------------------------- 2de rangs memerij -----------------------------------------------------
    # Verkeerde kanaal
    print(message.guild.name, message.channel.name) # debug
    if '?' in message.content and 'waarom' in message.content and message.channel.name != 'algemeen':
        response = "Interessante vraag. Even doorpraten in #algemeen alstjeblieft. Volgende keer kan je ook meteen daar de vragen stellen." 
        await message.channel.send(response, reference=message.to_reference())
        print(date_time, ">vraag", message.guild.name, message.channel.name, response)
        return      

    # Slimmerd
    if len(message.content) > 150:
        y = random.randint(0, 5)
        if y == 0:
            response = "Ik heb met plezier je bijdragen gelezen en ik weet dat je een slimmerdje bent. \nSlimmerik. \nSlim" 
            await message.channel.send(response, reference=message.to_reference())
            print(date_time, ">slimmerd", message.guild.name, message.channel.name, response)
            return



    # ------------------------------- random responses -----------------------------------------------------
    # Random reacties eens in de x posts
    y = random.randint(0, 20)
    print(date_time, message.guild.name, message.channel.name, y)
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
            "Waarom als ik even mag vragen? (Gekke maar belangrijke vraag)",
        ]       
        response = random.choice(phrases) 
        print(date_time, ">replied", message.guild.name, message.channel.name, response)
        await message.channel.send(response, reference=message.to_reference())
        return



# Start client
client.run(TOKEN)
