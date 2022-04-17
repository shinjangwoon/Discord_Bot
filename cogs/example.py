
from discord.ext import commands

# Example이라는 클래스 선언후 commands.Cog를 상속


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    '''
    Example Cog가 실행 준비가 되었을 때 실행되는
    이벤트 리스너를 등록하는 코드
    실행준비가 완료되면 콘솔창에 example Cog is Ready 문구 출력
    '''
    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")

    @commands.command(name="ping")
    async def _ping(self, ctx):
        await ctx.send('pong!')

# 메인함수에서 봇에 Cog를 등록하기 위한 함수


def setup(client):
    client.add_cog(Example(client))
