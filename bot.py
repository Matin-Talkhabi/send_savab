import random
import json
import requests
from datetime import datetime
import asyncio
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters,
    ContextTypes, ConversationHandler
)
from apscheduler.schedulers.background import BackgroundScheduler
from db import init_db, get_user, set_user_time, set_user_mode, update_user_position
from dotenv import load_dotenv
import os
# ===================== لاگ‌گیری =====================
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ===================== تنظیمات اولیه =====================
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
scheduler = BackgroundScheduler()
scheduler.start()

main_menu = ReplyKeyboardMarkup([
    ["📖 دریافت آیه الان"],
    ["🕗 تنظیم ساعت ارسال"],
    ["🔀 انتخاب نوع ارسال آیه"],
    ["📚 انتخاب سوره و آیه خاص"]
], resize_keyboard=True)

# ===================== دریافت آیه =====================
def fetch_ayah(chapter=None, verse=None, mode="random"):
    try:
        if chapter is None:
            chapter = random.randint(1, 114)
        url_ar = f"https://cdn.jsdelivr.net/npm/quran-json@3.1.2/dist/chapters/en/{chapter}.json"
        res_ar = requests.get(url_ar)
        if res_ar.status_code != 200:
            logger.error("خطا در دریافت متن عربی از API.")
            return "❌ خطا در دریافت متن عربی.", chapter, verse
        data_ar = res_ar.json()
        verses = data_ar['verses']

        if verse is None:
            verse_data = random.choice(verses) if mode == "random" else verses[0]
        else:
            verse_data = next((v for v in verses if v['id'] == verse), None)
            if verse_data is None:
                logger.warning(f"آیه {chapter}:{verse} یافت نشد.")
                return "❌ آیه‌ای با این مشخصات پیدا نشد.", chapter, verse

        arabic_text = verse_data['text']
        verse_num = verse_data['id']
        chapter_name = data_ar['name']

        url_fa = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/fas-abdolmohammaday.json"
        res_fa = requests.get(url_fa)
        if res_fa.status_code != 200:
            logger.error("خطا در دریافت ترجمه فارسی.")
            return "❌ خطا در دریافت ترجمه فارسی.", chapter, verse
        data_fa = res_fa.json()['quran']
        translation = next(
            (item['text'] for item in data_fa if item['chapter'] == chapter and item['verse'] == verse_num),
            "❌ ترجمه‌ای یافت نشد."
        )

        return f"📖 سوره {chapter_name} ({chapter}) - آیه {verse_num}\n\n🕋 *متن عربی:*\n\u200F{arabic_text}\n\n🌍 *ترجمه فارسی:*\n{translation}", chapter, verse_num
    except Exception as e:
        logger.exception("خطا در fetch_ayah:")
        return "❌ خطا در دریافت آیه", chapter, verse

# ===================== زمان‌بندی =====================
async def send_ayah_at_time(user_id, bot):
    user_data = get_user(user_id)
    if not user_data:
        return

    mode = user_data[2] or "random"
    chapter = user_data[3]
    verse = user_data[4]

    logger.info(f"ارسال آیه زمان‌بندی شده برای کاربر {user_id} با حالت {mode}")

    if mode == "sequential":
        text, new_chapter, new_verse = fetch_ayah(chapter, verse + 1, mode="sequential")
        update_user_position(user_id, new_chapter, new_verse)
    else:
        text, _, _ = fetch_ayah()

    await bot.send_message(chat_id=user_id, text=text, parse_mode='Markdown')

def schedule_daily(user_id, bot, time_str="08:00"):
    hour, minute = map(int, time_str.split(":"))
    job_id = f"user_{user_id}"

    def wrapper():
        asyncio.create_task(send_ayah_at_time(user_id, bot))

    scheduler.add_job(
        wrapper,
        trigger='cron',
        hour=hour,
        minute=minute,
        id=job_id,
        replace_existing=True
    )
    logger.info(f"زمان‌بندی برای کاربر {user_id} ثبت شد: {time_str}")

