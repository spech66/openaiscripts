import os
import sys
from datetime import datetime
import urllib.request
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()

# Fail if no commandline argument is provided
if len(sys.argv) < 2:
    print("Please provide an text")
    exit(1)

text_prompt = sys.argv[1]

client = OpenAI()

response = ""

try:
    completion = client.chat.completions.create(
        model=os.getenv("CHAT_MODEL") or "gpt-4o",
        messages=[
            {"role": "user", "content": text_prompt}
        ]
    )
    response = completion.choices[0].message.content
except openai.OpenAIError as e:
  print(e.http_status)
  print(e.error)
  exit(1)    

print(response)

# Store the response in a file
if not os.path.isdir("chat"):
    os.mkdir("chat")
    
cur_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

with open(f"chat/{cur_time}.txt", "w", encoding="utf-8") as f:
    f.write(text_prompt)
    f.write("\n\n---\n\n")
    f.write(response)
