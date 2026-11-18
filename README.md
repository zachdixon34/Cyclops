# Cyclops

A simple program for downloading and managing videos from websites.

### Supported Websites
- YouTube (`youtube.com`)
- Instagram (`instagram.com`)
- X / Twitter (`x.com`)

---

## Requirements & Setup

### Requirements
- Python 3
- FFmpeg

### Setup
Setup instructions are for **Windows**, but the app can also be deployed on Linux.

#### 1. Install Python Packages
All packages are listed in `requirements.txt` for external deployment.

```bash
pip install -r requirements.txt
```

Or install them one at a time:

```bash
pip install flask
pip install "yt-dlp[default]"
pip install gunicorn
```

#### 2. Install FFmpeg
yt-dlp uses FFmpeg to merge and convert video and audio files.

```bash
winget install Gyan.FFmpeg
```

---

## Running

1. To verify the install, run this in a terminal:
   ```bash
   python .\app.py
   ```
2. Open the local URL shown in the console and try downloading a YouTube video.
3. If it works, deploy it wherever you need it.

---

## Use Cases

1. **Short-term local use**
   - Run it on your own machine for small, quick tasks.
2. **Embedded deployment (long-term)**
   - Deploy it to an always-on device so it runs 24/7.
   - A server or NAS works well for this. A Linux-based system is recommended.
3. **External deployment**
   - Host it as a service for other people to use.

---

## Versions

### v1.0
- Download videos
- Purge **all** videos from the download folder
- Viewing previously downloaded videos is not supported yet