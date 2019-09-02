#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "NjE4MTEyNTI2NjI1OTMxMjcz.XW09JA.y2IJRVkpoQmnrQNIT0D7JCxuYec" #トークン
CHANNEL_ID =299037452373458944 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '01:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
