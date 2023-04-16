import os
import random
import re
from datetime import datetime
import asyncio

import discord
import os.path
from datetime import datetime, timedelta

from custom import *


# -- BOT CONFIG-----------------------------------------------------------------------
# ====================================================================================
botcfg = {}
botcfg['home_channel'] = 'bot-commandos'
botcfg['guardian'] = 'Felikc'

# -- CLIENT SETUP --------------------------------------------------------------------
# ====================================================================================
with open("./secrets/discord_token", "r") as f:
    TOKEN = f.read()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
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
    # Lakomte -------------------------------------------------------------------------------
    LakomteUser = message.guild.get_member_named('LaKomte#1042')
    if LakomteUser in message.mentions:
        logtext = f'{message.author} - {message.channel.name}'
        Log(message, 'Lakomte', extra_info=logtext)

        # Get botguardian
        bot_guardian_user = message.guild.get_member_named(botcfg['guardian'])

        # deny self elevation
        if message.author.discriminator == LakomteUser.discriminator:
            await message.channel.send('Waarom tag je jezelf? :eyes:', reference=message.to_reference())
            return
        
        # Get time
        now = datetime.now() 
        dateformat = "%m/%d/%Y, %H:%M:%S"
        date_time = now.strftime(dateformat)         

        # Add line to trackrecord
        msgcont = message.content.replace("\n", "; ")
        msg = f'{date_time} - {message.author} - {msgcont}'
        appendfile('lakomte', msg)

        # Read number of lines in trackrecord
        with open('trackrecord/_lakomte.txt', 'r') as file:
            num = len(file.readlines())
        
        # Get status
        maxx = 10
        left = maxx - num

        # Let Felikc know what's up
        await dm(bot_guardian_user, f'Lakomte actie remaining: {left}. {logtext}')

        # Respond in channel
        if left > 0:
            text = f"{left} van {maxx} pings resterend voordat Lakomte mod rechten krijgt op deze server :flushed:"
            await message.channel.send(text, reference=message.to_reference())
        if left == 0:
            text = f"Bedankt voor je bijdrage, met deze ping krijgt Lakomte mod rechten, jij zal altijd herinnerd worden als het server lid dat dit mogelijk heeft gemaakt! :verwijfde_duim: "
            await message.channel.send(text, reference=message.to_reference())

        return


    # !say -------------------------------------------------------------------------------
    if message.content.startswith('!say '):
        r = await fupjotr(message)
        if r:
            return

        # repeat given text without the command prefix
        text = message.content[5:]

        Log(message, '!say', extra_info=text)
        await message.channel.send(text, reference=message.reference)

        # remove original message
        await message.delete()
        return

    # !offense -------------------------------------------------------------------------------
    if message.content.startswith('!cringe_dm'):
        r = await fupjotr(message)
        if r:
            return

        # dm message to refenced author
        refmsg = await message.channel.fetch_message(message.reference.message_id)
        
        Log(message, '!cringe_dm', extra_info=refmsg.author)
        await dm(refmsg.author, "", file=discord.File(r'files/offense.mp4'))

        # remove original message
        await message.delete()
        return        


    # !offense -------------------------------------------------------------------------------
    if message.content.startswith('!cringe'):
        r = await fupjotr(message)
        if r:
            return

        # dm message to refenced author
        refmsg = await message.channel.fetch_message(message.reference.message_id)
        
        Log(message, '!cringe', extra_info=refmsg.author)
        await message.channel.send("", file=discord.File(r'files/offense.mp4'), reference=message.reference)

        # remove original message
        await message.delete()
        return

    # Remove N messages (newest to oldest) -----------------------------------------------
    if message.content.startswith("!clean"):
        # get user felixc to let him know if people try to misuse the bot
        bot_guardian_user = message.guild.get_member_named(botcfg['guardian'])

        # test if user has manage_messages permission
        manage_messages = message.channel.permissions_for(message.author).manage_messages
        Log(message, '!clean', extra_info=manage_messages)
        if manage_messages == False:
            await message.channel.send(f"Computer says no :hot_face: {bot_guardian_user.mention}", reference=message.to_reference())
            return

        # get amount to delete
        arguments = message.content.split(' ')
        if len(arguments) != 2 or arguments[1].isdigit() == False:
            await message.channel.send("Je hebt het commando verkeerd gebruikt mijn beste, typ het zo: `!clean 2` (2 is het aantal berichten dat je wilt verwijderen).", reference=message.to_reference())
            return

        number = int(arguments[1]) + 1

        Log(message, '!clean', extra_info=f">clean {number}")
    
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
        r = await fupjotr(message)
        if r:
            return

        Log(message, '!valaan')
        ref = message.reference
        if ref is not None:
            await message.channel.send("Blaf blaf blaf! ```*struggle snuggle*```", reference=message.reference)
            return
        print("err: could not find ref", message.reference)


    if message.content == "!badonk":
        r = await fupjotr(message)
        if r:
            return

        Log(message, '!badonk-img')

        # send msg
        await message.channel.send(':sweat:', file=discord.File(r'files/badonk.png'))

        # remove command msg
        await message.delete()        
        return


    # Ik heb alle rode pillen die je wilde krijgen ---------------------------------------
    if message.content == "!redpill":
        r = await fupjotr(message)
        if r:
            return

        redpills = [
            ("Zalig, dit. Lekker met koptelefoon op aan het luisteren. :pray::wink:  https://www.youtube.com/watch?v=YRNKjQg6y-c", None),
            ("Inspiratie voor het weekend. https://www.youtube.com/watch?v=vpp5EXZZrgA", None),
            ("De hele show. Alvast een zalig begin, de rest moet ik nog kijken. Dit zal zeker weer nieuwe stellingen en discussies opleveren. https://www.youtube.com/watch?v=mthj2Z7xqvM", None),
            ("In de #multimedia staat genoeg om jezelf een hart mee onder de riem te steken in je vrije (geïnformeerde?) keuze.", None),
            ("Veel plezier! :thumbsup::thumbsup:", discord.File(r'files/Industrial-Society-and-Its-Future-Theodore-Kaczynski.pdf')),
        ]
        index = cycle('redpills', len(redpills) - 1)
        response = redpills[index]        

        Log(message, '!redpill', extra_info=f'{response[0]}, <{index}>')
        await message.channel.send(response[0], file=response[1], reference=message.to_reference())    
        return

    # Slimmerd commando ------------------------------------------------------------------
    if message.content == "!slim":
        r = await fupjotr(message)
        if r:
            return

        Log(message, '!slim')
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
        
        Log(message, '>remove-muilkorf')
        return


    # -- RESPOND TO CONTENTS (Global) ----------------------------------------------------
    # ====================================================================================
    mc = message.content.lower()

    # joteewaawee joteewaawee mkaddeshhhhhhh
    if "hugo de jonge" in mc:
        
        response = "Krijg ik al die vieze energie aan me server, bah."
        Log(message, '>jotewawe')
        await message.channel.send(response, reference=message.to_reference())
        await asyncio.sleep(4)
        response = "Joteewaawee joteewaawee mkaddeshhhhhhh."
        await message.channel.send(response)
        return

    # Baudaddy
    if mc == "baudet":
        await message.channel.send("", file=discord.File(r'files/baudaddy.mov'), reference=message.to_reference())
        return

    if "TRANSZORG NU".lower() in mc:
        await message.delete() 
        return

    # "Gewoon joods" ---------------------------------------------------------------------
    if ("joods" in mc or "joden" in mc or "jood" in mc) and "gewoon" in mc:
        response = "Je kunt niet \"gewoon joods\" zijn, als je wil kunnen we doorpraten in #gamer-zone. Volgensmij is het antisemitisch om te denken dat er menselijke rassen zijn."
        Log(message, '>joods')
        await message.channel.send(response, reference=message.to_reference())
        return

    # Respetto ---------------------------------------------------------------------------
    if message.content == "😂 😂":
        Log(message, '>respetto')
        await message.channel.send("ik houd van humor maar ik houd nog meer van respect", reference=message.to_reference())
        return
    
    # -- RESPOND TO CONTENTS -------------------------------------------------------------
    # ====================================================================================
    mc = message.content.lower()
    if (message.guild.name == 'TestServer' or message.channel.name == botcfg['home_channel']) and ((re.search('(?<![A-z])(bi)+(?![A-z])', mc) is not None) or 'flikker' in mc or 'lgbti' in mc or 'bisex' in mc or 'hetero' in mc or 'gay' in mc or 'homo' in mc):
        
        homo = [
            ("Niemand boeit het dat je bi bent, je kan er over ophouden.", None),
            (f"Niks mis met bi zijn, het is oke {message.author.name}.", None),
            ("Hoe eerder je het accepteert, hoe eerder je van jezelf kan gaan houden.", None),
            ("De eerste stap is toegeven dat je een probleem hebt.", None),
            ("Waar het hart van vol is loopt den mond van over.", None),
        ]
        index = cycle('homo', len(homo) - 1)
        response = homo[index]

        Log(message, '>homo', extra_info=f'{response} <{index}>')
        await message.channel.send(response[0], reference=message.to_reference())

    if message.channel.name == botcfg['home_channel']:

        # Negus ------------------------------------------------------------------------------
        if match(["neger","nigga","nigger"], mc) and not (match(["negeren"], mc)):
            Log(message, '>negus')
            await message.channel.send(reference=message.to_reference(), file=discord.File(r'files/tsktsk.mp4'))
            return

        if match(["n i g g a", "n e g e r", "n i g g e r"], mc):
            Log(message, '>negus_emoji')
            emoji = discord.utils.get(message.guild.emojis, name='7390pepethink')
            await message.add_reaction(emoji)
            return        
          
        # Pikkelikker --------------------------------------------------------------------
        if re.findall(r'\b(pik)\b', message.content, re.IGNORECASE):
            Log(message, '>pik')
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

            Log(message, '>badonkadonk', extra_info=f'warnings: {warnings}')

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

                Log(message, '>badonkadonk:muilkorf', extra_info=f'warnings: {warnings}')
                
            return   

        # Slimmerd -----------------------------------------------------------------------
        if len(message.content) > 150:
            y = random.randint(0, 5)
            if y == 0:
                response = "Ik heb met plezier je bijdragen gelezen en ik weet dat je een slimmerdje bent. \nSlimmerik. \nSlim" 
                Log(message, '>slimmerd-len')
                await message.channel.send(response, reference=message.to_reference())
                return      

        # Verkeerde kanaal ---------------------------------------------------------------
        if '?' in message.content and 'waarom' in message.content and message.channel.name != 'algemeen':
            response = "Interessante vraag. Even doorpraten in #algemeen alstjeblieft. Volgende keer kan je ook meteen daar de vragen stellen." 
            
            Log(message, '>vraag')
            await message.channel.send(response, reference=message.to_reference())
            return       

        # iWaldeeeeeeeeeeeeeeeen ---------------------------------------------------------
        if 'iwalden' in message.content.lower() and len(message.content) > 10:  
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
            index = cycle('phrases', len(phrases) - 1)
            response = phrases[index]

            Log(message, '>iwalden')
            await message.channel.send(response, reference=message.to_reference())
            return

    else:
        pass


# -- AT LOAD EVENT -------------------------------------------------------------------
# ====================================================================================
# Only used for debug atm
@client.event
async def on_ready():
    SimpleLog(msg=f'{client.user} is connected', function_name="on_ready()")

# -- CLIENT START --------------------------------------------------------------------
# ====================================================================================
# Start client
client.run(TOKEN)


# -- SUPPORTING FUNCTIONS ------------------------------------------------------------
# ====================================================================================
# Logging
def Log(message, function_name, extra_info=None, levelname="INFO"):
    msg = f'{message.guild.name}/{message.channel.name}/{function_name}, {message.author.name}, msg:"{message.content}"'
    if extra_info is not None:
        msg += f' [{extra_info}]'
    print(f'[{levelname}] {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - {msg}')

def SimpleLog(msg='', function_name="", levelname="INFO"):
    msg = f'{function_name}, msg:"{msg}"'
    print(f'[{levelname}] {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} - {msg}')   

SimpleLog(msg="Test logger", function_name="script") 

async def fupjotr(message):
    banlist = ['']
    if message.author.name in banlist:
        await message.channel.send(f"Jij gaat mij niet vertellen wat ik moet doen vriend.", reference=message.to_reference())
        return True
    return False