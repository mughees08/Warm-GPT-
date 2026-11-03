
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TELEGRAM_TOKEN = "8803467655:AAFNjWx6rLDbp41SPooodWWBRcqRbkPdULc"
API_KEY = ""
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Main test bot hoon. Kuch bhi poochein.')
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": user_text}]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        reply = response_data['choices'][0]['message']['content']
    except Exception as e:
        reply = f"API Error: {e}"
    await update.message.reply_text(reply)
if __name__ == '__main__':
    print("Bot start ho raha hai...")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot chal raha hai! Ab Telegram par check karein.")
    app.run_polling()
