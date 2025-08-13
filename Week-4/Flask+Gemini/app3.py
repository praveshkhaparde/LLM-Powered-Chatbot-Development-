# app.py
import os
from flask import Flask, request, session, render_template, redirect, url_for
from google import genai
import redis
from markdown import markdown
app = Flask(__name__,  template_folder = '.')
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.StrictRedis(host='localhost', port=6379, db=0)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
chat = client.chats.create(model="gemini-2.0-flash")

@app.route("/", methods=["GET", "POST"])
def chatbot_page():
    if not session.get('history'):
        print('History is empty')
        session['history'] = []


    print(session['history'], flush = True)
    
    reply = None
    if request.method == "POST":
        user_msg = request.form["message"].strip()
        session["history"].append({"role": "user", "parts": [{"text": user_msg}]})
        
        # print(session['history'], flush = True)
        resp = chat.send_message(message=user_msg)
        ai_text = resp.text
        reply =  markdown('**AI: **' + ai_text, extensions=["fenced_code", "codehilite"])
        session["history"].append({"role": "model", "parts": [{"text": reply}]})
        
        # print(session['history'], flush = True)
        session.modified = True
    return render_template("index2.html", history=session["history"], reply=reply)

@app.route("/clear_chat_history")
def clear_chat_history():
    """This does not work currently"""
    session.clear()
    chat.history = []
    # chat.__init__()
    return redirect(url_for("chatbot_page"))

@app.route("/clear")
def clear():
    session.clear()
    return redirect(url_for("chatbot_page"))

if __name__ == "__main__":
    app.run(debug=True)
