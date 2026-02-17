import subprocess
import time

STREAM_KEY = "q155-8c7t-u5de-2adx-6d1s"

while True:
    # Scarica temporaneamente tutti i video YouTube
    # -o "-" li manda direttamente a FFmpeg senza salvare su disco
    # (versione più semplice, ma yt-dlp salva in memoria temporanea)
    subprocess.run([
        "yt-dlp",
        "-a", "links.txt",
        "-f", "mp4",
        "-o", "%(title)s.%(ext)s"  # scarica in cartella temporanea
    ])

    # Prende tutti i mp4 appena scaricati
    mp4_files = subprocess.getoutput("ls *.mp4").splitlines()
    if not mp4_files:
        print("Nessun video disponibile, riprovo tra 10 secondi...")
        time.sleep(10)
        continue

    # Unisce tutti i video scaricati in streaming
    subprocess.run([
        "ffmpeg",
        "-re",
        "-stream_loop", "-1",
        "-i", "concat:" + "|".join(mp4_files),
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

    # Rimuove i video scaricati per ricominciare il loop
    subprocess.run(["rm", "-f"] + mp4_files)

    # Attesa 5 secondi prima di scaricare di nuovo
    time.sleep(5)
