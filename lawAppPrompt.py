## 1st prompt
legal case summery
description: built an application that retrieve legal cases, policies and regulation based on specific keyword generates summeries or case  comparasion
feature: ingest legal documents and case files(allows the model to highlight similar cases or plain-language explanation.
use case: helping law student or lawyer with quick case research and brief summery
i have to prepare a rag application using google colab and streamlit suggest me some model and database. additionaly, i cannot use paid OPEN AI api key, therefore suggest model that run using groq api key which description is as under.
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

## second prompt
now using dataset from huggig face suggested model by giving me a complete code for the application. i will be running codes on google colab than will make repo in github and deploy it on streamlit
suggest model that run using groq api key, description is as under.
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
