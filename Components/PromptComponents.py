import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = 'api key here'
role_play = "Act as a ..."
instruction = "Task: "
context = "In the context of..."
output = ""
specificity =""

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"{role_play} {instruction} {context} {output} {specificity}",
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=0.5,
  presence_penalty=0.0
)

print(response)