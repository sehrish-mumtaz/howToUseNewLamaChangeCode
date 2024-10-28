#i want to make a realtime chatbot for voice to voice. the model which i will use to convert audio to text is openai whisper. then will use groq api key to interact with the llm here are the documentation for the groq
import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
then i will use gtts model to convert the text from llm it into audio. i will be working on google colad and use gradio to make the interface and will upload it on huggingface.

(first code) !pip install openai-whisper groq gtts gradio (first code)
(second code) 
import gradio as gr
import os
import whisper
from groq import Groq
from gtts import gTTS

# Load Whisper model for audio transcription
model = whisper.load_model("base")

# Set up Groq API client with your API key
os.environ["GROQ_API_KEY"] = "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"
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def chatbot(audio_file):
    # Transcribe audio to text
    transcription = model.transcribe(audio_file)["text"]

    # Get response from LLM using Groq API
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": transcription}
        ],
        model="llama3-8b-8192",
    )
    response_text = chat_completion.choices[0].message.content

    # Convert response text to audio
    tts = gTTS(response_text)
    tts.save("response_audio.mp3")

    return response_text, "response_audio.mp3"

# Gradio Interface
gr.Interface(
    fn=chatbot,
    inputs=gr.Audio(type="filepath"),
    outputs=[gr.Textbox(label="Chatbot Text Response"), gr.Audio(type="filepath", label="Chatbot Audio Response")],
    title="Voice-to-Voice Chatbot",
    description="Speak to the chatbot, and it will respond with both text and audio."
).launch()


# my complete application on huggingface
https://huggingface.co/spaces/SehrishMumtaz/voiceToVoiceSM


