FROM python:3.11-slim

# Installa ffmpeg
RUN apt-get update && apt-get install -y ffmpeg curl

# Installa yt-dlp
RUN pip install --upgrade pip yt-dlp

# Imposta working directory
WORKDIR /app

# Copia tutti i file del repository
COPY . .

# Comando unico in foreground
CMD python3 -u -c "import os, subprocess; os.makedirs('videos', exist_ok=True); import time; while True: subprocess.run(['yt-dlp','-a','links.txt','-f','mp4','-o','videos/%(title)s.%(ext)s']); subprocess.run(['ffmpeg','-re','-stream_loop','-1','-pattern_type','glob','-i','videos/*.mp4','-i','logo.png','-filter_complex','overlay=10:10','-c:v','libx264','-preset','veryfast','-maxrate','3500k','-bufsize','7000k','-c:a','aac','-b:a','160k','-f','flv','rtmp://a.rtmp.youtube.com/live2/q155-8c7t-u5de-2adx-6d1s']); time.sleep(5)"
