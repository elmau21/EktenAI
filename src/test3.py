"""
Authors: MauDev, BriannaBalamV

Key:

"""


import gradio as gr
import openai
from gradio.components import Textbox, Audio, Radio
from pydub import AudioSegment

def convert_to_mp3(file):
    audio = AudioSegment.from_file(file)    
    mp3_file = file.rsplit('.', 1)[0] + '.mp3'
    audio.export(mp3_file, format='mp3')
    return mp3_file

def transcribe_or_translate(api_key, audio_file, task, recording):
    openai.api_key = api_key
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
    
    audio = whisper.load_audio(file)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_melspectrogram(audio).to(model.device)

    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text

api_key = Textbox(label='Enter API Key')
audio_file = Audio(label='Upload audio file (either mp3 or wav)', type='filepath')
task = Radio(['Transcription', 'Translation'], label='Choose a task')
recording = Audio(label='Record yourself!', type='filepath', source='microphone')

output_text = Textbox(label='Transcribed or Translated text')

app = gr.Interface(fn=transcribe_or_translate, 
                    inputs=[api_key, audio_file, task, recording], 
                    outputs=output_text,
                    title='Universal Audio Transcriber/Translator (UPY)', 
                    description='Choose an audio to translate or transcribe.')
app.launch()
