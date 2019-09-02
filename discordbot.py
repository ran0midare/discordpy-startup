@client.event
async def on_ready():
    while True:
        if time.strftime('%H:%M:%S',time.localtime())=='18:00:00':
            channel = client.get_channel('299037452373458944')
            await client.send_message(channel, '勝手に喋るよ')
            sleep(5)
