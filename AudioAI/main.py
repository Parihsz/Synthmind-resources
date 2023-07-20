import os
import openai
from recording import *

openai.api_key = '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'

memory = []

while True:
    recording(5, "recording.wav")
    audio_file = "recording.wav"
    recognized_text = transcribe_audio(audio_file)

    user_input = recognized_text
    print("Finished recording")

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
    output_file = "response.wav"
    text = response_text
    text_to_speech(text, output_file)

    if len(memory) >= 6:
        memory.pop(0)
        memory.pop(1)
    memory.append("user said:" + user_input)
    memory.append("assistant said:" + response_text)