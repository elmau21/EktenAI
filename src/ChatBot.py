"""
key: 

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

"""

import gradio as gr
from gradio.components import Textbox,Audio,Radio
import openai

openai.api_key = ""

def chat(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 100,
        n = 1,
        temperature = 0.8,
    )

    message = completions.choices[0].text
    return message.strip()

def chatbot(input, history=[]):
    output = chat(input)
    history.append((input, output))
    return history, history

gr.Interface(
    fn = chatbot,
    inputs= ["text", "state"],
    outputs= ["chatbot", "state"]
).launch()