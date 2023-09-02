"""
Authors: 
MauDev, BriannaBalamV, 
Christian Can, 
Javier Can, 
Mariano Miranda

API's: openai - ElevenLabs - HuggingFace

"""

from elevenlabs import generate, play
import gradio as gr
import openai
from gradio.components import Textbox, Audio, Radio
from pydub import AudioSegment
import time

openai.api_key = ""
set_api_key = ""

def convert_to_mp3(file):
    audio = AudioSegment.from_file(file)    
    mp3_file = file.rsplit('.', 1)[0] + '.mp3'
    audio.export(mp3_file, format='mp3')
    return mp3_file

def transcribe_or_translate(audio_file, task, recording):
    if audio_file:
        file = audio_file
    elif recording:
        file = convert_to_mp3(recording)
    else:
        return "Please upload a valid audio file or record yourself."
    
    with open(file, 'rb') as f:
        if task == 'Transcription':
            text = openai.Audio.transcribe("whisper-1", f)
        elif task == 'Translation':
            text = openai.Audio.translate("whisper-1", f)
    return text.text

def ekten_voice(audio_file, task, recording):
    text = transcribe_or_translate(audio_file, task, recording)
    audio_data = generate(
        api_key= set_api_key,
        voice = "Bella",
        model="eleven_multilingual_v1",
        text=text
    )
    time.sleep(1)
    play(audio_data)
    return text

audio_file = Audio(label='Upload an audio file (must be in .mp3 or .wav)', type='filepath')
task = Radio(['Transcription', 'Translation'], label='Choose a task')
recording = Audio(label='Record yourself!', type='filepath', source='microphone')

output_text = Textbox(label='Transcribed or Translated text')

app = gr.Interface(fn=ekten_voice, 
                    inputs=[audio_file, task, recording], 
                    outputs=[output_text],
                    title='EktenAI - by Glow Up', 
                    description='EktenAI Improving Communication and Learning!')
app.launch()