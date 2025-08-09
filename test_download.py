#!/usr/bin/env python3
import yt_dlp
import os

print("🚀 Starting Video Download Test...")

# Simple test URL
test_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Create folder
os.makedirs('test_videos', exist_ok=True)

# Download options
ydl_opts = {
    'outtmpl': 'test_videos/%(title)s.%(ext)s',
    'format': 'best[filesize<50M]/best',
    'quiet': False,
    'no_warnings': False,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"📊 Downloading: {test_url}")
        ydl.download([test_url])
        print("✅ Download successful!")
except Exception as e:
    print(f"❌ Error: {e}")
