import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# bot event (when its ready)

print(client)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    steve_jobs_quote = "Innovation distinguishes between a leader and a follower."

    if (message.content == 'steve'):
        await message.channel.send(steve_jobs_quote)
    # if message.content:
    #     response = steve_jobs_quote


client.run(TOKEN)
