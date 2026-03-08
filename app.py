from flask import Flask, send_from_directory
import subprocess, os, threading, time

app = Flask(__name__)
os.makedirs("/mnt/stream", exist_ok=True)

# Playlist YouTube fornita
playlist = [
    "https://youtu.be/2UO2XdNl92k",
    "https://youtu.be/y1i-t_GaC2M",
    "https://youtu.be/vHw3MITYcE4",
    "https://youtu.be/HzY3KLzOn40",
    "https://youtu.be/d4sjXlaEVb0",
    "https://youtu.be/P3k9UfepZz0",
    "https://youtu.be/RMZMr43FB-4",
    "https://youtu.be/JszyRu6ctgQ",
    "https://youtu.be/qTdPMy6bfM4",
    "https://youtu.be/giFdq7q9CZw",
    "https://youtu.be/UnJ-N-ksP2Q?is=HK3ieCQRQe1oVob3",
    "https://youtu.be/2UO2XdNl92k"
]

# Funzione che genera HLS in loop infinito
def stream_loop():
    while True:
        for link in playlist:
            print(f"Streaming: {link}")
            cmd = f"yt-dlp -o - {link} | ffmpeg -i - -c:v libx264 -preset veryfast -f hls /mnt/stream/stream.m3u8"
            subprocess.run(cmd, shell=True)
            time.sleep(1)

# Avvia il loop in un thread separato
threading.Thread(target=stream_loop, daemon=True).start()

# Route per servire i file HLS
@app.route("/stream/<path:filename>")
def serve_stream(filename):
    return send_from_directory("/mnt/stream", filename)

# Root di test
@app.route("/")
def index():
    return "Web TV HLS attivo! Usa /stream/stream.m3u8 per il player"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
