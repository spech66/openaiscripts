import os
import sys
import re
from datetime import datetime
from dotenv import load_dotenv
import openai
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Source: https://gist.github.com/ivansaul/ac2794ecbddec6c54f1c2e62cccfc175
def parseYoutubeURL(url:str)->str:
   data = re.findall(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
   if data:
       return data[0]
   return ""

load_dotenv()

# Fail if no commandline argument is provided
if len(sys.argv) < 2:
    print("Please provide an video link oder video id")
    exit(1)
    
video_id = sys.argv[1]
if "youtube.com" in video_id:
    video_id = parseYoutubeURL(video_id)

# Get transcript and format it as text
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['de', 'en'], preserve_formatting=True)
formatter = TextFormatter()
txt_formatted = formatter.format_transcript(transcript)

client = OpenAI()

response = ""

try:
    completion = client.chat.completions.create(
        model=os.getenv("CHAT_MODEL") or "gpt-4o",
        messages=[
            {"role": "system", "content": "Summarize the video transcript."},
            {"role": "user", "content": txt_formatted}
        ]
    )
    response = completion.choices[0].message.content    
except openai.OpenAIError as e:
  print(e.http_status)
  print(e.error)
  exit(1)
  
print(response)

# Store the response in a file
if not os.path.isdir("yt_transcript_summary"):
    os.mkdir("yt_transcript_summary")

cur_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

with open(f"chat/{cur_time}.txt", "w", encoding="utf-8") as f:
    f.write(response)
