import discord
from discord.ext import commands
import json
import random


class Rule(commands.Cog):
    def __init__(self, client):
        self.client = client

        # 데이터 불러오기
        with open("./data/Rule.json", 'r', encoding='utf-8') as f:
            self.RuleDict = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Rule is Ready")

    @commands.command(name="룰뽑기")
    async def recommand_Rule(self, ctx, arg=None):
        if arg == None:
            categories = list(self.RuleDict.keys())
            category = random.choice(categories)
            Rule = random.choice(self.RuleDict[category])
            await ctx.send(f"오늘 해볼 룰은~ {category} 입니다~")
        else:
            category = arg
            Rule = random.choice(self.RuleDict[category])
            await ctx.send(f"야무지게 {Rule} 어떰?")


def setup(client):
    client.add_cog(Rule(client))
