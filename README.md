
# 🕌 ربات تلگرام ارسال آیات قرآن

سلام! 🙌  
این ربات تلگرام به شما کمک می‌کنه تا آیات قرآن کریم رو به صورت **تصادفی** یا طبق تنظیمات دلخواهتون دریافت کنید. می‌تونید از این ربات برای **یادگیری، تدبر و دلگرمی روزانه** استفاده کنید.

---

## ✨ امکانات:
- 📖 دریافت آیه تصادفی از قرآن
- 🕗 ارسال خودکار آیه در زمان مشخص‌شده توسط کاربر
- 🔄 انتخاب حالت ارسال: تصادفی یا ترتیبی
- 📚 دریافت آیه خاص از سوره و آیه مورد نظر
- 💬 نمایش ترجمه فارسی همراه با متن عربی آیه

---

## 🛠 شروع استفاده:
1. ربات رو استارت کنید (`/start`) و وارد منو بشید.
2. یکی از گزینه‌ها رو انتخاب و تنظیمات دلخواه رو انجام بدید.
3. برای زمان‌بندی، ساعت مورد نظر رو وارد کنید (مثلاً `07:30`).
4. ربات طبق تنظیمات شما، آیه‌های دلخواه رو ارسال می‌کنه.

---

## 🧭 دستورات کاربردی:
- `/start` : شروع استفاده از ربات
- `/cancel` : لغو عملیات فعلی

---

## ⚠️ نکات مهم:
- برای دیدن بهتر آیات عربی، از فونت «Uthmani» در تلگرام استفاده کنید.
- اگر آیه‌ای در زمان مشخص ارسال نشد، تنظیمات ساعت رو بررسی کنید.

---

## 🧩 نصب و راه‌اندازی محلی:
1. این مخزن رو کلون یا دانلود کنید.
2. محیط مجازی پایتون بسازید (اختیاری اما پیشنهادی).
3. کتابخانه‌ها رو نصب کنید:
   ```bash
   pip install -r requirements.txt


4. فایل `.env` بسازید و مقدار توکن ربات رو وارد کنید:

   ```
   BOT_TOKEN=your_telegram_bot_token
   ```
5. اجرا:

   ```bash
   python bot.py
   ```

---

## 🚀 دیپلوی در Render.com و استفاده از UptimeRobot

### ✅ مراحل دیپلوی در Render:

1. وارد [Render.com](https://render.com) شوید و ثبت‌نام کنید.

2. از داشبورد گزینه **New Web Service** را انتخاب کنید.

3. مخزن گیت‌هاب خود را متصل کنید.

4. تنظیمات را این‌گونه وارد کنید:

   * **Start command**:

     ```bash
     bash start.sh
     ```
   * **Environment Variables**:

     * `BOT_TOKEN` را اضافه کنید و مقدار آن را برابر با توکن واقعی ربات قرار دهید.
   * **Port** (در صورت نیاز): `10000`

5. منتظر بمانید تا سرویس بالا بیاید و URL عمومی را دریافت کنید (مثلاً: `https://send-savab.onrender.com`)

---

### ✅ روشن نگه‌داشتن ربات با UptimeRobot:

1. به [UptimeRobot.com](https://uptimerobot.com) بروید و ثبت‌نام کنید.
2. روی **Add New Monitor** کلیک کنید.
3. مشخصات زیر را وارد کنید:

   * **Monitor Type**: HTTP(s)
   * **URL**: آدرس Render شما (مثلاً `https://send-savab.onrender.com`)
   * **Friendly Name**: هر اسمی مثل `Quran Bot`
   * **Interval**: هر 5 دقیقه
4. ذخیره کنید.

✅ حالا ربات شما همیشه بیدار می‌مونه و UptimeRobot اجازه نمی‌ده Render اونو به خواب ببره.

---

## 👨‍💻 توسعه‌دهنده:

* [@KMmatin\_00](https://t.me/KMmatin_00) – برنامه‌نویس ربات و طراح اصلی

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

