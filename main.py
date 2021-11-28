import argparse
import json
import shelve
from os import getenv

from discord.ext import commands
from dotenv import load_dotenv

from cogs import *


def main(dev=False):
    config = None
    with open("config.json") as conf:
        config = json.load(conf)
    print(config)
    bot = commands.Bot("!")
    bot.add_cog(Currency(bot, shelve.open("econ-dev.db" if dev else "econ.db")))
    bot.add_cog(Events(bot))
    bot.run(getenv("TOKEN"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-dev")
    load_dotenv()
    main(parser.parse_args().dev)
