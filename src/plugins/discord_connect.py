import discord
import json
import requests
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

ch_ids = ["C015TAH6LPN", 546851119641526282]

with open(".token") as f:
    pre_token = f.readlines()
    tokens = [i.rstrip("\n") for i in pre_token]

post_url = 'https://slack.com/api/chat.postMessage'

class Main(discord.Client):
    async def on_ready(self):
        print("discord bot ready")

    async def on_message(self, message):
        if message.channel.id != ch_ids[1]:
            return

        if message.author == self.user:
            return

        attachments = [{
            "text": message.content
        }]

        payload = {
            "as_user": False,
            "token": tokens[0],
            "channel": ch_ids[0],
            "username": message.author.name,
            "icon_url": re.sub("\.[a-z]+\?size.+$", ".png", str(message.author.avatar_url)),
            "attachments": json.dumps(attachments)
        }

        res = requests.post(post_url, data=payload)
        print(res.status_code)

Main().run(tokens[1])