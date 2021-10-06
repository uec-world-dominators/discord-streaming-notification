import discord
import os
import aiohttp

client = discord.Client()

url = os.environ['SLACK_WEBHOOK']
token = os.environ['DISCORD_APP_TOKEN']


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    print(after)
    if after.channel and after.channel.name == '作業配信' and after.self_stream:
        text = f"{member.display_name}が配信しているよ！"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json={
                'text': text
            }) as response:
                print(response.status)

client.run(token)
