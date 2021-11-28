from discord.ext import commands


class Currency(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db

    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.db[member.id] = {}
