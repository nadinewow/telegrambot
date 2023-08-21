FROM python:3.9-slim

WORKDIR /telegrambot

COPY ./requirements.txt /telegrambot/requirements.txt

RUN pip install -r requirements.txt

COPY ./bot /telegrambot/bot
CMD ["python", "/telegrambot/bot/main.py"]

EXPOSE 8000
