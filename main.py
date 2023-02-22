import discord, dotenv, os
import database
from discord.ext import commands
dotenv.load_dotenv()



TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
intents.reactions = True

client = commands.Bot(command_prefix=">", intents=intents)


@client.event
async def on_ready():
    print("Ready")

@client.command(name="showdown")
async def showdown(ctx, user: discord.Member):
    if ctx.author.id == user.id:
        await ctx.send(f"{ctx.author.mention}, You can't challenge yourself!")
    elif database.checkUser(ctx.author.id):
        if database.checkUser(user.id):
            await ctx.send("Both Users in DB")



client.run(TOKEN)