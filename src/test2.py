"""
Author: MauDev

Key: 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
"""


import gradio as gr
import openai
from gradio.components import Textbox,Audio,Radio

def transcribe_or_translate(api_key, audio_file, task):
    openai.api_key = api_key
    with open(audio_file, 'rb') as f:
        if task == 'Transcription':
            text = openai.Audio.transcribe("whisper-1", f)
        elif task == 'Translation':
            text = openai.Audio.translate("whisper-1", f)
    return text.text

def transcribe(audio):
    
    #time.sleep(3)
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text

api_key = Textbox(label='Enter API Key')
audio_file = Audio(label='Upload audio file (either mp3 or wav)', type='filepath')
task = Radio(['Transcription', 'Translation'], label='Choose a task')

output_text = Textbox(label='Transcribed or Translated text')

app = gr.Interface(fn=transcribe_or_translate, transcribe=transcribe(audio),
                    inputs=[api_key, audio_file, task, gr.inputs.Audio(source="microphone", type="filepath")], 
                    outputs= output_text,
                    title='Universal Audio Transcriber/Translator (UPY)', 
                    description='Choose an audio to translate or transcribe.')
app.launch()