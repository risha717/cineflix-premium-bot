import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID', '0'))

# Database Channels
DB_CHANNEL_ADULT = int(os.getenv('DB_CHANNEL_ADULT', '0'))
DB_CHANNEL_MOVIE = int(os.getenv('DB_CHANNEL_MOVIE', '0'))
DB_CHANNEL_SERIES = int(os.getenv('DB_CHANNEL_SERIES', '0'))

# Force Join Channels
MAIN_CHANNEL_ID = int(os.getenv('MAIN_CHANNEL_ID', '0'))
BACKUP_CHANNEL_ID = int(os.getenv('BACKUP_CHANNEL_ID', '0'))

# Channel Links
MAIN_CHANNEL_LINK = os.getenv('MAIN_CHANNEL_LINK', '')
BACKUP_CHANNEL_LINK = os.getenv('BACKUP_CHANNEL_LINK', '')
MINI_APP_URL = os.getenv('MINI_APP_URL', '')

# MongoDB
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'cineflix_premium')

# Bot Settings
FORCE_SUB_CHANNELS = [MAIN_CHANNEL_ID, BACKUP_CHANNEL_ID]
DATABASE_CHANNELS = {
    'adult': DB_CHANNEL_ADULT,
    'movie': DB_CHANNEL_MOVIE,
    'series': DB_CHANNEL_SERIES
}

# Messages
WELCOME_MSG = """
🎬 **Welcome to Cineflix Streaming Bot!**

আসসালামু আলাইকুম! স্বাগতম {name} 🌟

✨ **Cineflix Premium Bot এ আপনাকে স্বাগতম!**

🎯 **Features:**
🎬 Unlimited Movies & Series
🔞 Adult Content (18+)
📱 Mini App Integration
💎 Premium Quality
⚡ Fast Download/Streaming

📲 **Get Started:**
👇 নিচের বাটনে ক্লিক করুন

🆔 Your ID: `{user_id}`
"""

HELP_MSG = """
📚 **কিভাবে ব্যবহার করবেন?**

**Step 1:** আমাদের চ্যানেলে জয়েন করুন
**Step 2:** Mini App open করুন
**Step 3:** Video select করুন
**Step 4:** Watch/Download click করুন
**Step 5:** Enjoy! 🎉

💡 **Categories:**
🔞 Adult Content
🎬 Movies
📺 Series

🎯 **Tips:**
• Premium content unlock করতে চ্যানেলে active থাকুন
• Daily new uploads পাবেন
• Fast download speed

❓ Need help? Contact Admin
"""

FORCE_JOIN_MSG = """
🔒 **Content Locked!**

এই ভিডিও দেখতে হলে আমাদের চ্যানেলে জয়েন করুন! 👇

📢 **Main Channel** - সব latest updates
💾 **Backup Channel** - Extra content

✅ জয়েন করার পর **"✅ Joined"** বাটনে ক্লিক করুন
"""

VIDEO_SENT_MSG = """
✅ **Video Sent Successfully!**

🎬 Enjoy your content!

📱 **More videos পেতে:**
👉 Mini App: {mini_app}
👉 Main Channel: {main_channel}

⭐ Share with friends!
"""

# Admin Panel Messages
ADMIN_PANEL_MSG = """
⚙️ **CINEFLIX ADMIN PANEL**

👋 Welcome Boss! 

📊 **Quick Stats:**
👥 Total Users: {users}
🎬 Total Videos: {videos}
🔞 Adult: {adult}
🎬 Movies: {movies}
📺 Series: {series}

📈 **Today's Activity:**
➕ New Users: {new_users}
📹 Videos Added: {new_videos}

🕐 Last Updated: {time}
"""

VIDEO_SAVED_MSG = """
✅ **New Video Saved!**

📝 **Title:** {title}
🆔 **Video ID:** `{video_id}`
📂 **Category:** {category}
💾 **Database:** {database}
📊 **File Size:** {size}

📋 **Google Sheet Code:**
```
{sheet_code}
```

**Quick Actions:**
"""

# Category Emojis
CATEGORY_EMOJI = {
    'adult': '🔞',
    'movie': '🎬',
    'series': '📺',
    'other': '📹'
}

# Database Names
DB_NAMES = {
    'adult': 'Adult DB',
    'movie': 'Movie DB',
    'series': 'Series DB'
}

# Button Labels
BTN_LABELS = {
    'mini_app': '📱 Open Mini App',
    'main_channel': '📢 Main Channel',
    'backup_channel': '💾 Backup Channel',
    'help': '❓ Help',
    'admin_panel': '⚙️ Admin Panel',
    'joined': '✅ Joined, Get Video',
    'manage_videos': '📹 Manage Videos',
    'manage_channels': '📢 Manage Channels',
    'broadcast': '✉️ Broadcast',
    'statistics': '📊 Statistics',
    'settings': '⚙️ Settings',
    'back': '🔙 Back',
    'copy_code': '📋 Copy Code',
    'edit': '✏️ Edit',
    'delete': '🗑️ Delete',
    'view_all': '👁️ View All Videos',
    'add_channel': '➕ Add Channel',
    'remove_channel': '➖ Remove Channel',
    'refresh': '🔄 Refresh'
}

# Feature Flags
FEATURES = {
    'auto_category': True,
    'age_verification': True,
    'search_enabled': True,
    'analytics_enabled': True,
    'auto_sheet_code': True,
    'dual_database': True
}

# Limits
MAX_FILE_SIZE = 2000 * 1024 * 1024  # 2GB
MAX_BROADCAST_USERS = 10000
RATE_LIMIT_MESSAGES = 20  # per minute
CACHE_TTL = 3600  # 1 hour

# Logging
LOG_CHANNEL = MAIN_CHANNEL_ID  # Where to send error logs
DEBUG_MODE = False

print("✅ Configuration loaded successfully!")
