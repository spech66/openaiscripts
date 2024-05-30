# OpenAI Scripts

Wrapper for OpenAI API. Use ChatGPT, DALL-E, and other models (TTS, STT, ...). Allows conversion between text, image, audio, and video.

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

## Scripts

* dalle: text to image
  * `python dalle.py "a bear in a forest"`
* whisper: audio to text
  * `python whisper.py test.ogg`
* whisper-yt: youtube to text
  * `python whisper-yt.py https://www.youtube.com/shorts/pB5Pfq-Aa3g`
* voice: text to speech
  * `python voice.py "Hello, how are you?"`

## Development

### Update SDK and requirements

```sh
pip install --upgrade openai
pip freeze > requirements.txt
```
