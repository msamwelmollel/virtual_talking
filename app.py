#venv/Lib/site-packages/speech_recognition/recognizers/google.py

from openai import OpenAI
import os
import time
from utils import record_audio, play_audio

client = OpenAI()

while True:
  record_audio('test.wav')
  audio_file= open('test.wav', "rb")
  transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
  )

  print(transcription.text)
  text = transcription.text
  # text = "How can I start my day learning new thing"

  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      # {"role": "system", "content": "You are my assitance named Eunice. Please answer in short sentences and be kind."},
      {"role": "system", "content": "You are my assitance named Eunice. Please answer translate to swahili"},
      {"role": "user", "content": f"Please answer: {text}"},
    ]
  )

  print(response.choices[0].message.content)

  response = client.audio.speech.create(
    model="tts-1",
    # voice="nova",
    voice="alloy",
    input=response.choices[0].message.content
  )




  response.stream_to_file('output.mp3')
  play_audio('output.mp3')
  # time.sleep(10)
