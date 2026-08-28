import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [['حساباتنا على التواصل الاجتماعي']]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    
    welcome_msg = (
        "أهلاً بك في بوت تلاوات الحرمين 🌿\n\n"
        "البوت المخصص لنشر التلاوات الخاشعة والروائع القرآنية.\n\n"
        "يرجى اختيار الخدمة المطلوبة من القائمة بالأسفل 👇"
    )
    await update.message.reply_text(welcome_msg, reply_markup=markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == 'حساباتنا على التواصل الاجتماعي':
        accounts_msg = (
            "حساباتنا الرسمية لـ تلاوات الحرمين 🌿\n\n"
            "• تيك توك:\nhttps://www.tiktok.com/@tilawat_2.h\n\n"
            "• قناة اليوتيوب:\nhttps://www.youtube.com/@tilawat_2.h\n\n"
            "• إنستقرام:\nhttps://www.instagram.com/tilawat_2.h\n\n"
            "• منصة X:\nhttps://x.com/tilawat_2.h\n\n"
            "• قناة تيليجرام:\nhttps://t.me/tilawat_2.h"
        )
        await update.message.reply_text(accounts_msg)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
