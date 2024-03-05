# EktenAI - Glow Up
Overview

This repository contains the source code for EktenAI - Glow Up, a Python application leveraging the ElevenLabs, Gradio, OpenAI, and Pydub libraries to transcribe or translate audio files and generate corresponding synthesized voices. The purpose of this application is to facilitate seamless communication by overcoming language barriers.
Features

    Transcription and Translation: The application supports both transcription and translation of audio content, enabling users to understand spoken words in their preferred language.

    User-Friendly Interface: Gradio provides an intuitive and user-friendly interface for uploading audio files, recording audio, selecting the desired task (transcription or translation), and visualizing the transcribed or translated text along with the generated audio.

    Multilingual Synthesis: EktenAI utilizes the ElevenLabs API to generate high-quality synthesized voices in multiple languages, enhancing the user experience and promoting cross-cultural communication.

Getting Started

To use EktenAI - Glow Up, follow these steps:

    Clone this repository to your local machine.

    Install the required dependencies using the following command:

    bash

pip install elevenlabs gradio openai pydub

Obtain API keys for the ElevenLabs and OpenAI services.

Replace the placeholder values for openai.api_key and set_api_key with your actual API keys.

Run the script to launch the Gradio interface:

bash

    python <script_name>.py

    Use the interface to upload audio files, record audio, select the task (transcription or translation), and experience the seamless generation of transcribed or translated text along with synthesized audio.

Note

Ensure that the audio file is in either .mp3 or .wav format for proper processing.
Acknowledgments

    ElevenLabs for providing the Eleven Multilingual API.
    Gradio for simplifying the creation of user interfaces for machine learning models.
    OpenAI for the powerful language models and audio processing capabilities.
