import os
import sys
import yt_dlp
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

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
client = OpenAI()
transcript = client.audio.transcriptions.create(
    model="gpt-4o-transcribe",
    file=audio_file,
)

print(transcript.text)

# write transcript to file
if not os.path.isdir("whisper_yt"):
    os.mkdir("whisper_yt")
cur_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
with open(f"whisper_yt/{cur_time}_{audio_file_name}.txt", "w") as f:
    f.write(transcript.text)
