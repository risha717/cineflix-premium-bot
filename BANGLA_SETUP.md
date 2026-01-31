# 🎬 Cineflix Premium Bot - সম্পূর্ণ সেটআপ গাইড

## 🌟 আপনার Bot এর Features:

### ✨ Premium Features:
- ✅ **3টি Database Channel** - Adult, Movie, Series
- ✅ **Auto Category Detection** - Automatically detect করবে
- ✅ **Smart Episode Management** - Series এর episodes track করবে
- ✅ **Google Sheet Auto Code** - Click-to-copy codes
- ✅ **Admin Panel** - No coding needed!
- ✅ **Force Join System** - 2 channels
- ✅ **Analytics Dashboard** - Popular videos tracking
- ✅ **Broadcast System** - সব users এ message
- ✅ **Forward Protection** - Videos নিরাপদ
- ✅ **Rate Limiting** - Spam protection
- ✅ **Beautiful UI/UX** - Premium look

---

## 📋 যা যা প্রস্তুত আছে:

### ✅ Bot Settings:
- 🤖 Bot Token: `8006015641:AAHMiqhkmtvRmdLMN1Rbz2EnwsIrsGfH8qU`
- 👤 Admin ID: `1858324638`

### ✅ Database Channels:
- 🔞 Adult DB: `-1003334300028`
- 🎬 Movie DB: `-1003872857468`
- 📺 Series DB: `-1003680803943`

