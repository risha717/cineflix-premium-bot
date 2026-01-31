# 🚀 Railway Deployment সম্পূর্ণ গাইড (বাংলায়)

## 📋 যা যা লাগবে

1. **Railway Account** - https://railway.app (ফ্রি)
2. **Telegram Bot Token** - @BotFather থেকে
3. **MongoDB Atlas Account** - https://mongodb.com (ফ্রি)
4. **Telegram Channels** - ৫টি চ্যানেল তৈরি করতে হবে

---

## ধাপ ১: MongoDB Atlas Setup

### ১.১ MongoDB Atlas Account তৈরি করুন

1. যান: https://www.mongodb.com/cloud/atlas/register
2. Email দিয়ে account তৈরি করুন (ফ্রি)
3. "Create a deployment" ক্লিক করুন

### ১.২ Free Cluster তৈরি করুন

1. **M0 Free** select করুন
2. **Cloud Provider**: AWS select করুন
3. **Region**: Singapore বা Mumbai select করুন (দ্রুত)
4. Cluster Name দিন (যেমন: `Cluster0`)
5. "Create Deployment" ক্লিক করুন

### ১.৩ Database User তৈরি করুন

1. **Username** দিন (যেমন: `cineflix_user`)
2. **Password** দিন (শক্তিশালী password, সেভ করে রাখুন)
3. "Create Database User" ক্লিক করুন

### ১.৪ Network Access সেটআপ করুন

1. বাম পাশে "Network Access" ক্লিক করুন
2. "Add IP Address" ক্লিক করুন
3. "Allow Access from Anywhere" select করুন (0.0.0.0/0)
4. "Confirm" ক্লিক করুন

### ১.৫ Connection String নিন

1. বাম পাশে "Database" ক্লিক করুন
2. "Connect" বাটনে ক্লিক করুন
3. "Drivers" select করুন
4. Connection String কপি করুন:
   ```
   mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/
   ```
5. `<username>` এবং `<password>` replace করুন আপনার credentials দিয়ে

---

## ধাপ ২: Telegram Bot তৈরি করুন

### ২.১ Bot Token নিন

1. Telegram-এ @BotFather খুলুন
2. `/newbot` send করুন
3. Bot এর নাম দিন (যেমন: `Cineflix Premium Bot`)
4. Username দিন (যেমন: `cineflix_premium_bot`)
5. Bot Token সেভ করে রাখুন (দেখতে এরকম: `1234567890:ABCdefGHI...`)

### ২.২ আপনার User ID নিন

1. @userinfobot খুলুন
2. `/start` send করুন
3. আপনার User ID সেভ করুন (যেমন: `1234567890`)

---

## ধাপ ৩: Telegram Channels তৈরি করুন

### ৩.১ ৫টি Channel তৈরি করুন:

1. **Main Channel** - Users দের জয়েন করার জন্য
2. **Backup Channel** - Secondary channel
3. **Adult DB Channel** - Adult videos store করার জন্য
4. **Movie DB Channel** - Movies store করার জন্য
5. **Series DB Channel** - Series store করার জন্য

### ৩.২ Channel Setup:

প্রতিটি channel-এ:
- Channel Type: **Public** করুন (পরে Private করতে পারবেন)
- Bot কে **Admin** বানান
  - Channel Settings → Administrators → Add Admin
  - আপনার bot খুঁজুন এবং add করুন
  - All permissions দিন

### ৩.৩ Channel IDs নিন:

প্রতিটি channel থেকে:
1. যেকোনো message forward করুন @userinfobot -এ
2. Channel ID কপি করুন (দেখতে এরকম: `-1001234567890`)
3. সব IDs সেভ করে রাখুন

### ৩.৪ Channel Links নিন:

প্রতিটি channel-এর:
- Channel Info → Link কপি করুন (যেমন: `https://t.me/cineflix_main`)

---

## ধাপ ৪: Railway-তে Deploy করুন

### ৪.১ Railway Account তৈরি করুন

1. যান: https://railway.app
2. GitHub দিয়ে sign up করুন (recommended)
3. Email verify করুন

### ৪.২ New Project তৈরি করুন

1. Dashboard-এ "New Project" ক্লিক করুন
2. "Empty Project" select করুন
3. Project এর নাম দিন (যেমন: `cineflix-bot`)

### ৪.৩ Service Add করুন

