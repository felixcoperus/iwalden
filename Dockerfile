FROM python:3.8-slim-buster
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY ./app .
CMD ["python3", "bot.py"]
