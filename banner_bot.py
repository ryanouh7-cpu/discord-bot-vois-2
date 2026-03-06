import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

TARGET_CHANNELS = ["ooo", "urr", "yyu"] 

@bot.event
async def on_ready():
    print(f"✅ Logged in as: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot: return

    if message.channel.name.lower() in [name.lower() for name in TARGET_CHANNELS]:
        try:
            # هنا يقرأ البوت الصورة اللي رفعتها أنت في GitHub
            if os.path.exists("banner.png"):
                file = discord.File("banner.png", filename="uun_banner.png")
                await message.channel.send(file=file)
            else:
                print("❌ Error: 'banner.png' not found in GitHub files!")
        except Exception as e:
            print(f"❌ Error: {e}")

    await bot.process_commands(message)

bot.run(os.getenv('BANNER_BOT_TOKEN'))
