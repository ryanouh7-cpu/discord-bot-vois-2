import discord
from discord.ext import commands
import os

# --- 1. إعداد الصلاحيات ---
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 

# إنشاء البوت (يفضل استخدام توكن مختلف عن بوت التيكت)
bot = commands.Bot(command_prefix='!', intents=intents)

# --- 2. الإعدادات ---
# الرومات اللي حددتها
TARGET_CHANNELS = ["ooo", "urr", "yyu"] 

# رابط البنر الوردي المحدث Uun
BANNER_URL = "http://googleusercontent.com/generated_image_content/0"

@bot.event
async def on_ready():
    print(f"✅ Banner Bot is online as {bot.user}")
    print(f"Monitoring channels: {TARGET_CHANNELS}")

@bot.event
async def on_message(message):
    # تجاهل رسائل البوتات عشان ما يسوي تكرار لا نهائي
    if message.author.bot:
        return

    # التحقق إذا كانت الرسالة في أحد الرومات المطلوبة (بأحرف صغيرة لضمان الدقة)
    if message.channel.name.lower() in [name.lower() for name in TARGET_CHANNELS]:
        try:
            # إرسال البنر بعد رسالة العضو مباشرة
            await message.channel.send(BANNER_URL)
        except Exception as e:
            print(f"❌ Error in {message.channel.name}: {e}")

    # تشغيل الأوامر إذا أضفت أي أمر مستقبلاً
    await bot.process_commands(message)

# تشغيل البوت
bot.run(os.getenv('BANNER_BOT_TOKEN'))
