import os
import subprocess
import time

# Crea cartella videos
os.makedirs("videos", exist_ok=True)

STREAM_KEY = "q155-8c7t-u5de-2adx-6d1s"

while True:
    # Scarica tutti i video YouTube da links.txt
    subprocess.run(["yt-dlp", "-a", "links.txt", "-f", "mp4", "-o", "videos/%(title)s.%(ext)s"])

    # Avvia lo streaming con FFmpeg
    subprocess.run([
        "ffmpeg",
        "-re",
        "-stream_loop", "-1",
        "-pattern_type", "glob",
        "-i", "videos/*.mp4",
        "-i", "logo.png",
        "-filter_complex", "overlay=10:10",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-maxrate", "3500k",
        "-bufsize", "7000k",
        "-c:a", "aac",
        "-b:a", "160k",
        "-f", "flv",
        f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"
    ])

    # Attesa 5 secondi prima di ripetere
    time.sleep(5)
