FROM python:3.11-slim

# Installa ffmpeg e curl
RUN apt-get update && apt-get install -y ffmpeg curl

# Installa yt-dlp
RUN pip install --upgrade pip yt-dlp

WORKDIR /app

COPY . .

CMD ["python3", "app.py"]
