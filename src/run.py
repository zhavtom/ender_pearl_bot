from slackbot.bot import Bot
from subprocess import Popen

p = Popen(["python", "discord_connect.py"])

def main():
    bot = Bot()
    bot.run()

def end_func():
    p.terminate()

if __name__ == "__main__":
    print("slack bot ready")
    main()

import atexit
atexit.register(end_func)