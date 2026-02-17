FROM jrottenberg/ffmpeg:6.0-alpine

# Installa Python, pip, bash, curl
RUN apk add --no-cache python3 py3-pip bash curl

# Aggiorna pip e installa yt-dlp
RUN pip3 install --upgrade pip
RUN pip3 install yt-dlp

# Imposta working directory
WORKDIR /app

# Copia tutti i file del repository
COPY . .

# Comando unico, tutto inline, in foreground
CMD bash -c "mkdir -p videos && while true; do yt-dlp -a links.txt -f mp4 -o 'videos/%(title)s.%(ext)s'; ffmpeg -re -stream_loop -1 -pattern_type glob -i 'videos/*.mp4' -i logo.png -filter_complex 'overlay=10:10' -c:v libx264 -preset veryfast -maxrate 3500k -bufsize 7000k -c:a aac -b:a 160k -f flv rtmp://a.rtmp.youtube.com/live2/q155-8c7t-u5de-2adx-6d1s; sleep 5; done"
