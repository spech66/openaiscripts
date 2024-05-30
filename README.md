# OpenAI Scripts

## Setup

Install packages (with admin permissions)

```sh
pip install python-dotenv
pip install openai
```

Update SDK: `pip install --upgrade openai` (with admin permissions).

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
