## Week 4

This week, I learned how to access LLMs using their APIs, and with a lot of syntax help (especially for `node`, but also for `flask`), built a layer of UI to create a locally-hosted chatbot interface.

### Directory Contents

#### `API_Call_Gemini`
- First call to the Gemini API using `google.genai`
- Demonstrates how to authenticate and make basic content requests

#### `First_Flask_Webpage`
- Basic experimentation with a Flask backend
- Receives user inputs from a webpage and processes them using Python in the backend

#### `Flask+Gemini`
- `app.py`: Flask backend with Gemini API call logic (using `Client.models.generate_content`). This version does not retain chat memory. Uses `index.html` as the frontend template
- `app2.py`: A basic terminal-based chat app using `google.genai.Client.chats` that supports multi-turn interaction 
- `app3.py`: Final version combining Flask backend with chat memory (extends `app2.py`) and includes a slightly better UI using `index2.html` as the webpage template (supports markdown for output formatting)

#### `node_website`
- `server.js` handles the communication with the API using `@google/genai.chats`, `express` and `express-session` are helpful for backend-handling and middleware utilities (e.g. `express.json()`)
- `index.html` is the webpage, `style.css` is the stylesheet
