# 📖 Quick Reference Guide - Cineflix Bot

## ⚡ Quick Commands

### User Commands:
- `/start` - Start the bot / Get video
- `/help` - Show help message

### Admin Commands (via buttons):
- **Admin Panel** - Main control center
- **Manage Videos** - View/Edit/Delete videos
- **Broadcast** - Send message to all users
- **Statistics** - View bot analytics

---

## 🎯 Video Upload Quick Guide

### Format:
```
Title: [Show Name] S[Season]E[Episode] - [Episode Title]

Examples:
✅ Bachelor Point S05E01 - First Day
✅ Money Heist S01E02
✅ Avatar 2 (2026)
✅ Exclusive Content 18+
```

### Auto-Detection:
- **Series:** Detects S01E01, Season 1 Episode 1
- **Adult:** Detects 18+, Adult, XXX, 🔞
- **Movie:** Default for everything else

---

## 📋 Google Sheet Code Format

### Single Video:
```
Full:vid_abc123
```

### Series Episodes:
```
S05E01:vid_a1b2,S05E02:vid_c3d4,S05E03:vid_e5f6
```

### Alternative Format:
```
Ep 1:vid_111,Ep 2:vid_222,Ep 3:vid_333
```

---

## 🎨 Category Icons

- 🔞 Adult
- 🎬 Movies
- 📺 Series
- 📹 Other

---

## 🔧 Common Issues & Quick Fixes

### Bot not responding?
```bash
# Check Railway logs
# Verify environment variables
# Restart deployment
```

### Video not saving?
```bash
# Make bot admin in database channel
# Check channel ID in config
# Verify video format (video/document)
```

### Force join not working?
```bash
# Check channel links are public
# Verify channel IDs in FORCE_SUB_CHANNELS
# Make sure bot is member of channels
```

### MongoDB error?
```bash
# Check password in MONGO_URI
# Verify IP whitelist (0.0.0.0/0)
# Test connection string
```

---

## 📊 Database Channels

| Channel | Category | ID |
|---------|----------|-----|
| Adult DB | Adult Content | -1003334300028 |
| Movie DB | Movies | -1003872857468 |
| Series DB | TV Series | -1003680803943 |

---

## 🎯 Environment Variables

```env
BOT_TOKEN=your_bot_token
ADMIN_ID=your_telegram_id
DB_CHANNEL_ADULT=-100xxx
DB_CHANNEL_MOVIE=-100yyy
DB_CHANNEL_SERIES=-100zzz
MAIN_CHANNEL_ID=-100aaa
BACKUP_CHANNEL_ID=-100bbb
MAIN_CHANNEL_LINK=https://t.me/channel
BACKUP_CHANNEL_LINK=https://t.me/backup
MINI_APP_URL=https://your-app.vercel.app/
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/
```

---

## 🚀 Deployment Checklist

### Pre-Deploy:
- [ ] MongoDB cluster created
- [ ] Database user created
- [ ] IP whitelist configured (0.0.0.0/0)
- [ ] Connection URI copied
- [ ] GitHub repo created
- [ ] All files uploaded

### Deploy:
- [ ] Railway account created
- [ ] Project deployed from GitHub
- [ ] Environment variables added
- [ ] Deployment successful

### Post-Deploy:
- [ ] Bot added as admin to all 3 database channels
- [ ] Tested /start command
- [ ] Admin panel accessible
- [ ] Video upload tested
- [ ] Sheet code received
- [ ] Mini app integration tested

---

## 💡 Best Practices

### Video Naming:
✅ **Good:**
- `Bachelor Point S05E01`
- `Avatar 2 (2026)`
- `Money Heist Complete`

❌ **Bad:**
- `video_123.mp4`
- `new file`
- No title

### Caption Usage:
- First line = Title
- Keep it clean and descriptive
- Include season/episode info for series

### Database Organization:
- Adult → Adult Channel only
- Movies → Movie Channel
- Series → Series Channel
- Use proper naming conventions

### User Management:
- Regular broadcasts keep users engaged
- Monitor statistics
- Clean up banned users periodically

---

## 📱 Mini App Integration

### Sheet Structure:
```
Column A: Title
Column B: Image URL
Column C: Watch Links (format: Ep:vid,Ep:vid)
Column D: Region/Category
Column E: Download Links (same format as C)
```

### Example Row:
```
Bachelor Point S5 | https://img.url | S05E01:vid_1,S05E02:vid_2 | Series | S05E01:vid_3,S05E02:vid_4
```

---

## 🎬 Workflow

### Daily Operations:
1. Upload new videos to appropriate database channel
2. Bot automatically saves and sends code
3. Copy code to Google Sheet
4. Update mini app if needed
5. Monitor user activity
6. Respond to issues

### Weekly Tasks:
- Check statistics
- Broadcast important updates
- Clean up old analytics data
- Verify all channels active
- Test new features

### Monthly Maintenance:
- Review and optimize database
- Update welcome/help messages
- Check force join channels
- Analyze popular content
- Plan content strategy

---

## 🔐 Security Notes

### Keep Secure:
- ✅ Bot token
- ✅ MongoDB URI
- ✅ Admin ID
- ✅ Database channel IDs

### Can Share:
- ✅ Main channel link
- ✅ Backup channel link
- ✅ Mini app URL
- ✅ Bot username

### Never Share:
- ❌ .env file
- ❌ MongoDB password
- ❌ Database channel invite links
- ❌ Admin credentials

---

## 📈 Growth Tips

1. **Content Quality:** Upload high-quality videos
2. **Regular Updates:** Daily new content
3. **Engagement:** Use broadcast feature
4. **Categories:** Maintain all categories
5. **Mini App:** Keep it updated and functional
6. **Channels:** Keep force join channels active
7. **User Experience:** Fast, reliable service

---

## 🆘 Emergency Procedures

### Bot Down:
1. Check Railway deployment status
2. View logs for errors
3. Verify environment variables
4. Restart deployment
5. Check MongoDB connection

### Database Issues:
1. Verify MongoDB Atlas status
2. Check connection string
3. Verify IP whitelist
4. Test database connection
5. Contact MongoDB support if needed

### High Load:
1. Monitor Railway metrics
2. Check rate limiting
3. Optimize queries if needed
4. Consider upgrade if necessary

---

## 📞 Quick Links

- **MongoDB Atlas:** https://cloud.mongodb.com
- **Railway:** https://railway.app
- **Telegram BotFather:** https://t.me/BotFather
- **Mini App:** https://cinaflix-streaming.vercel.app/

---

**Keep this guide handy for quick reference! 📌**
