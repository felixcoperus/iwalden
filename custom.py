import os.path
from datetime import datetime, timedelta

def warn(author_name, warn_type, cooldown):
    ''' usage:  
            cooldown = timedelta(weeks=0, days=0, hours=0, minutes=0, seconds=10)
            warnings = warn(message.author.name, 'badonkabonk', cooldown) '''

    # input
    filename = f'trackrecord/_{warn_type}.txt' 
    #output
    warnings = 1 

    # init
    now = datetime.now() 
    dateformat = "%m/%d/%Y, %H:%M:%S"
    date_time = now.strftime(dateformat)       

    # Get existant warnings
    lines = []
    if os.path.exists(filename):
        with open(filename) as file:
            lines = file.readlines()

    # - remove cooldowned warnings
    # - count how many times the author has been warned already
    # - write new warning
    with open(filename, 'w') as file:
        for line in lines:
            # Test if warning in file is old enough to be removed
            warning_datetime, warning_author = [x.strip() for x in line.split(';')]
            datetime_dif = now - datetime.strptime(warning_datetime, dateformat)
            if datetime_dif <= cooldown:
                # Not old enough, write back to file
                file.write(line)

                # increment output warning if same author as current
                if warning_author == author_name:
                    warnings += 1
    
        # Write new warning
        file.write(f'{date_time}; {author_name}\n')

        # Output
        return warnings

async def dm(user, msg_str, file=None):
    ''' usage: dm(message.author, "REEEE") '''

    # Ensure dm_channel exists
    dm_channel = user.dm_channel
    if dm_channel is None:
        dm_channel = await user.create_dm()

    await dm_channel.send(msg_str, file=file)

def set_state(key, value):
    filename = f'trackrecord/_{key}.txt'
    with open(filename, 'w') as file:
        file.write(str(value))

def cycle(key, maximum):
    filename = f'trackrecord/_{key}.txt'

    # read
    number = 0
    lines = []
    if os.path.exists(filename):
        with open(filename) as file:
            lines = file.readlines()  
        number = int(lines[0]) 

    # inc
    number += 1
    if number > maximum:
        number = 0

    with open(filename, 'w') as file:
        file.write(str(number))

    return number

def match(matchlist, message_content):
    for matchstring in matchlist:
        if matchstring in message_content:
            return True
    return False