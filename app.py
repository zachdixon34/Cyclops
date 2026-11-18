from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
import os
from pathlib import Path
from yt_dlp import YoutubeDL
from urllib.parse import urlparse

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = Path(os.environ.get("DOWNLOAD_DIR", BASE_DIR / "downloads"))
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

print("Saving downloads to: ", DOWNLOAD_DIR)



@app.route("/")
def index():
    return render_template("index.html")

ALLOWED_DOMAINS = {"youtube.com", "youtu.be", "instagram.com", "x.com", "twitter.com"}

def is_allowed(url):
    host = (urlparse(url).hostname or "").lower()
    return any(host == d or host.endswith("." + d) for d in ALLOWED_DOMAINS)



@app.route("/download", methods=["POST"])
def download():
    # read link
    link = request.form.get("link")
    print("link recieved: ", link)

    # reject non youtube/instagram
    if not link or not is_allowed(link):
        return jsonify({"ok": False, "error": "Only Youtube and Instagram"}), 400

    #yt-dlp settings
    ydl_opts = {
        "outtmpl": str(DOWNLOAD_DIR / "%(title)s.%(ext)s"),
        "format": "bv*[vcodec^=avc1]+ba[ext=m4a]/b[ext=mp4]/b",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "no_color": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info=ydl.extract_info(link, download=True)
            filepath = Path(info["requested_downloads"][0]["filepath"])
        return jsonify({"ok": True, 
                        "title": info.get("title"),
                        "url": url_for("serve_file", filename=filepath.name),
                         "download_url": url_for("serve_file", filename=filepath.name, dl=1),})
        
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.route("/files/<path:filename>")
def serve_file(filename):
    as_attachment = request.args.get("dl") == "1"
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=as_attachment)

@app.route("/files", methods=["DELETE"])
def delete_all():
    deleted, failed = 0, []
    for f in DOWNLOAD_DIR.iterdir():
        if f.is_file():
            try:
                f.unlink()
                deleted += 1
            except OSError as e:
                failed.append(f.name)
                print("Could not delete", f, e)
    return jsonify({"ok": not failed, "deleted": deleted, "failed": failed})



if __name__ == "__main__":
    app.run(debug=True)

