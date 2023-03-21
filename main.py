import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
# bot event (when its ready)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return

    steve_jobs_quote = "Innovation distinguishes between a leader and a follower."

    if (message.content == 'steve'):
        await message.channel.send(steve_jobs_quote)
    # if message.content:
    #     response = steve_jobs_quote


@bot.command()
async def test(ctx, *args):
    arguments = ' '.join(args)
    await ctx.send(arguments)

bot.run(TOKEN)
