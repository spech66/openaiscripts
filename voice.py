import os
import sys
from datetime import datetime
from dotenv import load_dotenv
import openai
from openai import OpenAI
from pathlib import Path

load_dotenv() 

# Fail if no commandline argument is provided
if len(sys.argv) < 2:
    print("Please provide an text")
    exit(1)

text_prompt = sys.argv[1]

client = OpenAI()

speech_file_path = ""

# Stream audio and save it to file in the voice folder
if not os.path.isdir("voice"):
    os.mkdir("voice")
    
cur_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

try:
    speech_file_path = f"voice/{cur_time}.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice=os.getenv("SPEECH_VOICE") or "alloy",
        input=text_prompt
    )

    response.stream_to_file(speech_file_path)
except openai.OpenAIError as e:
  print(e.http_status)
  print(e.error)
  exit(1)

print(speech_file_path)
