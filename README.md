# howToUseNewLamaChangeCode (text to tet conversion)
### when we will use lama version that is train on 8 billion perameter data
export GROQ_API_KEY=<your-api-key-here>   #######**** (first use this)****
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

print(chat_completion.choices[0].message.content) ######3****( second than use this )****
###### in case of wanting to use different lama version that is trained on more data like
Gemma 7B
Model ID: gemma-7b-it
Developer: Google
Context Window: 8,192 toke
#####than we can cut this in line 19 **llama3-8b-8192** and paste **gemma-7b-it****** of new model 








