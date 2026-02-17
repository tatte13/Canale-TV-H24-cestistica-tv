FROM python:3.11-slim

# Installa ffmpeg e curl
RUN apt-get update && apt-get install -y ffmpeg curl

# Installa yt-dlp
RUN pip install --upgrade pip yt-dlp

# Imposta la working directory
WORKDIR /app

# Copia tutti i file nel container
COPY . .

# Avvia lo script principale
CMD ["python3", "app.py"]
