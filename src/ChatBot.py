import gradio as gr
from gradio.components import Textbox,Audio,Radio
from transformers import EmbeddedTransformer
import openai

openai.api_key = ""

def chat(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        temperature = 0.8,
    )

    message = completions.choices[0].text
    return message.strip()

def chatbot(input, history=[]):
    output = chat(input)
    history.append((input, output))
    return history, history

def embedded_message(input, history=[]):
    emb = EmbeddedTransformer(input)
    for message in enumerate(messages):
        if message[0].text:
            return emb
        else:
            return "We can't reach the message to emb"

gr.Interface(
    fn = chatbot,
    inputs= ["text", "state"],
    outputs= ["chatbot", "state"],
    title="Cutomized Recommendation ChatBot",
    description="Enter the city and the places that you want to visit and if you want to, the time per place."
).launch()