from pyrogram import Client, filters
from ai import ask_google
from pyrogram.enums import ChatAction

# Telegram message character limit
MAX_MESSAGE_LENGTH = 4000

def register_handlers(app: Client):
    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):
        await message.reply_text(
            "👋 Hello! I'm your Bunny AI bot.\n\n"
            "Use /ask followed by your question to get an answer.\n"
            "Use /help for command info."
        )

    @app.on_message(filters.command("help"))
    async def help_cmd(client, message):
        await message.reply_text(
            "**🤖 Available Commands:**\n\n"
            "`/start` - Welcome message\n"
            "`/help` - Show this help message\n"
            "`/ask <your question>` - Ask anything using Bunny AI\n\n"
            "_Example:_ `/ask What is quantum computing?`"
        )

    @app.on_message(filters.command("ask"))
    async def ask_cmd(client, message):
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            await message.reply_text("❗ Please provide a prompt:\n`/ask What is the capital of France?`")
            return

        prompt = parts[1].strip()
        await message.reply_chat_action(ChatAction.TYPING)

        reply = await ask_google(prompt)
        if not reply:
            await message.reply_text("❌ No response from BunnyAI.")
            return

        # Split and send long responses in chunks
        for i in range(0, len(reply), MAX_MESSAGE_LENGTH):
            await message.reply_text(reply[i:i + MAX_MESSAGE_LENGTH])
