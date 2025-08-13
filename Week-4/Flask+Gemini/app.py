"""Sends a message to the Gemini Model and prints response
No memory/state handling, Gemini does not remember previous messages
Need to feed in context separately, NOT implemented in this file"""

from google import genai
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, render_template
import os
import markdown
API_KEY=os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
model = "gemini-2.5-flash"
app = Flask(__name__, template_folder = '.')

@app.route('/', methods = ['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        text = request.form.get('text_input')
        response = client.models.generate_content(
            model=model, 
            contents=text
        )
        result = response.text
        result = markdown.markdown(result, extensions=["fenced_code", "codehilite"])
    return render_template("index.html", result = result)


if __name__ == '__main__':
    app.run(debug = True)