while true
do
yt-dlp -a links.txt -f mp4 -o "%(title)s.%(ext)s"
ffmpeg -re -stream_loop -1 -pattern_type glob -i "*.mp4" \
-i logo.png -filter_complex "overlay=10:10" \
-c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k \
-c:a aac -b:a 160k \
-f flv rtmp://a.rtmp.youtube.com/live2/q155-8c7t-u5de-2adx-6d1s
done
