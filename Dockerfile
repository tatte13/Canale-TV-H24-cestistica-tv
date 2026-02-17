# Base image con ffmpeg su Alpine
FROM jrottenberg/ffmpeg:6.0-alpine

# Aggiorna pacchetti e installa Python, pip, bash e curl
RUN apk add --no-cache python3 py3-pip bash curl

# Aggiorna pip e installa yt-dlp
RUN pip3 install --upgrade pip
RUN pip3 install yt-dlp

# Imposta la working directory
WORKDIR /app

# Copia tutti i file del repository nella working directory
COPY . .

# Comando automatico all'avvio del container
CMD ["bash", "run.sh"]
