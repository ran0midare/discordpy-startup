#coding:UTF-8
import discord
from discord.ext import tasks

TOKEN = "NjE4MTEyNTI2NjI1OTMxMjcz.XW1DIA.pAul1jgdN_mPymMxobJdyGZN_n8" #トークン
CHANNEL_ID = 299037452373458944  #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
