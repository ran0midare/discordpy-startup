from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['NjE4MTEyNTI2NjI1OTMxMjcz.XW54xw.wyTy1d5ry-2xlYbRO0UV4pIzA74']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
