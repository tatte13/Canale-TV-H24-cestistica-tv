FROM jrottenberg/ffmpeg:6.0-alpine

RUN apk add --no-cache bash python3 py3-pip
RUN pip install yt-dlp

WORKDIR /app

COPY . .

CMD ["bash", "run.sh"]
