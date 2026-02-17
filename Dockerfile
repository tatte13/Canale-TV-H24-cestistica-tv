FROM python:3.11-slim

RUN apt-get update && apt-get install -y ffmpeg curl

RUN pip install --upgrade pip yt-dlp

WORKDIR /app

COPY . .

CMD ["python3", "app.py"]
