import os
import sys
from datetime import datetime
from dotenv import load_dotenv
import openai
from openai import OpenAI
import json

load_dotenv()

# Fail if no commandline argument is provided
if len(sys.argv) < 2:
    print("Please provide an text")
    exit(1)

text_prompt = sys.argv[1]

client = OpenAI()

response_full = ""

participants = []
with open("group_brainstorming_participants.json", "r") as file:
    participants = json.load(file)

try:
    for participant in participants:
        print(f"Participant: {participant['name']}")
        
        system_prompt = "You are in a group brainstorming session with your team. You are discussing the topic provided by the user. "
        system_prompt += f"You are '{participant['name']}'. "
        system_prompt += f" {participant['role']}. "
        system_prompt += "Write all the ideas that come to your mind."
        
        completion = client.chat.completions.create(
            model=os.getenv("CHAT_MODEL") or "gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text_prompt}
            ]
        )
        response = completion.choices[0].message.content
        
        response_full += f"## {participant['name']}\n\n"
        response_full += response
        response_full += "\n\n---\n\n"        
except openai.OpenAIError as e:
  print(e.http_status)
  print(e.error)
  exit(1)

# Store the response in a file
if not os.path.isdir("group_brainstorming"):
    os.mkdir("group_brainstorming")

cur_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

with open(f"group_brainstorming/{cur_time}.md", "w", encoding="utf-8") as f:
    f.write(f"# Group brainstorming {cur_time}\n\n")
    f.write(text_prompt)
    f.write("\n\n---\n\n")
    f.write(response_full)
