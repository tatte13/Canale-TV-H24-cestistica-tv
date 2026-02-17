import subprocess
import time

STREAM_KEY = "q155-8c7t-u5de-2adx-6d1s"

# Leggi i link da links.txt
with open("links.txt", "r") as f:
    links = [line.strip() for line in f if line.strip()]

while True:
    for link in links:
        print(f"Streaming video: {link}")
        
        # Scarica temporaneamente il video
        filename = "temp.mp4"
        subprocess.run([
            "yt-dlp", "-f", "mp4", "-o", filename, link
        ])
        
        # Se il download ha avuto successo
        subprocess.run([
            "ffmpeg",
            "-re",
            "-i", filename,
            "-i", "logo.png",
            "-filter_complex", "overlay=10:10",
            "-c:v", "libx264",
            "-preset", "veryfast",
            "-maxrate", "3500k",
            "-bufsize", "7000k",
            "-c:a", "aac",
            "-b:a", "160k",
            "-f", "flv",
            f"rtmp://a.rtmp.youtube.com/live2/{q155-8c7t-u5de-2adx-6d1s}"
        ])
        
        # Cancella il file temporaneo
        subprocess.run(["rm", "-f", filename])
        
    # Ripeti la playlist all’infinito
    time.sleep(5)
    # Attesa 5 secondi prima di scaricare di nuovo
    time.sleep(5)
