import os
import random
import re

import discord
from dotenv import load_dotenv
import os.path
from datetime import datetime, timedelta

from custom import warn, dm


# -- BOT CONFIG-----------------------------------------------------------------------
# ====================================================================================
botcfg = {}
botcfg['home_channel'] = 'bot-commandos'
botcfg['guardian'] = 'Felikc'

# -- CLIENT SETUP --------------------------------------------------------------------
# ====================================================================================
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)   

# -- MESSAGE EVENT -------------------------------------------------------------------
# ====================================================================================
@client.event
async def on_message(message):
    # Init
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    # Don't respond to self to avoid endless loops
    if message.author == client.user:
        return


    # -- GLOBAL COMMANDS -----------------------------------------------------------------
    # ====================================================================================

    # !say -------------------------------------------------------------------------------
    if message.content.startswith('!say '):
        # repeat given text without the command prefix
        text = message.content[5:]
        await message.channel.send(text, reference=message.reference)

        # remove original message
        await message.delete()
        return
            

    # Remove N messages (newest to oldest) -----------------------------------------------
    if message.content.startswith("!clean"):
        # get user felixc to let him know if people try to misuse the bot
        bot_guardian_user = message.guild.get_member_named(botcfg['guardian'])

        # test if user has manage_messages permission
        manage_messages = message.channel.permissions_for(message.author).manage_messages
        print(manage_messages)
        if manage_messages == False:
            await message.channel.send(f"Computer says no :hot_face: {bot_guardian_user.mention}", reference=message.to_reference())
            return

        # get amount to delete
        arguments = message.content.split(' ')
        if len(arguments) != 2 or arguments[1].isdigit() == False:
            await message.channel.send("Je hebt het commando verkeerd gebruikt mijn beste, typ het zo: `!clean 2` (2 is het aantal berichten dat je wilt verwijderen).", reference=message.to_reference())
            return

        number = int(arguments[1]) + 1

        print(date_time, f">clear {number}", message.guild.name, message.channel.name, message.author.name)

        # get messages & delete
        messages = await message.channel.history(limit=number).flatten()
        for msg in messages:
            await msg.delete()

        # dm author
        await dm(message.author, f"Klaar met verwijderen van {number - 1} berichten in {message.channel.name}.")

        print("Done deleting messages.")
        return

    # Trucje -----------------------------------------------------------------------------
    if message.content == "!valaan":
        print(date_time, ">attack", message.guild.name, message.channel.name)
        ref = message.reference
        if ref is not None:
            await message.channel.send("Blaf blaf blaf! ```*struggle snuggle*```", reference=message.reference)
            return
        print("err: could not find ref", message.reference)



    # Ik heb alle rode pillen die je wilde krijgen ---------------------------------------
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

    # Slimmerd commando ------------------------------------------------------------------
    if message.content == "!slim":
        print(date_time, ">slim-command", message.guild.name, message.channel.name)
        ref = message.reference
        if ref is not None:
            # get referenced message
            oc_msg = await message.channel.fetch_message(message.reference.message_id)

            # remove command msg
            await message.delete()

            # respond to oc_msg
            slim = "Ik heb met plezier je bijdragen gelezen en ik weet dat je een slimmerdje bent. \nSlimmerik. \nSlim"
            await oc_msg.channel.send(slim, reference=ref)
            return
        print("err: could not find ref", message.reference)   

    # muilkorf verwijderen ---------------------------------------------------------------
    if message.content == "Sorry iWalden, ik zal geen badonkadonk meer zeggen" or ("sorry" in message.content.lower() and "walden" in message.content.lower()):
        # remove role
        roles = [x for x in await message.guild.fetch_roles() if x.name == "iMuilkorf"]
        await message.author.remove_roles(*roles, reason="gewoon een tof lid")

        # walden sausje
        await message.channel.send("Ik accepteer je excuses. Ik vind het jammer dat je ervan lijkt te genieten als leden van deze server zich ongemakkelijk of onprettig voelen, maar je bent een tof lid, en ik wil best mijn hand over mijn hart strijken voor zo een tof lid als jij :relieved:", reference=message.to_reference())
        
        print(date_time, ">removed muilkorf", message.author.name)
        return


    # -- RESPOND TO CONTENTS (Global) ----------------------------------------------------
    # ====================================================================================

    # "Gewoon joods" ---------------------------------------------------------------------
    mc = message.content
    if ("joods" in mc or "joden" in mc or "jood" in mc) and "gewoon" in mc:
        response = "Je kunt niet \"gewoon joods\" zijn, als je wil kunnen we doorpraten in #gamer-zone. Volgensmij is het antisemitisch om te denken dat er menselijke rassen zijn."
        print(date_time, ">joods", message.guild.name, message.channel.name)
        await message.channel.send(response, reference=message.to_reference())
        return

    # Respetto ---------------------------------------------------------------------------
    if message.content == "😂 😂":
        print(date_time, ">respetto", message.guild.name, message.channel.name)
        await message.channel.send("ik houd van humor maar ik houd nog meer van respect", reference=message.to_reference())
        return
    
    # -- RESPOND TO CONTENTS -------------------------------------------------------------
    # ====================================================================================
    if message.channel.name == botcfg['home_channel']:
          
        # Pikkelikker --------------------------------------------------------------------
        if re.findall(r'\b(pik)\b', message.content, re.IGNORECASE):
            print(date_time, ">pik", message.guild.name, message.channel.name)
            await message.channel.send("Pik?", reference=message.to_reference())
            return

        # badonkadonk --------------------------------------------------------------------
        if 'badonkadonk' in message.content.lower() or 'badonkabonk' in message.content.lower():
            # Setup
            author = message.author
            warning_type = 'badonkadonk'
            cooldown = timedelta(weeks=0, days=0, hours=2, minutes=0, seconds=0)

            # Find how many times the author has been warned for this error already
            warnings = warn(author.name, warning_type, cooldown)

            print(date_time, ">badonkadonk", message.author.name, warnings)

            # Define responses and pick right one
            responses = []
            responses.append(
                "Hier op deze server zitten best veel mensen met een warmbloedig hart. "
                "Mods, leden, echt veel mensen die je in het echt ook niet \"badonkadonk\" in hun gezicht zou zeggen als ze "
                "het over diepe dingen hebben, en hun best doen. \n"
                "Ik begrijp dat het even lollig was en ik neem je de meme daarom ook niet kwalijk.\n" 
                "Maar zou je hem na dit gesprek nog steeds plaatsen?"
            )
            responses.append(
                "Ik vind dit heel jammer."
            )       
            response = ":cry:"
            if warnings <= len(responses):
                response = responses[warnings - 1]

            # Send response to offending user
            await message.channel.send(response, reference=message.to_reference())

            # Give mute role when repeat offender
            if warnings > 1:
                # Give correct mute role
                roles = [x for x in await message.guild.fetch_roles() if x.name == "iMuilkorf"]
                await author.add_roles(*roles, reason="badonkabonk")

                # dm user voor instructies hoe te onmuilkorven
                await dm(message.author, "Ik ben heel teleurgesteld in jou. Als je \"Sorry iWalden, ik zal geen badonkadonk meer zeggen\" zegt in **#bot-commandos** vergeef ik het je. We kunnen allemaal leren van onze fouten.")

                print(date_time, ">muilkorf:badonkadonk", message.author.name, warnings)
                
            return   

        # Slimmerd -----------------------------------------------------------------------
        if len(message.content) > 150:
            y = random.randint(0, 5)
            if y == 0:
                response = "Ik heb met plezier je bijdragen gelezen en ik weet dat je een slimmerdje bent. \nSlimmerik. \nSlim" 
                await message.channel.send(response, reference=message.to_reference())
                print(date_time, ">slimmerd", message.guild.name, message.channel.name, response)
                return      

        # Verkeerde kanaal ---------------------------------------------------------------
        print(message.guild.name, message.channel.name) # debug
        if '?' in message.content and 'waarom' in message.content and message.channel.name != 'algemeen':
            response = "Interessante vraag. Even doorpraten in #algemeen alstjeblieft. Volgende keer kan je ook meteen daar de vragen stellen." 
            await message.channel.send(response, reference=message.to_reference())
            print(date_time, ">vraag", message.guild.name, message.channel.name, response)
            return       

        # iWaldeeeeeeeeeeeeeeeen ---------------------------------------------------------
        if 'iwalden' in message.content.lower():
            y = random.randint(0, 1)
            if y == 0:     
                phrases = [
                    "Neem het met een korrel zout. Tegelijk: ik twijfel grondig aan deze stelling.",
                    "Wat een zwendel.",
                    "Lieve help.",
                    "Best eng eigenlijk.",
                    "Dit zal geen WO3 ontketenen.",
                    "Over lessen leren uit het verleden gesproken... ",
                    "Ja. Wel een beetje kort door de bocht",
                    "Waarom als ik even mag vragen? (Gekke maar belangrijke vraag)",
                    'wollah tfoe, dacht ik, bitch ass cracka',
                ]       
                response = random.choice(phrases) 
                print(date_time, ">replied", message.guild.name, message.channel.name, response)
                await message.channel.send(response, reference=message.to_reference())
                return

    else:
        pass






# -- AT LOAD EVENT -------------------------------------------------------------------
# ====================================================================================
# Only used for debug atm
@client.event
async def on_ready():
    print(
        f'{client.user} is connected'
    )

# -- CLIENT START --------------------------------------------------------------------
# ====================================================================================
# Start client
client.run(TOKEN)


