import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import time



load_dotenv(dotenv_path=".env") # This will load my enviornment variables
BOT_TOKEN = os.getenv("TELE_TOKEN")
DAILY_TEXT="https://www.jw.org/finder?srcid=jwlshare&wtlocale=E&prefer=lang&alias=daily-text"

time_reminders = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await time_loop(update, context)
    await update.message.reply_text(f"Welcome To Your Reminder  Bot!")

async def add(update: Update, context:ContextTypes.DEFAULT_TYPE):
    reminder = " ".join(context.args)
    await update.message.reply_text(f"Reminder Added: {reminder}")

async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    daily_text = DAILY_TEXT
    print(daily_text)
    await update.message.reply_text(daily_text)

async def clean_chat(update: Update, context:ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    current_id = update.message.message_id

    for msg_id in range(current_id - 30, current_id):
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
        except:
            pass

async def time_based_reminder(update: Update, context:ContextTypes.DEFAULT_TYPE):
    args = context.args
    time = args[0]
    reminder = " ".join(args[1:])
    time_reminders.update({time: reminder})
    print(time_reminders)
    await update.message.reply_text("Reminder added")

async def time_loop(Update, Context):
    while True:
        current_time = time.strftime("%H:%M")
        for ti in time_reminders:
            if ti == current_time:
                await Update.message.reply_text(time_reminders[ti])
            else:
                pass

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("text", text))
app.add_handler(CommandHandler("clean", clean_chat))
app.add_handler(CommandHandler("time", time_based_reminder))

app.run_polling()

# bot_name: dypyrembot

