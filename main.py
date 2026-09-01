import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@Tilawat_2_h"

reply_keyboard = [
    ['حساباتنا على التواصل الاجتماعي', 'الاقتراحات والدعم']
]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "أهلاً بك في بوت تلاوات الحرمين\n\n"
        "البوت لدعمكم وخدماتنا الرسمية.\n\n"
        "اختيار الخدمة من القائمة."
    )
    await update.message.reply_text(welcome_text, reply_markup=markup)

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    if text == 'حساباتنا على التواصل الاجتماعي':
        msg = (
            "حساباتنا الرسمية لـ تلاوات الحرمين:\n\n"
            "• تيك توك: https://www.tiktok.com/@tilawat_2.h\n"
            "• يوتيوب: https://www.youtube.com/@tilawat_2.h\n\n"
            "ولعرض جميع منصاتنا وحساباتنا:\n"
            "https://linktr.ee/tilawat_2.h"
        )
        await update.message.reply_text(msg, disable_web_page_preview=True)

    elif text == 'الاقتراحات والدعم':
        try:
            member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
            if member.status in ['member', 'administrator', 'creator']:
                msg = (
                    "للإقتراحات والدعم معنا عبر مجموعتنا على تيليجرام:\n\n"
                    "https://t.me/+EHtOF91-FWJlYjlk"
                )
                await update.message.reply_text(msg)
            else:
                msg = (
                    "عذراً، يجب عليك الاشتراك في القناة الرسمية أولاً لتتمكن من الوصول لمجموعة الاقتراحات والدعم.\n\n"
                    "إضغط على الرابط للاشتراك ثم أعد المحاولة:\n"
                    "https://t.me/Tilawat_2_h"
                )
                await update.message.reply_text(msg)
        except Exception:
            msg = (
                "يرجى التأكد من الاشتراك في القناة الرسمية أولاً:\n\n"
                "https://t.me/Tilawat_2_h\n\n"
                "ثم الضغط على الزر مرة أخرى."
            )
            await update.message.reply_text(msg)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    app.run_polling()

if __name__ == '__main__':
    main()
