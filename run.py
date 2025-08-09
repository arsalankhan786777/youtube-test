import os
import yt_dlp
import json
import random
import time
from datetime import datetime

# Get pipeline number based on time
hour = datetime.utcnow().hour
if hour == 1: pipeline = 1
elif hour == 3: pipeline = 2  
elif hour == 12: pipeline = 3
elif hour == 15: pipeline = 4
else: pipeline = 1

print(f"🎯 Running Pipeline {pipeline}")

# Random delay (5 mins to 1 hour 50 mins)
delay = random.randint(300, 6600)
print(f"⏳ Waiting {delay//60} minutes...")
time.sleep(delay)

# Create folders
os.makedirs('videos', exist_ok=True)

# Load progress
try:
    with open('progress.json', 'r') as f:
        progress = json.load(f)
except:
    progress = {'uploaded': [], 'downloaded': []}

# Download videos
channel_url = os.environ.get('CHANNEL_URL')
print(f"📥 Downloading from {channel_url}")

ydl_opts = {
    'outtmpl': 'videos/%(title)s.%(ext)s',
    'format': 'best[ext=mp4]/best',
    'quiet': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(channel_url, download=False)
    videos = info.get('entries', [])
    
    # Download new videos only
    for video in videos:
        if video['id'] not in progress['downloaded']:
            print(f"Downloading: {video['title']}")
            ydl.download([video['webpage_url']])
            progress['downloaded'].append(video['id'])
            break  # One video per pipeline

# Save progress
with open('progress.json', 'w') as f:
    json.dump(progress, f)

print(f"✅ Pipeline {pipeline} completed!")
