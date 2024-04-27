import pathlib
import textwrap
import PIL.Image

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

GOOGLE_API_KEY = "AIzaSyC92Kq6UcsQWcqXoZfqNqY3zgZ9XYse-rg"
genai.configure(api_key=GOOGLE_API_KEY)



def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
#print(chat)
user_input = ""
while(user_input != "exit"):
    user_input = input("Input : ")
    response = chat.send_message(user_input, stream=True)

    for chunk in response:
        print(chunk.text)

print("\n**********Chat history**********\n")
for message in chat.history:
   print(to_markdown(f'**{message.role}**: {message.parts[0].text}').data)