import selfcord
from selfcord import Context
import os
import sys

bot = selfcord.Bot(prefixes="q!")

def stop_bot():
    """stops the bot"""
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.on("ready")
async def ready(time):
    print(f"Connected To {bot.user.name}\n Startup took {time:0.2f} seconds")

@bot.on("message")
async def responder(message: Context):
    if message.content == "Someone just dropped their wallet in this channel! Hurry and open it up with `~grab` before someone else gets it!":
        await message.channel.send("~grab")

@bot.cmd(description="responds with Pong!")
async def ping(ctx: Context):
    await ctx.reply("Pong!")

@bot.cmd(description="stops the bot")
async def stop(ctx: Context):
    await ctx.reply("Stopping...")
    stop_bot()

bot.run("YOUR TOKEN")