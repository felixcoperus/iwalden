# iWalden
De meme, de legende.

## Installation - Local
```bash
git clone git@github.com:felixcoperus/iwalden.git
cd iwalden/app
pip install -U -r requirements.txt
mkdir -p secrets

touch secrets/discord_token
```

Put your discord token in `secrets/discord_token`.


### Run
```
python bot.py
```

### Run in background
```bash
nohup python -u $HOME/git/iwalden/app/bot.py > program.out 2>&1 &
```

Or when in venv:

```bash
nohup /path/to/venv/bin/python -u $HOME/git/iwalden/app/bot.py > program.out 2>&1 &
```

## Installation - Docker
```bash
# get code
git clone git@github.com:felixcoperus/iwalden.git
cd iwalden

# build image (without secret)
docker build . -t felixcop/iwalden

# place secret in git root
mkdir -p secrets
vim secrets/discord_token # contents should be _ONLY_ your discord token

# mount secrets folder and run container
# note that some logging will only appear after stopping the container
docker run -d --mount type=bind,source="$(pwd)/secrets",target=/app/secrets felixcop/iwalden && docker logs $(docker ps -lq)
```

## Installation - Kubernetes
First follow `Installation - Docker`, to build the image, and test your setup.

You then need to host the image somewhere centrally. The easiest is Dockerhub. 
The code below is the code that I use to get this bot running on Kubernetes, change info where applicable.

``` bash
docker login -u felixcop
docker push felixcop/iwalden

kubectl create secret generic iwalden \
    --from-literal=discord_token='<your discord token>'

kubectl apply -f k8s/ # see contents of this folder for specifics
```