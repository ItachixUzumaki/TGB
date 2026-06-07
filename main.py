import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from modules.post import extract_info
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(filename='logs/bot.log', level=logging.INFO)

# Config
TOKEN = os.getenv("BOT_TOKEN")
SOURCE_ID = int(os.getenv("CHAT_ID1"))
DEST_ID = int(os.getenv("CHAT_ID2"))

async def handle_forward(update: Update, context):
    if update.effective_chat.id != SOURCE_ID:
        return
    
    # Logic to extract URL from forwarded message
    text = update.message.text or update.message.caption
    url = # Logic to regex find URL in text
    
    draft = extract_info(url)
    
    # Send draft with buttons
    keyboard = [[InlineKeyboardButton("Approve", callback_data='approve')]]
    await update.message.reply_text(draft, reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update, context):
    query = update.callback_query
    if query.data == 'approve':
        # Send to DEST_ID
        await context.bot.send_message(chat_id=DEST_ID, text=query.message.text)
        await query.edit_message_text("Post published to channel!")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_forward))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
