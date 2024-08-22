import os
import sys
from datetime import datetime
from dotenv import load_dotenv
import openai
from openai import OpenAI
import json

load_dotenv()

# Fail if no file argument is provided
if len(sys.argv) < 2:
    print("Please provide an file")
    exit(1)

input_file = sys.argv[1]
input_file_name = os.path.basename(input_file)
input_file_dir = os.path.dirname(input_file)

client = OpenAI()

text_prompt = ""
response = ""

with open(input_file, "r", encoding="utf-8") as file:
    text_prompt = file.read()

try:
    system_prompt = "The following is the output of a group discussion."
    system_prompt += "Can you summarize the discussion?"
    system_prompt += "The summary should be concise and informative."
    system_prompt += "The summary should be in markdown format."
    system_prompt += "The summary should include the main points of the discussion."
    system_prompt += "The summary should give all possible options and a conclusion."
        
    completion = client.chat.completions.create(
        model=os.getenv("CHAT_MODEL") or "gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text_prompt}
        ]
    )
    response = completion.choices[0].message.content
except openai.OpenAIError as e:
  print(e.http_status)
  print(e.error)
  exit(1)

# Store the response in a file
if not os.path.isdir("group_summary"):
    os.mkdir("group_summary")

with open(f"group_summary/{input_file_dir}_{input_file_name}", "w", encoding="utf-8") as f:
    f.write(response)
