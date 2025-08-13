## A terminal chat-app with gemini
## using the 'chats' functionality of the client object

from google import genai
from dotenv import load_dotenv
load_dotenv()
import os

API_KEY=os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
model = "gemini-2.5-flash"

chat_obj = client.chats.create(model = model)
resp_str = "(Start talking to Gemini now)"
prompt = input(resp_str + '\n' + '-' * 80 + '\nYou: ')
while True:
    reply = chat_obj.send_message(message=prompt)
    # print(reply.candidates[0].content.parts[0].text)
    resp_str = reply.candidates[0].content.parts[0].text
    prompt = input('-' * 80+ '\nGemini: ' + resp_str +  '\n' + '-' * 80 + '\n' +"You: ")
    # print(resp_str)
    