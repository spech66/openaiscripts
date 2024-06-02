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

# group_decisionmeeting

print("WIP")
