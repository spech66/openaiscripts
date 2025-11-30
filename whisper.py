import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 

# Fail if no commandline argument is provided
if len(sys.argv) < 2:
    print("Please provide an audio file")
    exit(1)

audio_file_name = sys.argv[1]

# Check if file exists
if not os.path.isfile(audio_file_name):
    print("File does not exist")
    exit(1)

# If file is in ogg format convert it to mp3
if audio_file_name.endswith(".ogg"):
    mp3_file_name = audio_file_name[:-4] + ".mp3"
    os.system(f"ffmpeg -i '{audio_file_name}' -ab 320k '{mp3_file_name}'")
    audio_file_name = mp3_file_name

audio_file = open(audio_file_name, "rb")
client = OpenAI()
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    language="de",
)
print(transcript.text)

# write transcript to file
if not os.path.isdir("whisper_audio"):
    os.mkdir("whisper_audio")
with open(f"whisper_audio/{audio_file_name}.txt", "w", encoding="utf-8") as f:
    f.write(transcript.text)
