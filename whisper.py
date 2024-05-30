import os
import sys
import openai

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
    os.system(f"ffmpeg -i '{audio_file_name}' -ab 320k '{audio_file_name}.mp3'")
    audio_file_name = f"{audio_file_name}.mp3"

audio_file= open(audio_file_name, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file, language="de")
print(transcript)

# write transcript to file
if not os.path.isdir("whisper_audio"):
    os.mkdir("whisper_audio")
with open(f"whisper_audio/{audio_file_name}.txt", "w") as f:
    f.write(transcript["text"])
