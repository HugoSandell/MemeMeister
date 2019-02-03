import discord
import threading
import asyncio
import json
from mmresources import R

# Load API key
f = open('keys.json')
API_KEY = json.load(f)["DISCORD_API_KEY"]
f.close()

client = discord.Client(activity=discord.Game("with my lolis"))

@client.event
async def on_ready():
    print('Loading resources...')
    R.load()
    print('Done!')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.author.bot or not message.content.startswith('_'):
        return
    try:
        if message.content == '_gifs':
            msg_list = '**MemeMeister GIF List**\n'
            for gif in R.gifs:
                msg_list += '`_' + gif['name'] + '`  ' + gif['description'] + '\n'
            await message.channel.send(msg_list)
        elif message.content == '_music':
            await message.channel.send('`!play https://www.youtube.com/playlist?list=PL5a5LivkBSfCxd88ZrGq5rDihAaQSh15v`')
        # insert other cases here
        else:
            for gif in R.gifs:
                if ('_' + gif["name"]) == message.content:
                    await message.delete()
                    embed = discord.Embed()
                    embed.set_image(url=gif["url"])
                    await message.channel.send(message.author.mention + ':', embed=embed)

    except Exception as e:
        print(e)

client.run(API_KEY)