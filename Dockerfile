FROM jrottenberg/ffmpeg:6.0-alpine

# Installazioni necessarie
RUN apk add --no-cache python3 py3-pip bash curl

# Aggiorna pip e installa yt-dlp
RUN pip3 install --upgrade pip
RUN pip3 install yt-dlp

# Imposta la working directory
WORKDIR /app

# Copia tutto il repository
COPY . .

# Esegui tutto direttamente da Docker CMD come comando shell
CMD ["sh", "-c", "chmod +x run.sh && ./run.sh"]
