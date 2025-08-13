const { marked } = require("marked"); // Response Mark-down to HTML
require("dotenv").config(); // Loads .env file contents into process.env
const express = require("express");
const session = require("express-session");
const { GoogleGenAI } = require("@google/genai");
const path = require("path");
const model = "gemini-2.0-flash";
const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json()); // .use() is 'middleware', feed it functions that you want to be run each time a request comes to the server
app.use(express.static(path.join(__dirname)));

app.use(
  session({
    secret: process.env.SESSION_SECRET || "dev-secret",
    resave: false,
    saveUninitialized: false,
    cookie: { maxAge: 86400000 },
  })
); // Express doesn't have builtin middleware, access data in req.session

// All class instances in JS are initialsised using 'new' keyword
const ai = new GoogleGenAI({ apiKey: process.env.GOOGLE_API_KEY });

// Server-side store for ChatSession instances
const CHAT_STORE = {};

async function initChat() {
  return ai.chats.create({ model: model });
}

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/chat", async (req, res) => {
  const sess = req.session;
  sess.history ||= [];

  // ensure session has an ID
  if (!sess.chatId) {
    sess.chatId = `${Date.now()}-${Math.random()}`;
  }

  // retrieve or create chat instance
  let chat = CHAT_STORE[sess.chatId];
  if (!chat) {
    chat = await initChat();
    CHAT_STORE[sess.chatId] = chat;
  }

  // append history
  const msg = req.body.message;
  sess.history.push({ role: "user", parts: [{ text: msg }] });

  // send message on the actual chat object
  const response = await chat.sendMessage({ message: msg });

  // Markdown to HTML
  const aiText = marked.parse(`**AI:** ${response.text}`);

  sess.history.push({ role: "model", parts: [{ text: aiText }] });
  sess.save();

  res.json({ text: aiText });
});

app.get("/clear", async (req, res) => {
  const sess = req.session;
  if (sess.chatId) {
    delete CHAT_STORE[sess.chatId]; // remove the chat instance
  }
  sess.chatId = null;
  sess.history = [];
  sess.save();

  res.json({ cleared: true });
});

app.listen(3000, () => console.log("Server running at http://localhost:3000")); // Starts the server
