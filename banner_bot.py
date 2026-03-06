import discord
from discord.ext import commands
import os
import aiohttp
import io

# --- 1. Setup Intents ---
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # هذا يتطلب التفعيل من موقع المطورين أيضاً

bot = commands.Bot(command_prefix='!', intents=intents)

# --- 2. Configuration ---
# تأكد أن الأسماء مطابقة تماماً لما في الديسكورد
TARGET_CHANNELS = ["ooo", "urr", "yyu"] 
BANNER_URL = "http://googleusercontent.com/generated_image_content/0"

@bot.event
async def on_ready():
    print(f"✅ Logged in as: {bot.user}")
    print(f"✅ Monitoring: {TARGET_CHANNELS}")

@bot.event
async def on_message(message):
    # تجاهل رسائل البوتات
    if message.author.bot:
        return

    # طباعة اسم الروم في سجلات Railway للتأكد من وصول البوت للرسالة
    print(f"📩 New message in: {message.channel.name}")

    # التحقق من الروم
    if message.channel.name.lower() in [name.lower() for name in TARGET_CHANNELS]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(BANNER_URL) as resp:
                    if resp.status == 200:
                        data = io.BytesIO(await resp.read())
                        file = discord.File(data, filename="uun_banner.png")
                        await message.channel.send(file=file)
                        print(f"✨ Banner sent to {message.channel.name}")
                    else:
                        print(f"❌ Failed to download image: Status {resp.status}")
        except Exception as e:
            print(f"❌ Error: {e}")

    await bot.process_commands(message)

# تأكد من اسم المتغير في Railway (BANNER_BOT_TOKEN)
bot.run(os.getenv('BANNER_BOT_TOKEN'))
