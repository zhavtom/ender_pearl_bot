with open(".token") as f:
    API_TOKEN = f.readlines()[0].rstrip("\n")

DEFAULT_REPLY = "…"

PLUGINS = ["plugins"]