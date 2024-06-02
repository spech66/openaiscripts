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

response = ""

personas = []
with open("group_brainstorming_personas.json", "r") as file:
    personas = json.load(file)

print("Participants:")
for persona in personas:
    print(f"    {persona['name']}")

# try:
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "user", "content": text_prompt}
#         ]
#     )
#     response = completion.choices[0].message.content
# except openai.OpenAIError as e:
#   print(e.http_status)
#   print(e.error)
#   exit(1)    

# # Store the response in a file
# if not os.path.isdir("group_brainstorming"):
#     os.mkdir("group_brainstorming")

# cur_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# with open(f"group_brainstorming/{cur_time}.txt", "w", encoding="utf-8") as f:
#     f.write(text_prompt)
#     f.write("\n\n---\n\n")
#     f.write(response)
