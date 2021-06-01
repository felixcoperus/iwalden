```bash
pip install -U discord.py
pip install -U python-dotenv

git clone git@github.com:felixcoperus/iwalden.git
cd iwalden/
touch .env
```

Put the following in .env:
```
DISCORD_TOKEN={token}
DISCORD_GUILD={servername}
```


run
```
python bot.py
```