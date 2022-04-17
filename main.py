import discord
from discord.ext import commands
import os

'''
Cog를 등록하기 위해 기존 코드를 일부분을 삭제
'''


def main():

    prefix = '!'
    # 봇이 서버 멤버의 정보나, 서버 멤버 리스트를 불러올 수 있도록 허용
    intents = discord.Intents.all()

    # 봇 객체를 만드는 부분
    # 봇이 채팅을 읽을 때, 이 접두사로 시작하는 모든 메세지를 명령어로 인식
    client = commands.Bot(command_prefix=prefix, intents=intents)

    # @client.command(name='ping')
    # async def ping(ctx):
    #     await ctx.send("pong!")

    for filename in os.listdir('./cogs'):
        if '.py' in filename:
            filename = filename.replace('.py', '')
            client.load_extension(f'cogs.{filename}')

    # 토큰에서 저장 해 두엇던 텍스트 파일을 불러와, token 변수에 저장
    with open('token.txt', 'r') as f:
        token = f.read()

    # 생성한 봇 객체에 토큰을 넣어 실행하는 코드
    client.run(token)


if __name__ == '__main__':
    main()
