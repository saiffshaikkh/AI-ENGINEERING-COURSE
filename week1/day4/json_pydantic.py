from httpx._client import ClientState
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("No API key found")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()

response_format={
    "type":"json_object"
}

sysem_prompt=f"""
This is a simple ticket extraction prompt
Output must be in JSON format.
And use the following schema:
{schema}
"""
message_system={
    "role":"system",
    "content":sysem_prompt
}

text="Hello My name is Saif. I broke up with my girlfriend. I have an iphone which is not working at all. My address is Mumbai. My email is abc@gmail.com. My contact number is 8850. "
prompt=f"""
This is a customer ticket. Please extract the personal information from this
{text}
"""
message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]

response=client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)

answer=response.choices[0].message.content
print(answer)

import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)