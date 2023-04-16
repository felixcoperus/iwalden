# iWalden
De meme, de legende.

## Installatie
```bash
pip install -U discord.py

git clone git@github.com:felixcoperus/iwalden.git
cd iwalden/
touch .env
```

Put the following in .env:
```
DISCORD_TOKEN={token}
```


## Run
```
python bot.py
```

## Run in background
```bash
nohup python -u /home/<user>/git/iwalden/bot.py > program.out 2>&1 &
```

Or when in venv:

```bash
nohup /path/to/venv/bin/python -u /home/<user>/git/iwalden/bot.py > program.out 2>&1 &
```
