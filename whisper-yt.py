import os
import sys
import yt_dlp
import openai

# Fail if no commandline argument is provided
if len(sys.argv) < 2:
    print("Please provide an video link")
    exit(1)

video_file_url = sys.argv[1]

# https://github.com/yt-dlp/yt-dlp#filter-videos
ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

audio_file_name = ""
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_file_url, download=False)
    audio_file_name = ydl.prepare_filename(info)
    ydl.process_info(info)  # starts the download

# Check if file exists
if not os.path.isfile(audio_file_name):
    print("File {audio_file_name} does not exist")
    exit(1)

audio_file = open(audio_file_name, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)

# write transcript to file
if not os.path.isdir("whisper_yt"):
    os.mkdir("whisper_yt")
with open(f"whisper_yt/{audio_file_name}.txt", "w") as f:
    f.write(transcript["text"])
