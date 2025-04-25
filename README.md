# OpenAI Scripts

OpenAI scripts for various tasks including brainstorming, decision meetings, chat, text to image, audio to text, text to speech, etc.

## Functionality

* chat: ChatGPT response
  * `python chat.py "What is the capital of germany?"`
* image: text to image
  * `python image.py "a bear in a forest"`
* whisper: audio to text (e.g. your WhatsApp voice notes)
  * `python whisper.py test.ogg`
* whisper-yt: youtube to text (depends on youtube-dl and ffmpeg - YouTube might block this from time to time)
  * `python whisper-yt.py https://www.youtube.com/shorts/pB5Pfq-Aa3g`
* yt-transcript-summary: extract transcript from YouTube video and summarize it
  * `python yt-transcript-summary.py https://www.youtube.com/watch?v=undmT0Jh7H4`
* voice: text to speech
  * `python voice.py "Hello, how are you?"`
* group-brainstorming: Multiple participants brainstorming (see json file for participants)
  * `python group-brainstorming.py "What are the best ways to improve your health?"`
* group-decisionmeeting: Multiple participants in a decision meeting (see json file for participants)
  * `python group-decisionmeeting.py "I want to work in a startup, what should I do? Current job is boring but stable. I have a family to feed. I am afraid of taking risks."`
* group-summary: Summarize a meeting or brainstorming session
  * `python group-summary.py (group_decisionmeeting|group_brainstorming)/filename.md`

## Setup

### Virtual environment

```sh
virtualenv aienv
source aienv/bin/activate
pip install -r requirements.txt
```

### Local installation

Install packages (with admin/sudo permissions).

```sh
pip install -r requirements.txt
```

Or using manual installation.

```sh
pip install python-dotenv
pip install openai
```

### OpenAI API key

Add your API key to the .env file (see env.sample).

`OPENAI_API_KEY="sk-xxxxxx"`

## Development

### Update SDK and requirements

```sh
pip install --upgrade openai
pip freeze > requirements.txt
```
