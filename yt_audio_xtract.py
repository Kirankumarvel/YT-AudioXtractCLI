# yt_audio_xtract.py
# This script downloads audio from a YouTube video using the pip install yt-dlp library.
# Install pytube with: pip install yt-dlp

import yt_dlp
import os

def print_banner():
    banner = """
==========================================
      🎵 YouTube Audio Extractor 🎵
        Powered by yt-dlp & FFmpeg
==========================================
"""
    print(banner)

def download_audio_yt_dlp(url, output_folder="output"):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
    }

    print("\n🔗 Downloading audio from:", url)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\n✅ Audio downloaded successfully!\n")

def main():
    print_banner()
    url = input("🔸 Enter YouTube video URL: ").strip()
    if url:
        download_audio_yt_dlp(url)
    else:
        print("⚠️  No URL provided. Exiting.")

if __name__ == "__main__":
    main()
