from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH
from handlers import register_handlers

app = Client("GeminiBot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

register_handlers(app)

print("🤖 Gemini Telegram Bot is running...")
app.run()
