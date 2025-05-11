
# 🤖 ربات تلگرامی ارسال آیات قرآن – Send Savab Bot

سلام! 🙋‍♂️  
این یه ربات ساده و کاربردیه برای ارسال آیات قرآن داخل تلگرام. می‌تونه هم به‌صورت تصادفی و هم طبق زمان‌بندی‌ای که تعیین می‌کنی، برات آیه بفرسته. اگه دوست داری روزت رو با یک آیه شروع کنی یا یک یادآوری معنوی داشته باشی، این ربات خیلی به‌دردت می‌خوره!

---

## ✨ امکانات ربات

- 📖 ارسال آیات به‌صورت تصادفی یا به‌ترتیب
- ⏰ تعیین زمان ارسال روزانه برای هر کاربر
- 📚 انتخاب سوره و آیه خاص
- 🌐 ارسال متن عربی + ترجمه فارسی
- 🔄 قابلیت لغو عملیات در هر مرحله

---

## 🚀 چطور راه‌اندازیش کنیم؟

1. این ریپو رو کلون کن یا فایل‌هاشو دانلود کن.
2. با استفاده از فایل `.env.example` یه فایل `.env` بساز و توکن رباتت رو بذار توش.
3. کتابخونه‌های موردنیاز رو نصب کن:
   ```bash
   pip install -r requirements.txt
````

4. برنامه رو اجرا کن:

   ```bash
   python bot.py
   ```

---

## ☁️ چطور روی Render و UptimeRobot دیپلویش کنیم؟

### مرحله 1: دیپلوی روی Render.com (رایگان ✅)

1. برو به [Render.com](https://render.com) و لاگین کن.

2. روی “New Web Service” کلیک کن.

3. ریپوی گیت‌هاب این پروژه رو انتخاب کن.

4. Build command رو بذار:

   ```bash
   pip install -r requirements.txt
   ```

5. Start command:

   ```bash
   bash start.sh
   ```

6. Environment Variable رو اضافه کن:

   * Name: `BOT_TOKEN`
   * Value: توکن ربات تلگرامت

7. دیپلوی کن و چند دقیقه صبر کن تا آماده بشه.

### مرحله 2: روشن نگه‌داشتن رایگان با UptimeRobot

Render تو پلن رایگان، بعد از چند دقیقه عدم استفاده، می‌خوابه. ولی یه ترفند داریم:

1. برو به [UptimeRobot.com](https://uptimerobot.com) و ثبت‌نام کن.
2. روی “Add New Monitor” کلیک کن.
3. این تنظیمات رو بزن:

   * Monitor Type: `HTTP(s)`
   * Friendly Name: `Send Savab Bot`
   * URL: آدرس پابلیک Renderت (مثلاً: `https://send-savab.onrender.com`)
   * Monitoring Interval: هر 5 دقیقه
4. ذخیره کن. تموم شد! 😄

---

## 🧪 دستورات مهم ربات

* `/start` : شروع به کار
* `/cancel` : لغو عملیات جاری
* `/help` : راهنمای ربات

---

## 👨‍💻 سازنده

* توسعه‌دهنده: [@KMmatin\_00](https://t.me/KMmatin_00)

---

## ❗ نکات مهم

* حواست باشه فونت تلگرامت روی "Uthmani" باشه تا آیات درست نمایش داده بشن.
* اگه آیه‌ها تو زمان مشخص‌شده ارسال نمی‌شن، ممکنه مشکلی توی زمان‌بندی یا اتصال به سرور وجود داشته باشه. لاگ‌ها رو چک کن.

---

## 📁 فایل‌های مهم ریپو

* `bot.py`: کد اصلی ربات
* `db.py`: مدیریت پایگاه داده کاربران
* `.env.example`: نمونه فایل محیطی
* `start.sh`: اسکریپت اجرای اتوماتیک
* `requirements.txt`: لیست وابستگی‌ها

---

موفق باشی و ان‌شاءالله ثواب بگیری 💚
اگه سوالی داشتی، توی تلگرام پیام بده یا Issue باز کن.

```

---

# 🕌 Telegram Quran Verse Bot

Hi there! 🙌
This Telegram bot helps you receive **Quranic verses** randomly or based on your preferred settings. Use it for daily reflection, learning, or just peaceful inspiration.

---

## ✨ Features:

* 📖 Get random verses from the Quran
* 🕗 Schedule daily verse delivery
* 🔄 Choose between random or sequential mode
* 📚 Request specific Surah and Ayah
* 💬 Includes Persian translation and Arabic text

---

## 🧭 Commands:

* `/start`: Start using the bot
* `/cancel`: Cancel current action

---

## 🧩 Local Installation:

```bash
git clone https://github.com/your-username/send-savab.git
cd send-savab
pip install -r requirements.txt
cp .env.example .env
# Add your BOT_TOKEN to .env
python bot.py
```

---

## 🚀 Deploying to Render + Keeping Alive with UptimeRobot

### ✅ On Render:

1. Go to [Render.com](https://render.com)
2. Create a **New Web Service**
3. Connect your GitHub repo
4. Start command:

   ```bash
   bash start.sh
   ```
5. Add an environment variable `BOT_TOKEN` with your bot's token.
6. After deployment, get your public URL (e.g. `https://send-savab.onrender.com`)

---

### ✅ On UptimeRobot:

1. Visit [UptimeRobot](https://uptimerobot.com)
2. Click **Add New Monitor**
3. Choose:

   * **Monitor Type**: HTTP(s)
   * **URL**: your Render link
   * **Friendly Name**: e.g. Quran Bot
   * **Check interval**: every 5 minutes
4. Save it!

✅ UptimeRobot will ping your app every 5 minutes so Render doesn't put it to sleep.

---

🕊️ Enjoy using the bot and may it bring blessings to your day!

```

---

