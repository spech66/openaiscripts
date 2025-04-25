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

image_url = ""

try:
    image_model = os.getenv("IMAGE_MODEL") or "gpt-image-1"
    if image_model == "gpt-image-1":
        response = client.images.generate(
            model=image_model,
            prompt=text_prompt,
            size=os.getenv("IMAGE_SIZE") or "auto",
            quality=os.getenv("IMAGE_QUALITY") or "auto",
            background=os.getenv("IMAGE_BACKGROUND") or "auto",
            n=1,
        )
    else:
        response = client.images.generate(
            model=image_model,
            prompt=text_prompt,
            size=os.getenv("IMAGE_SIZE") or "auto",
            quality=os.getenv("IMAGE_QUALITY") or "standard",
            n=1,
        )

    image_url = response.data[0].url
except openai.OpenAIError as e:
  print(e.http_status)
  print(e.error)
  exit(1)

print(image_url)

# Download image using python and save it to file in the image folder
if not os.path.isdir("image"):
    os.mkdir("image")
with urllib.request.urlopen(image_url) as response:
    cur_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"image/{cur_time}.png", "wb") as f:
        f.write(response.read())
    with open(f"image/{cur_time}.txt", "wb") as f:
        f.write(text_prompt.encode("utf-8"))
