import json
import os

with open("secrets.json") as f:
    secrets = json.load(f)

API_TOKEN = secrets["slack"]["token"]

DEFAULT_REPLY = "…"

PLUGINS = ["plugins"]