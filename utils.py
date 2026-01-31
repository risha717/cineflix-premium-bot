import re
import hashlib
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def generate_video_id(message_id, database):
    """Generate unique video ID"""
    timestamp = int(datetime.now().timestamp())
    raw = f"{database}_{message_id}_{timestamp}"
    hash_obj = hashlib.md5(raw.encode())
    short_hash = hash_obj.hexdigest()[:8]
    return f"vid_{short_hash}"

def detect_category(text):
    """Auto-detect video category from text"""
    if not text:
        return 'other'
    
    text_lower = text.lower()
    
    # Adult content detection
    adult_keywords = ['18+', 'adult', 'xxx', 'porn', 'sex', 'nsfw', '🔞']
    if any(keyword in text_lower for keyword in adult_keywords):
        return 'adult'
    
    # Series detection
    series_keywords = ['episode', 'ep', 'season', 's0', 'e0', 'series', 'সিজন', 'পর্ব']
    if any(keyword in text_lower for keyword in series_keywords):
        return 'series'
    
    # Movie by default
    return 'movie'

def extract_episode_info(text):
    """Extract season and episode numbers from text"""
    if not text:
        return None, None
    
    # Pattern: S01E01, S1E1, Season 1 Episode 1, etc.
    patterns = [
        r'[Ss](\d+)[Ee](\d+)',
        r'[Ss]eason\s*(\d+).*?[Ee]pisode\s*(\d+)',
        r'সিজন\s*(\d+).*?পর্ব\s*(\d+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            season = int(match.group(1))
            episode = int(match.group(2))
            return season, episode
    
    return None, None

def format_file_size(size_bytes):
    """Format file size in human-readable format"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

def format_duration(seconds):
    """Format duration in HH:MM:SS"""
    if not seconds:
        return "Unknown"
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"

def generate_sheet_code(video_data):
    """Generate Google Sheet code for video"""
    video_id = video_data.get('video_id', 'unknown')
    title = video_data.get('title', 'Untitled')
    season = video_data.get('season')
    episode = video_data.get('episode')
    
    # For series with episode info
    if season and episode:
        label = f"S{season:02d}E{episode:02d}"
    else:
        # Extract from title if available
        match = re.search(r'[Ee]p?\.?\s*(\d+)', title)
        if match:
            ep_num = match.group(1)
            label = f"Ep {ep_num}"
        else:
            label = "Full"
    
    return f"{label}:{video_id}"

def generate_batch_sheet_codes(videos):
    """Generate sheet codes for multiple videos (episodes)"""
    if not videos:
        return ""
    
    codes = []
    for video in sorted(videos, key=lambda x: (x.get('season', 0), x.get('episode', 0))):
        code = generate_sheet_code(video)
        codes.append(code)
    
    return ",".join(codes)

def escape_markdown(text):
    """Escape markdown special characters"""
    if not text:
        return ""
    
    special_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in special_chars:
        text = text.replace(char, f'\\{char}')
    return text

def clean_filename(filename):
    """Clean filename for safe storage"""
    if not filename:
        return "untitled"
    
    # Remove special characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Replace spaces with underscores
    filename = filename.replace(' ', '_')
    # Limit length
    if len(filename) > 100:
        filename = filename[:100]
    
    return filename

def parse_admin_command(text):
    """Parse admin commands"""
    parts = text.strip().split(maxsplit=1)
    command = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""
    return command, args

def format_time_ago(dt):
    """Format datetime as 'time ago' string"""
    if not dt:
        return "Unknown"
    
    now = datetime.now()
    diff = now - dt
    
    seconds = diff.total_seconds()
    
    if seconds < 60:
        return "Just now"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif seconds < 604800:
        days = int(seconds / 86400)
        return f"{days} day{'s' if days > 1 else ''} ago"
    else:
        return dt.strftime("%d %b %Y")

def validate_channel_id(channel_id):
    """Validate Telegram channel ID format"""
    try:
        channel_id = int(channel_id)
        # Telegram channel IDs are negative and usually start with -100
        if channel_id < 0:
            return True
        return False
    except:
        return False

def get_category_emoji(category):
    """Get emoji for category"""
    from config import CATEGORY_EMOJI
    return CATEGORY_EMOJI.get(category, '📹')

def get_database_name(database):
    """Get human-readable database name"""
    from config import DB_NAMES
    return DB_NAMES.get(database, 'Unknown DB')

def create_pagination_buttons(current_page, total_pages, callback_prefix):
    """Create pagination buttons"""
    buttons = []
    
    if current_page > 1:
        buttons.append(('◀️ Previous', f'{callback_prefix}_page_{current_page - 1}'))
    
    buttons.append((f'{current_page}/{total_pages}', 'noop'))
    
    if current_page < total_pages:
        buttons.append(('Next ▶️', f'{callback_prefix}_page_{current_page + 1}'))
    
    return buttons

def split_message(text, max_length=4096):
    """Split long message into chunks"""
    if len(text) <= max_length:
        return [text]
    
    chunks = []
    current_chunk = ""
    
    for line in text.split('\n'):
        if len(current_chunk) + len(line) + 1 <= max_length:
            current_chunk += line + '\n'
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = line + '\n'
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

def extract_video_title(caption, filename):
    """Extract clean video title from caption or filename"""
    # Try caption first
    if caption:
        # Remove markdown, hashtags, etc.
        title = re.sub(r'[#@]', '', caption)
        # Take first line
        title = title.split('\n')[0].strip()
        if title and len(title) > 3:
            return title[:200]  # Limit length
    
    # Fallback to filename
    if filename:
        # Remove extension
        title = re.sub(r'\.[^.]+$', '', filename)
        # Clean up
        title = title.replace('_', ' ').replace('-', ' ')
        return title[:200]
    
    return "Untitled"

def is_adult_content(text):
    """Check if content is adult"""
    if not text:
        return False
    
    text_lower = text.lower()
    adult_indicators = ['18+', 'adult', 'xxx', 'porn', 'sex', 'nsfw', '🔞', 'nude', 'onlyfans']
    
    return any(indicator in text_lower for indicator in adult_indicators)

def generate_unique_code(text):
    """Generate unique short code from text"""
    hash_obj = hashlib.md5(text.encode())
    return hash_obj.hexdigest()[:6].upper()

def format_number(num):
    """Format number with commas"""
    return f"{num:,}"

def get_greeting():
    """Get time-based greeting"""
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        return "সুপ্রভাত! 🌅"
    elif 12 <= hour < 17:
        return "শুভ অপরাহ্ন! ☀️"
    elif 17 <= hour < 21:
        return "শুভ সন্ধ্যা! 🌆"
    else:
        return "শুভ রাত্রি! 🌙"

class RateLimiter:
    """Simple rate limiter"""
    def __init__(self, max_requests=20, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}
    
    def is_allowed(self, user_id):
        """Check if user is allowed to make request"""
        now = datetime.now()
        
        if user_id not in self.requests:
            self.requests[user_id] = []
        
        # Clean old requests
        self.requests[user_id] = [
            req_time for req_time in self.requests[user_id]
            if (now - req_time).total_seconds() < self.time_window
        ]
        
        # Check limit
        if len(self.requests[user_id]) >= self.max_requests:
            return False
        
        # Add new request
        self.requests[user_id].append(now)
        return True

# Global rate limiter instance
rate_limiter = RateLimiter()

logger.info("✅ Utils loaded successfully!")
