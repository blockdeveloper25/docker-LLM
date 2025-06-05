from openai import OpenAI
import os

client = OpenAI(
    base_url="http://localhost:12434/engines/v1",
    api_key='docker',
)

completion = client.chat.completions.create(
    model="ai/smollm2",
    messages=[
        {"role": "system", "content": "Answer the question in story format."},
        {"role": "user", "content": "tell me about current in gaza."},
    ]
)

print(completion.choices[0].message.content)