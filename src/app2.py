"""
Authors: MauDev, BriannaBalamV

Key:
"""


import gradio as gr
import openai
from gradio.components import Textbox,Audio,Radio
import numpy as np

def transcribe_or_translate(api_key, audio_file, task, recording):
    openai.api_key = api_key
    with open(audio_file, 'rb') as f:
        if task and recording == 'Transcription':
            text = openai.Audio.transcribe("whisper-1", f)
        elif task and recording == 'Translation':
            text = openai.Audio.translate("whisper-1", f)
    return text.text




api_key = Textbox(label='Enter API Key')
audio_file = Audio(label='Upload audio file (either mp3 or wav)', type='filepath')
task = Radio(['Transcription', 'Translation'], label='Choose a task')
recording = Audio(label='Record yourself!', type='filepath', source='microphone')

output_text = Textbox(label='Transcribed or Translated text')

app = gr.Interface(fn=transcribe_or_translate, 
                    inputs=[api_key, audio_file, task, recording], 
                    outputs= output_text,
                    title='Universal Audio Transcriber/Translator (UPY)', 
                    description='Choose an audio to translate or transcribe.')
app.launch()