# ===================== شروع =====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"کاربر {update.effective_user.id} ربات را استارت کرد.")
    await update.message.reply_text(
        "سلام! 🙌\n"
        "این ربات به شما آیات تصادفی قرآن رو ارسال می‌کنه.\n\n"
        "📌 برای مشاهده صحیح آیات عربی:\n"
        "لطفاً فونت تلگرام خود را روی فونتی مناسب قرآن مثل 'Uthmani' تنظیم کنید.\n\n"
        "🛠 در صورت مشاهده مشکل یا باگ:\n"
        "@KMmatin_00\n\n"
        "⏰ اگر آیه‌ای در زمان مقرر نرسید، ممکنه مشکلی در زمان‌بندی یا تنظیمات باشه.\n\n"
        "برای لغو هر فرآیند، دستور /cancel را ارسال کنید.",
        reply_markup=main_menu
    )

# ===================== منو =====================
async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id
    logger.info(f"کاربر {user_id} انتخاب کرد: {text}")

    if text == "📖 دریافت آیه الان":
        user_data = get_user(user_id)
        mode = user_data[2] if user_data else "random"
        msg, _, _ = fetch_ayah(mode=mode)
        await update.message.reply_text(msg, parse_mode='Markdown')

    elif text == "🕗 تنظیم ساعت ارسال":
        await update.message.reply_text("لطفاً ساعت را به صورت HH:MM وارد کن (مثلاً 08:00):\n\n🛑 برای لغو از /cancel استفاده کن.")
        return 1

    elif text == "🔀 انتخاب نوع ارسال آیه":
        keyboard = ReplyKeyboardMarkup([["🔁 رندوم", "🔢 به ترتیب"]], resize_keyboard=True, one_time_keyboard=True)
        await update.message.reply_text("نوع ارسال آیه را انتخاب کن:\n\n🛑 برای لغو از /cancel استفاده کن.", reply_markup=keyboard)
        return 2

    elif text == "📚 انتخاب سوره و آیه خاص":
        await update.message.reply_text("شماره سوره و آیه را به صورت `سوره:آیه` وارد کن (مثلاً 2:255):\n\n🛑 برای لغو از /cancel استفاده کن.")
        return 3

    else:
        await update.message.reply_text("دستور نامشخص بود.")

    return ConversationHandler.END

# ===================== مراحل گفتگو =====================
async def receive_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        time_str = update.message.text.strip()
        datetime.strptime(time_str, "%H:%M")
        user_id = update.effective_user.id

        set_user_time(user_id, time_str)
        schedule_daily(user_id, context.bot, time_str)

        logger.info(f"کاربر {user_id} ساعت {time_str} را ثبت کرد.")
        await update.message.reply_text(f"⏰ زمان دریافت آیه تنظیم شد: {time_str}", reply_markup=main_menu)
    except Exception as e:
        logger.error(f"خطا در دریافت ساعت از کاربر {update.effective_user.id}: {e}")
        await update.message.reply_text("❌ فرمت ساعت اشتباه است. لطفاً به صورت HH:MM وارد کن.")
    return ConversationHandler.END

async def receive_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    mode = "sequential" if "به ترتیب" in update.message.text else "random"
    set_user_mode(user_id, mode)
    logger.info(f"کاربر {user_id} حالت ارسال را انتخاب کرد: {mode}")
    await update.message.reply_text(f"🔄 حالت ارسال: {mode}", reply_markup=main_menu)
    return ConversationHandler.END

async def receive_specific_ayah(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.strip()
        chapter, verse = map(int, text.split(":"))
        msg, _, _ = fetch_ayah(chapter, verse)
        logger.info(f"کاربر {update.effective_user.id} درخواست آیه خاص داد: {chapter}:{verse}")
        await update.message.reply_text(msg, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"خطا در دریافت آیه خاص از کاربر {update.effective_user.id}: {e}")
        await update.message.reply_text("❌ فرمت اشتباه است. لطفاً به صورت `سوره:آیه` وارد کن.")
    return ConversationHandler.END

# لغو
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"کاربر {update.effective_user.id} فرآیند را لغو کرد.")
    await update.message.reply_text("❌ فرایند لغو شد.", reply_markup=main_menu)
    return ConversationHandler.END

# ===================== اجرا =====================
if __name__ == '__main__':
    init_db()
    logger.info("ربات در حال اجراست...")

    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_time)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_mode)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_specific_ayah)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)

    app.run_polling()
