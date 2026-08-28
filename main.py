import os
import re
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import yt_dlp

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [
        ['تحميل مقطع من المنصات'],
        ['حساباتنا على التواصل الاجتماعي']
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    
    welcome_msg = (
        "أهلاً بك في بوت تلاوات الحرمين\n\n"
        "البوت المخصص لنشر التلاوات.\n\n"
        "اختيار الخدمة المطلوبة من القائمة بالأسفل"
    )
    await update.message.reply_text(welcome_msg, reply_markup=markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == 'حساباتنا على التواصل الاجتماعي':
        accounts_msg = (
            "حساباتنا الرسمية لـ تلاوات الحرمين\n\n"
            "• تيك توك:\nhttps://www.tiktok.com/@tilawat_2.h\n\n"
            "• قناة اليوتيوب:\nhttps://www.youtube.com/@tilawat_2.h\n\n"
            "• إنستقرام:\nhttps://www.instagram.com/tilawat_2.h\n\n"
            "• منصة X:\nhttps://x.com/tilawat_2.h\n\n"
            "• قناة تيليجرام:\nhttps://t.me/tilawat_2.h"
        )
        await update.message.reply_text(accounts_msg)
        
    elif text == 'تحميل مقطع من المنصات':
        await update.message.reply_text("أرسل رابط المقطع الآن وسيتم تحميله وإرساله لك.")
        
    elif "http://" in text or "https://" in text:
        # استخراج الرابط فقط من النص
        urls = re.findall(r'(https?://[^\s]+)', text)
        if not urls:
            return
        
        url = urls[0]
        status_msg = await update.message.reply_text("جاري تحميل المقطع...")
        file_path = f"video_{update.message.message_id}.mp4"
        
        # اختيار صيغة مدموجة جاهزة تجنباً للخطأ
        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': file_path,
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            with open(file_path, 'rb') as video:
                await update.message.reply_video(video=video)
            
            await status_msg.delete()
            if os.path.exists(file_path):
                os.remove(file_path)
                
        except Exception as e:
            await status_msg.edit_text("حدث خطأ أثناء التحميل. تأكد من أن المقطع ليس طويلاً جداً وأن الرابط مباشر.")
            if os.path.exists(file_path):
                os.remove(file_path)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
