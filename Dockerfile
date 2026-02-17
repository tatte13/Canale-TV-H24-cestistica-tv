FROM python:3.11-slim

# Installa FFmpeg
RUN apt-get update && apt-get install -y ffmpeg curl

# Installa yt-dlp
RUN pip install --upgrade pip yt-dlp

# Imposta working directory
WORKDIR /app

# Copia tutti i file
COPY . .

# Comando principale
CMD ["python3", "app.py"]
