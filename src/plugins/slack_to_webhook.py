from slackbot.bot import listen_to
from .utils import in_channel
import requests, json

with open("secrets.json") as f:
    secrets = json.load(f)

@listen_to("(.|\s)*?")
def main(message, param):
    text = message.body["text"]
    if "file" in message.body:
        if text:
            text += "\n"
        text += message.body["file"]["url_private"]

    try:
        user = message.channel._client.users[message.body['user']]
    except KeyError:
        return
    
    username = user["profile"]["display_name"] or ["name"]
    icon_url = user["profile"]["image_original"] or ""
    
    requests.post(secrets["discord"]["webhook"], data = json.dumps({
        "text": text,
        "username": username,
        "icon_url": icon_url
    }))