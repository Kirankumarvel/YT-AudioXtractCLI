
# 🎵 YouTube Audio Extractor CLI - `yt_audio_xtract.py`

Easily extract high-quality **MP3 audio** from YouTube videos right from your terminal using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) and `ffmpeg`.

---

## 📦 Features

- Downloads best available audio from any YouTube video.
- Converts to **MP3 format** with 192kbps quality.
- CLI-based — clean, fast, and minimal.
- Automatically organizes downloads into an `/output` folder.
- No bloat. One Python file. Works out of the box.

---

## 🚀 Getting Started

### 1. Clone the repo or download `yt_audio_xtract.py`

```bash
git clone https://github.com/Kirankumarvel/yt-audio-extract-cli.git
cd yt-audio-extract-cli
````

### 2. Install Dependencies

Make sure you have Python 3.7+ installed.

```bash
pip install -r requirements.txt
```

Also, **ffmpeg** must be installed and available in your system PATH.

* 🔗 [Install FFmpeg](https://ffmpeg.org/download.html)

### 3. Run the Script

```bash
python yt_audio_xtract.py
```

Then paste your YouTube video URL when prompted.

---

## 📁 Output

* Downloads will be saved in the `output/` folder.
* Filenames will match the video title.
* Format: `.mp3` (converted via FFmpeg)

---

## 📄 Example

```bash
==========================================
      🎵 YouTube Audio Extractor 🎵
        Powered by yt-dlp & FFmpeg
==========================================

🔸 Enter YouTube video URL: https://www.youtube.com/watch?v=abcd1234

🔗 Downloading audio from: https://www.youtube.com/watch?v=abcd1234

✅ Audio downloaded successfully!
```

---

## 🧰 Requirements

* `yt-dlp` – YouTube video/audio downloader
* `ffmpeg` – Converts audio stream to `.mp3`

Install via:

```bash
pip install yt-dlp
```

---

## 📂 Files

* `yt_audio_xtract.py` – Main Python script
* `requirements.txt` – Python dependencies (`yt-dlp`)

---

## 🧠 Why `yt-dlp`?

Unlike `pytube`, `yt-dlp` is:

* Actively maintained 🔧
* Fast & reliable ⚡
* Supports more YouTube formats and sites 🌐

---

## 🛡️ License

MIT License © 2025 Kiran Kumar

---

## 🙌 Contributions

Feel free to fork, star ⭐, and improve this script.


