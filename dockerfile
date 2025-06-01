FROM python:3.14.0b1-bookworm

WORKDIR /usr/src/app

COPY . .

RUN apt update && pip install discord.py

CMD ["python", "./this is the way bot.py"]