### ✅ Force Join Channels:
- 📢 Main: `-1003749088877` (https://t.me/Cineflixofficialbd)
- 💾 Backup: `-1003809043509` (https://t.me/Cineflixbak)

### ✅ Mini App:
- 📱 URL: https://cinaflix-streaming.vercel.app/

---

## 🚀 Setup Steps (10 মিনিট):

### ধাপ ১: MongoDB Setup (3 মিনিট)

1. **MongoDB Atlas** এ যান: https://www.mongodb.com/cloud/atlas/register
2. **Sign up** করুন (Google দিয়ে করতে পারেন)
3. **Free Cluster** তৈরি করুন:
   - Provider: AWS
   - Region: Singapore (ap-southeast-1)
   - Cluster Tier: M0 Sandbox (FREE)
   - Cluster Name: `cineflix`

4. **Database Access** setup:
   - Left sidebar এ **Database Access** এ click করুন
   - **Add New Database User** click করুন
   - Authentication Method: **Password**
   - Username: `joymodol717` (আপনার username already আছে)
   - Password: একটি **strong password** তৈরি করুন
     - Example: `Cineflix@2026!`
   - Database User Privileges: **Atlas admin**
   - ✅ **Add User** click করুন
   - ⚠️ **এই password টি save করুন!**

5. **Network Access** setup:
   - Left sidebar এ **Network Access** click করুন
   - **Add IP Address** click করুন
   - **Allow Access from Anywhere** select করুন
   - IP Address: `0.0.0.0/0` (auto fill হবে)
   - ✅ **Confirm** click করুন

6. **Connection String** copy করুন:
   - **Database** এ যান
   - আপনার cluster এ **Connect** button click করুন
   - **Drivers** select করুন
   - **Python** এবং version select করুন
   - Connection string copy করুন:
     ```
     mongodb+srv://joymodol717:<password>@cluster0.i9ueyks.mongodb.net/?appName=Cluster0
     ```
   - ⚠️ `<password>` এর জায়গায় আপনার actual password বসান:
     ```
     mongodb+srv://joymodol717:Cineflix@2026!@cluster0.i9ueyks.mongodb.net/?appName=Cluster0
     ```
   - ✅ এই complete URI save করুন!

---

### ধাপ ২: Railway Setup (5 মিনিট)

#### 2.1 GitHub Repository তৈরি করুন

1. **GitHub** এ login করুন: https://github.com
2. **New Repository** click করুন
3. Settings:
   - Repository name: `cineflix-premium-bot`
   - Description: `Cineflix Premium Telegram Bot`
   - Visibility: **Private** (recommended)
4. ✅ **Create repository** click করুন

#### 2.2 Code Upload করুন

**Option A: GitHub Desktop (সহজ)**
1. GitHub Desktop download করুন
2. আপনার repository clone করুন
3. আমার দেওয়া folder এর সব files copy করুন
4. Commit এবং Push করুন

**Option B: Git Command Line**
```bash
# আপনার folder এ যান
cd cineflix_premium

# Git initialize
git init
git add .
git commit -m "Initial commit: Cineflix Premium Bot"

# GitHub এ push
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/cineflix-premium-bot.git
git push -u origin main
```

#### 2.3 Railway Deploy

1. **Railway** এ যান: https://railway.app
2. **Login with GitHub** click করুন
3. **New Project** click করুন
4. **Deploy from GitHub repo** select করুন
5. আপনার `cineflix-premium-bot` repository select করুন
6. ✅ **Deploy Now** click করুন

#### 2.4 Environment Variables Add করুন

1. Railway dashboard এ আপনার project click করুন
2. **Variables** tab এ যান
3. **Raw Editor** toggle করুন
4. নিচের সব variables paste করুন:

```env
BOT_TOKEN=8006015641:AAHMiqhkmtvRmdLMN1Rbz2EnwsIrsGfH8qU
ADMIN_ID=1858324638

DB_CHANNEL_ADULT=-1003334300028
DB_CHANNEL_MOVIE=-1003872857468
DB_CHANNEL_SERIES=-1003680803943

MAIN_CHANNEL_ID=-1003749088877
BACKUP_CHANNEL_ID=-1003809043509

MAIN_CHANNEL_LINK=https://t.me/Cineflixofficialbd
BACKUP_CHANNEL_LINK=https://t.me/Cineflixbak
MINI_APP_URL=https://cinaflix-streaming.vercel.app/

MONGO_URI=mongodb+srv://joymodol717:YOUR_ACTUAL_PASSWORD@cluster0.i9ueyks.mongodb.net/?appName=Cluster0
```

5. ⚠️ **IMPORTANT:** `YOUR_ACTUAL_PASSWORD` replace করুন আপনার MongoDB password দিয়ে!
6. ✅ **Save** click করুন
7. Railway automatically redeploy করবে

---

### ধাপ ৩: Channels Setup (2 মিনিট)

#### 3.1 Bot কে Admin বানান

আপনার **3টি Database Channel** এ bot কে **Administrator** বানান:

1. **Adult Channel** (`-1003334300028`):
   - Channel settings → Administrators
   - Add administrator → খুঁজুন: `@Cinaflix_Streembot`
   - ✅ All permissions দিন

2. **Movie Channel** (`-1003872857468`):
   - Same process

3. **Series Channel** (`-1003680803943`):
   - Same process

#### 3.2 Force Join Channels Setup

আপনার bot automatic force join করবে এই channels:
- Main Channel: https://t.me/Cineflixofficialbd
- Backup Channel: https://t.me/Cineflixbak

⚠️ নিশ্চিত করুন এই channels public/invite link আছে!

---

## ✅ Test করুন!

### 1. Bot Start করুন
- Telegram এ যান
- Search করুন: `@Cinaflix_Streembot`
- `/start` পাঠান
- ✅ Welcome message দেখতে পাবেন!

### 2. Admin Panel Check করুন
- **Admin Panel** button এ click করুন
- ✅ Statistics দেখতে পাবেন!

### 3. Video Upload Test করুন

**Method 1: Direct Upload**
1. আপনার **Movie Database Channel** এ যান
2. একটি video upload করুন
3. Caption দিন: `Test Movie 2026`
4. ✅ Bot আপনাকে Video ID পাঠাবে!

**Method 2: Forward Video**
1. যেকোনো video forward করুন database channel এ
2. Caption edit করুন: `Bachelor Point S05E01`
3. ✅ Bot auto-detect করবে এবং series হিসেবে save করবে!

### 4. Google Sheet Code পান

Bot এর message এ আপনি পাবেন:
```
📋 Google Sheet Code:
S05E01:vid_abc12345
```

এই code copy করে Google Sheet এ paste করুন:
```
Watch Links column:
S05E01:vid_abc12345,S05E02:vid_def67890
```

### 5. Mini App থেকে Test করুন

1. Mini App open করুন: https://cinaflix-streaming.vercel.app/
2. একটি video select করুন
3. **Watch** বা **Download** click করুন
4. Bot start হবে
5. Force join করুন channels এ
6. ✅ Video পাবেন!

---

## 🎯 কিভাবে ব্যবহার করবেন:

### 📹 Video Upload Process:

#### Adult Content:
1. **Adult Database Channel** এ যান
2. Video upload/forward করুন
3. Caption: `Exclusive Content 18+`
4. ✅ Bot save করবে adult category তে

#### Movies:
1. **Movie Database Channel** এ যান
2. Video upload করুন
3. Caption: `Avatar 2 (2026)`
4. ✅ Bot save করবে movie category তে

#### Series (Episodes):
1. **Series Database Channel** এ যান
2. Episodes upload করুন
3. Caption format:
   - `Bachelor Point S05E01`
   - `Bachelor Point S05E02`
   - `Bachelor Point S05E03`
4. ✅ Bot auto-detect করবে season ও episode number!

### 📋 Google Sheet Code Format:

**Single Video:**
```
Full:vid_abc123
```

**Multiple Episodes:**
```
S05E01:vid_abc123,S05E02:vid_def456,S05E03:vid_ghi789
```

**Mixed Format:**
```
Ep 1:vid_aaa,Ep 2:vid_bbb,Ep 3:vid_ccc
```

---

## 🎨 Admin Panel Features:

### 📊 Statistics:
- Total users
- Total videos (by category)
- Today's activity
- Popular videos

### 📹 Manage Videos:
- View all videos
- Filter by category
- Edit video details
- Delete videos
- Get sheet codes

### 📢 Broadcast:
- Send message to all users
- Support text, photo, video
- Progress tracking
- Success/fail report

### ⚙️ Settings (Coming Soon):
- Edit welcome message
- Customize buttons
- Change limits

---

## 🔧 Troubleshooting:

### ❌ Bot responding না করে:
**Check:**
1. Railway logs দেখুন
2. Environment variables সঠিক কিনা
3. Bot token valid কিনা
4. MongoDB connected কিনা

**Fix:**
- Railway dashboard → Logs check করুন
- Variables re-check করুন
- Bot redeploy করুন

### ❌ Video save হচ্ছে না:
**Check:**
1. Bot database channel এ admin কিনা
2. Channel ID সঠিক কিনা
3. Video format supported কিনা

**Fix:**
- Bot কে admin permission দিন
- Channel IDs verify করুন

### ❌ Force join কাজ করছে না:
**Check:**
1. Channel links public কিনা
2. Bot channels এ member কিনা

**Fix:**
- Channel settings check করুন
- Bot কে channels এ add করুন

### ❌ MongoDB connection error:
**Check:**
1. Password সঠিক কিনা MONGO_URI তে
2. IP whitelist করা আছে কিনা (0.0.0.0/0)
3. Network access enabled কিনা

**Fix:**
- Password re-enter করুন
- MongoDB Atlas settings check করুন

---

## 💡 Pro Tips:

### 🎬 Video Organization:
- Adult content শুধু adult channel এ রাখুন
- Movies movie channel এ
- Series proper naming convention use করুন:
  - `Show Name S01E01 - Episode Title`

### 📊 Google Sheet Best Practice:
- Series এর সব episodes একসাথে রাখুন:
  ```
  S01E01:vid_1,S01E02:vid_2,S01E03:vid_3
  ```
- Clear category maintain করুন sheet এ

### 👥 User Engagement:
- Regular broadcast পাঠান
- New content announce করুন
- Active channels maintain করুন

### 🔒 Security:
- Environment variables secure রাখুন
- Database channel private রাখুন
- Admin access carefully share করুন

---

## 📱 Mini App Integration:

আপনার Google Sheet format:

| Title | Image | Watch Links | Region | Download Links |
|-------|-------|-------------|---------|----------------|
| Bachelor Point S5 | img_url | S05E01:vid_1,S05E02:vid_2 | Series | S05E01:vid_3,S05E02:vid_4 |
| Avatar 2 | img_url | Full:vid_100 | Movie | Full:vid_101 |
| Adult Content 18+ | img_url | Full:vid_200 | Adult | Full:vid_201 |

---

## 🎉 সফল Deploy এর পর:

### ✅ Checklist:
- [ ] Bot responding করছে
- [ ] Admin panel কাজ করছে
- [ ] Video save হচ্ছে
- [ ] Sheet codes পাচ্ছেন
- [ ] Force join working
- [ ] Mini app integration complete

### 🚀 Next Steps:
1. ✅ Content upload শুরু করুন
2. ✅ Google Sheet update করুন
3. ✅ Mini App test করুন
4. ✅ Users invite করুন
5. ✅ Enjoy your premium bot!

---

## 📞 Support:

যদি কোনো সমস্যা হয়:
1. এই guide আবার carefully পড়ুন
2. Railway logs check করুন
3. MongoDB connection test করুন
4. Channel permissions verify করুন

---

**🎊 Congratulations! আপনার Cineflix Premium Bot সম্পূর্ণ প্রস্তুত!**

**Made with ❤️ for Cineflix Streaming**
