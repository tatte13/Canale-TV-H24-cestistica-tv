import subprocess
import time
import os

# Chiave live di YouTube già inserita
STREAM_KEY = "q155-8c7t-u5de-2adx-6d1s"

# Leggi i link da links.txt
with open("links.txt", "r") as f:
    links = [line.strip() for line in f if line.strip()]

while True:
    for link in links:
        print(f"Scaricando video: {link}")
        filename = "temp.mp4"

        # Scarica il video con yt-dlp
        subprocess.run(
            ["yt-dlp",
 "--cookies", "cookies.txt",
 "-f", "bv*+ba/b",
 "--merge-output-format", "mp4",
 "-o", filename,
 link]
        )

        # Controlla se il download è avvenuto
        if not os.path.exists(filename):
            print("Errore: video non scaricato, salto questo link")
            continue

        print(f"Streaming video: {filename}")

        # Avvia FFmpeg per lo streaming con logo overlay
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
            f"rtmp://a.rtmp.youtube.com/live2/q155-8c7t-u5de-2adx-6d1s"
        ])

        # Cancella il file temporaneo
        if os.path.exists(filename):
            os.remove(filename)

    # Loop infinito della playlist
    time.sleep(5)