1. "New" button ক্লিক করুন
2. "GitHub Repo" select করুন (যদি GitHub-এ upload করা থাকে)
   
   **অথবা**
   
   "Empty Service" select করুন এবং files manually upload করুন

### ৪.৪ Environment Variables Add করুন

Railway Dashboard-এ:
1. আপনার service select করুন
2. "Variables" tab-এ যান
3. "New Variable" ক্লিক করুন
4. নিচের সব variables add করুন:

```env
BOT_TOKEN=আপনার_bot_token_এখানে
ADMIN_ID=আপনার_user_id_এখানে

DB_CHANNEL_ADULT=adult_channel_id_এখানে
DB_CHANNEL_MOVIE=movie_channel_id_এখানে
DB_CHANNEL_SERIES=series_channel_id_এখানে

MAIN_CHANNEL_ID=main_channel_id_এখানে
BACKUP_CHANNEL_ID=backup_channel_id_এখানে

MAIN_CHANNEL_LINK=https://t.me/your_main_channel
BACKUP_CHANNEL_LINK=https://t.me/your_backup_channel
MINI_APP_URL=https://your-app.vercel.app/

MONGO_URI=আপনার_mongodb_connection_string
DATABASE_NAME=cineflix_premium
```

### ৪.৫ Deploy করুন

1. সব variables add করার পর
2. "Deploy" automatically শুরু হবে
3. Logs check করুন - "✅ Bot started successfully!" দেখা উচিত

---

## ধাপ ৫: Bot Test করুন

### ৫.১ Bot শুরু করুন

1. Telegram-এ আপনার bot খুলুন
2. `/start` send করুন
3. Welcome message আসা উচিত

### ৫.২ Admin Panel Check করুন

1. `/admin` send করুন
2. Admin panel দেখা উচিত (শুধু admin দেখতে পাবে)

### ৫.৩ Video Test করুন

1. যেকোনো video/file send করুন bot-এ
2. Bot category detect করবে
3. Database channel-এ save হবে
4. Success message পাবেন

---

## 🎯 Important Notes

### ✅ Security Checklist:
- [ ] সব secrets Railway variables-এ add করেছেন
- [ ] `.env` file কোথাও commit করেননি
- [ ] MongoDB password strong রেখেছেন
- [ ] Bot token কাউকে share করেননি

### ✅ Channel Checklist:
- [ ] সব channels তৈরি হয়েছে
- [ ] Bot সব channels-এ admin
- [ ] সব Channel IDs সঠিক (negative number)
- [ ] Channel links public accessible

### ✅ Deployment Checklist:
- [ ] Railway service running (green status)
- [ ] সব environment variables set করা
- [ ] Logs-এ কোনো error নেই
- [ ] Bot responding করছে

---

## 🐛 Common Problems & Solutions

### Problem: Bot responding করছে না

**Solution:**
1. Railway dashboard → Service → Logs check করুন
2. Service restart করুন
3. Environment variables verify করুন

### Problem: Database connection error

**Solution:**
1. MongoDB Atlas-এ Network Access check করুন (0.0.0.0/0 allowed?)
2. MONGO_URI সঠিক আছে কিনা verify করুন
3. Username/password সঠিক আছে কিনা check করুন

### Problem: Videos save হচ্ছে না

**Solution:**
1. Bot সব database channels-এ admin কিনা check করুন
2. Channel IDs সঠিক আছে কিনা verify করুন (negative হতে হবে)
3. Bot-এর channel read permission আছে কিনা check করুন

### Problem: Force join কাজ করছে না

**Solution:**
1. MAIN_CHANNEL_ID এবং BACKUP_CHANNEL_ID সঠিক আছে কিনা check করুন
2. Channel links working কিনা test করুন
3. Users channels-এ join করতে পারছে কিনা verify করুন

---

## 📞 Support

যদি কোনো সমস্যা হয়:
1. Railway Logs check করুন (সবচেয়ে গুরুত্বপূর্ণ)
2. সব environment variables double-check করুন
3. MongoDB Atlas connection test করুন
4. Bot permissions verify করুন

---

## 🎉 Congratulations!

আপনার Cineflix Premium Bot এখন live! 🚀

**এখন কি করবেন:**
1. Main channel-এ content post করুন
2. Users দের invite করুন
3. Videos upload করতে থাকুন
4. Admin panel দিয়ে manage করুন

---

**মনে রাখবেন:** Railway free tier-এ monthly limit আছে। Heavy usage হলে paid plan নিতে হতে পারে।

**Good Luck! 🎬**
