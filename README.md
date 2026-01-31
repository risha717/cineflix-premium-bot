# 🎬 Cineflix Premium Bot

A powerful Telegram bot for streaming and managing movies, series, and adult content with MongoDB integration.

## ✨ Features

- 🎬 **Multi-Category Support**: Movies, Series, and Adult content
- 📱 **Mini App Integration**: External web app integration
- 🔐 **Force Subscribe**: Users must join channels to access content
- 📊 **Admin Panel**: Complete statistics and management
- 💾 **MongoDB**: Persistent data storage
- 🔍 **Search**: Advanced video search functionality
- 📈 **Analytics**: Track views, downloads, and user activity
- ✉️ **Broadcast**: Send messages to all users
- 🎯 **Auto-Categorization**: Smart content organization

## 🚀 Railway Deployment Guide

### Prerequisites
- Railway account (https://railway.app)
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- MongoDB Atlas account (free tier works)
- Telegram channels for database storage

### Step 1: Setup MongoDB Atlas

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Create a database user with username and password
4. Get your connection string (should look like: `mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/`)
5. Whitelist all IPs (0.0.0.0/0) in Network Access

### Step 2: Create Telegram Bot

1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow instructions
3. Save your bot token (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 3: Setup Channels

Create the following Telegram channels:
- **Main Channel**: For users to join
- **Backup Channel**: Secondary channel
- **Database Channels**: 3 channels for storing videos
  - Adult content channel
  - Movies channel
  - Series channel

Make your bot an **admin** in all database channels.

### Step 4: Get Channel IDs

1. Forward any message from each channel to [@userinfobot](https://t.me/userinfobot)
2. It will show you the channel ID (e.g., `-1001234567890`)
3. Save all channel IDs

### Step 5: Deploy to Railway

#### Option A: Using Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Add environment variables (see below)
railway variables set BOT_TOKEN=your_bot_token_here
railway variables set ADMIN_ID=your_user_id
# ... (add all other variables)

# Deploy
railway up
```

#### Option B: Using Railway Dashboard

1. Go to [Railway](https://railway.app)
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Or click **"Deploy from local directory"** and upload this folder
4. Go to **"Variables"** tab
5. Add all environment variables (see Environment Variables section below)
6. Railway will automatically deploy

### Step 6: Configure Environment Variables

Add these variables in Railway dashboard:

```env
# Bot Configuration
BOT_TOKEN=your_bot_token_from_botfather
ADMIN_ID=your_telegram_user_id

# Database Channels
DB_CHANNEL_ADULT=-1001234567890
DB_CHANNEL_MOVIE=-1001234567891
DB_CHANNEL_SERIES=-1001234567892

# Force Join Channels
MAIN_CHANNEL_ID=-1001234567893
BACKUP_CHANNEL_ID=-1001234567894

# Channel Links
MAIN_CHANNEL_LINK=https://t.me/your_main_channel
BACKUP_CHANNEL_LINK=https://t.me/your_backup_channel
MINI_APP_URL=https://your-mini-app.vercel.app/

# MongoDB
MONGO_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?appName=Cluster0
DATABASE_NAME=cineflix_premium
```

### How to Get Your User ID

Send `/start` to [@userinfobot](https://t.me/userinfobot) to get your Telegram user ID.

## 📝 Local Development

### Setup

1. Clone this repository
2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Edit `.env` and add your credentials

6. Run the bot:
```bash
python bot.py
```

## 🎯 Usage

### For Users
1. Start the bot: `/start`
2. Join required channels
3. Use Mini App to browse videos
4. Send video link to bot to get file

### For Admins
1. Send `/admin` to access admin panel
2. Forward videos to bot from any chat
3. Bot will auto-detect category and save
4. Use admin panel to manage videos, users, and broadcast

## 📋 Bot Commands

- `/start` - Start the bot
- `/help` - Show help message
- `/admin` - Admin panel (admin only)
- `/stats` - View statistics (admin only)
- `/broadcast` - Broadcast message (admin only)

## 🔧 Configuration

All configuration is in `config.py`. You can customize:
- Welcome messages
- Help text
- Button labels
- Feature flags
- Rate limits
- File size limits

## 🛡️ Security Notes

- ⚠️ **Never commit `.env` file**
- ✅ All secrets are in environment variables
- ✅ MongoDB credentials not hardcoded
- ✅ Bot token stored securely
- ✅ `.gitignore` configured properly

## 📊 Database Structure

### Collections
- **videos**: All video metadata
- **users**: User information and activity
- **settings**: Bot configuration
- **analytics**: Usage analytics

## 🐛 Troubleshooting

### Bot not responding
- Check if Railway service is running
- Verify all environment variables are set
- Check Railway logs for errors

### Database connection failed
- Verify MongoDB URI is correct
- Check if IP is whitelisted in MongoDB Atlas
- Ensure database user has correct permissions

### Videos not saving
- Make sure bot is admin in database channels
- Check channel IDs are correct (must be negative)
- Verify bot has permission to read channel messages

## 📞 Support

If you encounter any issues:
1. Check Railway logs
2. Verify all environment variables
3. Ensure MongoDB is accessible
4. Check bot permissions in channels

## 📄 License

This project is for educational purposes only.

## ⚠️ Disclaimer

This bot is for personal use only. Ensure you have rights to distribute any content you upload.

---

Made with ❤️ for Cineflix Premium
