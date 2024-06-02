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

print("WIP")

# Store the resposne in a file
if not os.path.isdir("group_brainstorming"):
    os.mkdir("group_brainstorming")

cur_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

with open(f"group_brainstorming/{cur_time}.txt", "w", encoding="utf-8") as f:
    f.write(text_prompt)
    f.write("\n\n---\n\n")
    f.write(response)
