import discord
from discord.ext import commands
import os
import aiohttp
import io

# --- 1. Setup Intents ---
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

# --- 2. Configuration ---
TARGET_CHANNELS = ["ooo", "urr", "yyu"] 
# رابط البنر الوردي المحدث Uun
BANNER_URL = "http://googleusercontent.com/generated_image_content/0"

@bot.event
async def on_ready():
    print(f"✅ Uun Banner Bot is online!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.name.lower() in [name.lower() for name in TARGET_CHANNELS]:
        try:
            # تحميل الصورة من الرابط وإرسالها كملف لضمان ظهورها
            async with aiohttp.ClientSession() as session:
                async with session.get(BANNER_URL) as resp:
                    if resp.status == 200:
                        data = io.BytesIO(await resp.read())
                        file = discord.File(data, filename="uun_banner.png")
                        await message.channel.send(file=file)
        except Exception as e:
            print(f"❌ Error sending image: {e}")

    await bot.process_commands(message)

bot.run(os.getenv('BANNER_BOT_TOKEN'))
