from openai import OpenAI
from src.prompt import system_instruction

client = OpenAI()

#creating the prompt for system
messages = [
    {"role":"system","content":system_instruction} #here, we are giving prompt to the system/LLM which we import from prompt.py inside src
    #folder
]

def ask_order(messages, model="gpt-3.5-turbo", temperature = 0):

    response = client.chat.completions.create(
        model = model,
        messages= messages,
        temperature = temperature
    )

    return response.choices[0].message.content #to get the reponse of prompt from our system