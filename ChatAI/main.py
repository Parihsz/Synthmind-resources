import os
import openai

openai.api_key = 'api key here'

memory = []

while True:
    user_input = input(" ")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt='\n'.join(
            memory) + "\nuser input: " + user_input + ", please act as assistant to response to user input",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    response_text = response['choices'][0]['text']
    print(response_text)

    if len(memory) >= 6:
        memory.pop(0)
        memory.pop(1)
    memory.append("user said:" + user_input)
    memory.append("assistant said:" + response_text)