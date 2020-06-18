import discord
import json
import requests
import re

with open("secrets.json") as f:
    secrets = json.load(f)

client = discord.Client()

post_url = 'https://slack.com/api/chat.postMessage'

@client.event
async def on_ready():
    print("discord bot ready")

@client.event
async def on_message(message):

    if message.channel.id != secrets["discord"]["channel"]:
        return

    if message.webhook_id:
        return

    msgtext = message.content

    if message.attachments:
        for attachment in message.attachments:
            if msgtext:
                msgtext += "\n"
            msgtext += attachment.url

    payload = {
        "text": msgtext,
        "as_user": False,
        "unfurl_media": True,
        "token": secrets["slack"]["token"],
        "channel": secrets["slack"]["channel"],
        "username": message.author.name,
        "icon_url": re.sub("\.[a-z]+\?size.+$", ".png", str(message.author.avatar_url)),
    }

    res = requests.post(post_url, data=payload)

client.run(secrets["discord"]["token"])